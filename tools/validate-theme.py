#!/usr/bin/env python3
"""
Theme Validation Tool for Tootles Themes
Copyright Jascha Wanger 2025

This script validates CSS theme files to ensure they meet the requirements
for Tootles themes, including proper structure, required variables, and
accessibility standards.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List


class ThemeValidator:
    """Validates CSS theme files for Tootles compatibility."""
    
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.required_variables = {
            '--bg-primary',
            '--bg-secondary',
            '--text-primary',
            '--text-secondary',
            '--accent-primary',
            '--border-color',
            '--font-family-primary'
        }
        self.recommended_variables = {
            '--bg-tertiary',
            '--text-muted',
            '--accent-secondary',
            '--color-success',
            '--color-warning',
            '--color-error',
            '--border-focus',
            '--font-family-mono'
        }
    
    def validate_file(self, file_path: Path) -> bool:
        """
        Validate a CSS theme file.
        
        Args:
            file_path: Path to the CSS file to validate
            
        Returns:
            True if validation passes, False otherwise
        """
        if not file_path.exists():
            self.errors.append(f"File not found: {file_path}")
            return False
        
        if not file_path.suffix.lower() == '.css':
            self.errors.append(f"File must have .css extension: {file_path}")
            return False
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            self.errors.append(f"File must be UTF-8 encoded: {file_path}")
            return False
        
        # Run validation checks
        self._validate_copyright(content, file_path)
        self._validate_css_variables(content)
        self._validate_css_syntax(content)
        self._validate_accessibility(content)
        self._validate_structure(content)
        
        return len(self.errors) == 0
    
    def _validate_copyright(self, content: str, file_path: Path) -> None:
        """Validate that the file contains proper copyright notice."""
        copyright_pattern = r'/\*.*?Copyright\s+Jascha\s+Wanger\s+2025.*?\*/'
        if not re.search(copyright_pattern, content, re.IGNORECASE | re.DOTALL):
            self.errors.append(
                "Missing or invalid copyright notice. "
                "Expected: /* ... Copyright Jascha Wanger 2025 ... */"
            )
    
    def _validate_css_variables(self, content: str) -> None:
        """Validate that required CSS variables are defined."""
        # Extract all CSS variables
        found_variables = set(re.findall(r'(--[\w-]+)', content))
        
        # Check required variables
        missing_required = self.required_variables - found_variables
        if missing_required:
            self.errors.append(
                f"Missing required CSS variables: {', '.join(sorted(missing_required))}"
            )
        
        # Check recommended variables
        missing_recommended = self.recommended_variables - found_variables
        if missing_recommended:
            self.warnings.append(
                f"Missing recommended CSS variables: {', '.join(sorted(missing_recommended))}"
            )
    
    def _validate_css_syntax(self, content: str) -> None:
        """Basic CSS syntax validation."""
        # Check for balanced braces
        open_braces = content.count('{')
        close_braces = content.count('}')
        if open_braces != close_braces:
            self.errors.append(
                f"Unbalanced braces: {open_braces} opening, {close_braces} closing"
            )
        
        # Check for common syntax errors
        if re.search(r'[^;{}]\s*}', content):
            self.warnings.append("Possible missing semicolon before closing brace")
        
        # Check for empty rules
        empty_rules = re.findall(r'[^{}]+\{\s*\}', content)
        if empty_rules:
            self.warnings.append(f"Found {len(empty_rules)} empty CSS rules")
    
    def _validate_accessibility(self, content: str) -> None:
        """Validate accessibility considerations."""
        # Check for focus styles
        if not re.search(r':focus\b', content):
            self.warnings.append("No focus styles found - consider adding for accessibility")
        
        # Check for reduced motion support
        if not re.search(r'prefers-reduced-motion', content):
            self.warnings.append(
                "No reduced motion support found - consider adding for accessibility"
            )
        
        # Check for high contrast considerations
        if not re.search(r'contrast|accessibility', content, re.IGNORECASE):
            self.warnings.append(
                "Consider adding high contrast mode support for accessibility"
            )
    
    def _validate_structure(self, content: str) -> None:
        """Validate theme structure and organization."""
        # Check for :root selector
        if not re.search(r':root\s*\{', content):
            self.errors.append("Missing :root selector for CSS variables")
        
        # Check for basic element styles
        required_elements = ['body', 'h1', 'a', 'button']
        for element in required_elements:
            if not re.search(rf'\b{element}\b\s*[,{{]', content):
                self.warnings.append(f"No styles found for {element} element")
        
        # Check for responsive design
        if not re.search(r'@media', content):
            self.warnings.append("No media queries found - consider responsive design")
    
    def get_validation_report(self) -> str:
        """Generate a formatted validation report."""
        report = []
        
        if self.errors:
            report.append("ERRORS:")
            for error in self.errors:
                report.append(f"  ❌ {error}")
            report.append("")
        
        if self.warnings:
            report.append("WARNINGS:")
            for warning in self.warnings:
                report.append(f"  ⚠️  {warning}")
            report.append("")
        
        if not self.errors and not self.warnings:
            report.append("✅ Theme validation passed!")
        elif not self.errors:
            report.append("✅ Theme validation passed with warnings.")
        else:
            report.append("❌ Theme validation failed.")
        
        return "\n".join(report)


def validate_theme_directory(theme_dir: Path) -> bool:
    """
    Validate all CSS files in a theme directory.
    
    Args:
        theme_dir: Path to theme directory
        
    Returns:
        True if all validations pass, False otherwise
    """
    css_files = list(theme_dir.glob("*.css"))
    if not css_files:
        print(f"No CSS files found in {theme_dir}")
        return False
    
    all_valid = True
    for css_file in css_files:
        print(f"\nValidating {css_file.name}...")
        validator = ThemeValidator()
        is_valid = validator.validate_file(css_file)
        print(validator.get_validation_report())
        
        if not is_valid:
            all_valid = False
    
    return all_valid


def main():
    """Main entry point for the theme validator."""
    parser = argparse.ArgumentParser(
        description="Validate Tootles theme CSS files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s theme.css                    # Validate single file
  %(prog)s themes/cyberpunk/            # Validate directory
  %(prog)s --strict theme.css           # Treat warnings as errors
        """
    )
    
    parser.add_argument(
        'path',
        type=Path,
        help='Path to CSS file or directory to validate'
    )
    
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Only show errors and final result'
    )
    
    args = parser.parse_args()
    
    if not args.path.exists():
        print(f"Error: Path does not exist: {args.path}")
        return 1
    
    success = True
    
    if args.path.is_file():
        # Validate single file
        validator = ThemeValidator()
        is_valid = validator.validate_file(args.path)
        
        if not args.quiet:
            print(validator.get_validation_report())
        
        if args.strict and validator.warnings:
            is_valid = False
        
        success = is_valid
    
    elif args.path.is_dir():
        # Validate directory
        success = validate_theme_directory(args.path)
        
        if args.strict:
            # Re-validate with strict mode
            css_files = list(args.path.glob("*.css"))
            for css_file in css_files:
                validator = ThemeValidator()
                validator.validate_file(css_file)
                if validator.warnings:
                    success = False
                    if not args.quiet:
                        print(f"Strict mode: Warnings in {css_file.name} treated as errors")
    
    else:
        print(f"Error: Path must be a file or directory: {args.path}")
        return 1
    
    if success:
        if not args.quiet:
            print("\n🎉 All validations passed!")
        return 0
    else:
        if not args.quiet:
            print("\n💥 Validation failed!")
        return 1


if __name__ == '__main__':
    sys.exit(main())