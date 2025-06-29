#!/usr/bin/env python3
"""
Theme Preview Generator for Tootles Themes
Copyright Jascha Wanger 2025

This script generates HTML preview files for CSS themes, allowing developers
to visualize how their themes look with various UI components and content types.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional


class PreviewGenerator:
    """Generates HTML preview files for CSS themes."""
    
    def __init__(self):
        self.template_components = {
            'typography': self._generate_typography_section(),
            'buttons': self._generate_buttons_section(),
            'forms': self._generate_forms_section(),
            'tables': self._generate_tables_section(),
            'cards': self._generate_cards_section(),
            'alerts': self._generate_alerts_section(),
            'code': self._generate_code_section(),
            'navigation': self._generate_navigation_section()
        }
    
    def generate_preview(self, css_file: Path, output_file: Optional[Path] = None) -> Path:
        """
        Generate an HTML preview file for a CSS theme.
        
        Args:
            css_file: Path to the CSS theme file
            output_file: Optional output path for HTML file
            
        Returns:
            Path to the generated HTML file
        """
        if not css_file.exists():
            raise FileNotFoundError(f"CSS file not found: {css_file}")
        
        if output_file is None:
            output_file = css_file.parent / f"{css_file.stem}-preview.html"
        
        theme_name = css_file.stem.replace('-', ' ').title()
        html_content = self._generate_html_template(css_file, theme_name)
        
        output_file.write_text(html_content, encoding='utf-8')
        return output_file
    
    def _generate_html_template(self, css_file: Path, theme_name: str) -> str:
        """Generate the complete HTML template."""
        css_path = css_file.name
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{theme_name} Theme Preview</title>
    <link rel="stylesheet" href="{css_path}">
    <style>
        .preview-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .preview-section {{
            margin: 3rem 0;
            padding: 2rem;
            border: 1px solid var(--border-color, #ddd);
            border-radius: 8px;
        }}
        .preview-section h2 {{
            margin-top: 0;
            border-bottom: 2px solid var(--accent-primary, #007bff);
            padding-bottom: 0.5rem;
        }}
        .component-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }}
        .theme-info {{
            background: var(--bg-secondary, #f8f9fa);
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }}
        .color-palette {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }}
        .color-swatch {{
            padding: 1rem;
            border-radius: 4px;
            text-align: center;
            font-size: 0.875rem;
        }}
        .dark-mode-toggle {{
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
        }}
    </style>
</head>
<body>
    <div class="dark-mode-toggle">
        <button onclick="toggleDarkMode()" class="btn btn-secondary">
            🌓 Toggle Dark Mode
        </button>
    </div>

    <div class="preview-container">
        <header>
            <h1>{theme_name} Theme Preview</h1>
            <div class="theme-info">
                <p><strong>Theme:</strong> {theme_name}</p>
                <p><strong>CSS File:</strong> {css_path}</p>
                <p><strong>Generated:</strong> <span id="generated-date"></span></p>
                <p>This preview demonstrates how the theme styles various UI components and content types.</p>
            </div>
        </header>

        {self._generate_all_sections()}
    </div>

    <script>
        // Set generated date
        document.getElementById('generated-date').textContent = new Date().toLocaleString();
        
        // Dark mode toggle
        function toggleDarkMode() {{
            const body = document.body;
            const currentTheme = body.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        }}
        
        // Load saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {{
            document.body.setAttribute('data-theme', savedTheme);
        }}
    </script>
</body>
</html>"""
    
    def _generate_all_sections(self) -> str:
        """Generate all preview sections."""
        sections = []
        for section_name, section_content in self.template_components.items():
            sections.append(f"""
        <section class="preview-section">
            <h2>{section_name.title()}</h2>
            {section_content}
        </section>""")
        return '\n'.join(sections)
    
    def _generate_typography_section(self) -> str:
        """Generate typography preview section."""
        return """
            <h1>Heading 1 - Main Title</h1>
            <h2>Heading 2 - Section Title</h2>
            <h3>Heading 3 - Subsection</h3>
            <h4>Heading 4 - Minor Heading</h4>
            <h5>Heading 5 - Small Heading</h5>
            <h6>Heading 6 - Smallest Heading</h6>
            
            <p>This is a regular paragraph with <strong>bold text</strong>, <em>italic text</em>, 
            and <a href="#">a sample link</a>. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            
            <blockquote>
                This is a blockquote. It's used for highlighting important quotes or 
                excerpts from other sources.
            </blockquote>
            
            <ul>
                <li>Unordered list item 1</li>
                <li>Unordered list item 2</li>
                <li>Unordered list item 3</li>
            </ul>
            
            <ol>
                <li>Ordered list item 1</li>
                <li>Ordered list item 2</li>
                <li>Ordered list item 3</li>
            </ol>
        """
    
    def _generate_buttons_section(self) -> str:
        """Generate buttons preview section."""
        return """
            <div class="component-grid">
                <div>
                    <h4>Primary Buttons</h4>
                    <button class="btn btn-primary">Primary Button</button>
                    <button class="btn btn-primary" disabled>Disabled Primary</button>
                </div>
                <div>
                    <h4>Secondary Buttons</h4>
                    <button class="btn btn-secondary">Secondary Button</button>
                    <button class="btn btn-secondary" disabled>Disabled Secondary</button>
                </div>
                <div>
                    <h4>Outline Buttons</h4>
                    <button class="btn btn-outline">Outline Button</button>
                    <button class="btn btn-outline" disabled>Disabled Outline</button>
                </div>
                <div>
                    <h4>Button Sizes</h4>
                    <button class="btn btn-primary btn-sm">Small</button>
                    <button class="btn btn-primary">Regular</button>
                    <button class="btn btn-primary btn-lg">Large</button>
                </div>
            </div>
        """
    
    def _generate_forms_section(self) -> str:
        """Generate forms preview section."""
        return """
            <form>
                <div style="margin-bottom: 1rem;">
                    <label for="text-input">Text Input:</label>
                    <input type="text" id="text-input" class="form-control" placeholder="Enter text here">
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="email-input">Email Input:</label>
                    <input type="email" id="email-input" class="form-control" placeholder="user@example.com">
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="password-input">Password Input:</label>
                    <input type="password" id="password-input" class="form-control" placeholder="Password">
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="select-input">Select Dropdown:</label>
                    <select id="select-input" class="form-control">
                        <option>Option 1</option>
                        <option>Option 2</option>
                        <option>Option 3</option>
                    </select>
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label for="textarea-input">Textarea:</label>
                    <textarea id="textarea-input" class="form-control" rows="4" 
                              placeholder="Enter multiple lines of text here..."></textarea>
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label>
                        <input type="checkbox"> Checkbox option
                    </label>
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <label>
                        <input type="radio" name="radio-group"> Radio option 1
                    </label>
                    <label>
                        <input type="radio" name="radio-group"> Radio option 2
                    </label>
                </div>
                
                <button type="submit" class="btn btn-primary">Submit Form</button>
                <button type="reset" class="btn btn-secondary">Reset</button>
            </form>
        """
    
    def _generate_tables_section(self) -> str:
        """Generate tables preview section."""
        return """
            <table class="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>John Doe</td>
                        <td>john@example.com</td>
                        <td>Administrator</td>
                        <td><span class="text-success">Active</span></td>
                    </tr>
                    <tr>
                        <td>Jane Smith</td>
                        <td>jane@example.com</td>
                        <td>Editor</td>
                        <td><span class="text-warning">Pending</span></td>
                    </tr>
                    <tr>
                        <td>Bob Johnson</td>
                        <td>bob@example.com</td>
                        <td>Viewer</td>
                        <td><span class="text-danger">Inactive</span></td>
                    </tr>
                </tbody>
            </table>
        """
    
    def _generate_cards_section(self) -> str:
        """Generate cards preview section."""
        return """
            <div class="component-grid">
                <div class="card">
                    <div class="card-header">
                        <h4>Card Title</h4>
                    </div>
                    <div class="card-body">
                        <p>This is a basic card with header, body, and footer sections.</p>
                        <button class="btn btn-primary">Action</button>
                    </div>
                    <div class="card-footer">
                        <small class="text-muted">Last updated 3 mins ago</small>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-body">
                        <h4>Simple Card</h4>
                        <p>This card only has a body section with some content and actions.</p>
                        <a href="#" class="btn btn-outline">Learn More</a>
                    </div>
                </div>
            </div>
        """
    
    def _generate_alerts_section(self) -> str:
        """Generate alerts preview section."""
        return """
            <div class="alert alert-success">
                <strong>Success!</strong> This is a success alert message.
            </div>
            
            <div class="alert alert-info">
                <strong>Info:</strong> This is an informational alert message.
            </div>
            
            <div class="alert alert-warning">
                <strong>Warning!</strong> This is a warning alert message.
            </div>
            
            <div class="alert alert-danger">
                <strong>Error!</strong> This is an error alert message.
            </div>
        """
    
    def _generate_code_section(self) -> str:
        """Generate code preview section."""
        return """
            <p>Inline code example: <code>const variable = 'value';</code></p>
            
            <h4>Code Block Example:</h4>
            <pre><code>function greetUser(name) {
    if (!name) {
        throw new Error('Name is required');
    }
    
    return `Hello, ${name}! Welcome to the application.`;
}

// Usage example
try {
    const greeting = greetUser('Alice');
    console.log(greeting);
} catch (error) {
    console.error('Error:', error.message);
}</code></pre>
        """
    
    def _generate_navigation_section(self) -> str:
        """Generate navigation preview section."""
        return """
            <nav style="margin-bottom: 2rem;">
                <ul style="list-style: none; padding: 0; display: flex; gap: 1rem;">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
            
            <div style="margin: 2rem 0;">
                <h4>Breadcrumb Navigation:</h4>
                <nav>
                    <a href="#">Home</a> &gt; 
                    <a href="#">Category</a> &gt; 
                    <span>Current Page</span>
                </nav>
            </div>
        """


def main():
    """Main entry point for the preview generator."""
    parser = argparse.ArgumentParser(
        description="Generate HTML preview files for Tootles themes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s theme.css                           # Generate preview for single theme
  %(prog)s theme.css -o custom-preview.html    # Specify output file
  %(prog)s themes/cyberpunk/                   # Generate previews for all themes in directory
        """
    )
    
    parser.add_argument(
        'path',
        type=Path,
        help='Path to CSS file or directory containing themes'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output HTML file path (for single file mode)'
    )
    
    parser.add_argument(
        '--open',
        action='store_true',
        help='Open generated preview in default browser'
    )
    
    args = parser.parse_args()
    
    if not args.path.exists():
        print(f"Error: Path does not exist: {args.path}")
        return 1
    
    generator = PreviewGenerator()
    generated_files = []
    
    try:
        if args.path.is_file():
            # Generate preview for single file
            if not args.path.suffix.lower() == '.css':
                print(f"Error: File must have .css extension: {args.path}")
                return 1
            
            output_file = generator.generate_preview(args.path, args.output)
            generated_files.append(output_file)
            print(f"Generated preview: {output_file}")
        
        elif args.path.is_dir():
            # Generate previews for all CSS files in directory
            css_files = list(args.path.glob("*.css"))
            if not css_files:
                print(f"No CSS files found in {args.path}")
                return 1
            
            for css_file in css_files:
                output_file = generator.generate_preview(css_file)
                generated_files.append(output_file)
                print(f"Generated preview: {output_file}")
        
        else:
            print(f"Error: Path must be a file or directory: {args.path}")
            return 1
        
        # Open in browser if requested
        if args.open and generated_files:
            import webbrowser
            for file_path in generated_files:
                webbrowser.open(f"file://{file_path.absolute()}")
        
        print(f"\n✅ Successfully generated {len(generated_files)} preview file(s)")
        return 0
    
    except Exception as e:
        print(f"Error generating preview: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())