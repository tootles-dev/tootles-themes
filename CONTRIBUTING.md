# Contributing to Tootles Themes

Thank you for your interest in contributing to Tootles Themes! This document provides guidelines and instructions for contributing themes, templates, and tools to this repository.

## Table of Contents

- [Getting Started](#getting-started)
- [Theme Development](#theme-development)
- [Submission Guidelines](#submission-guidelines)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community Guidelines](#community-guidelines)

## Getting Started

### Prerequisites

- Basic knowledge of CSS and web design principles
- Understanding of CSS custom properties (variables)
- Familiarity with accessibility best practices
- Python 3.7+ (for using development tools)

### Development Setup

1. Fork the repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/tootles-themes.git
   cd tootles-themes
   ```
3. Create a new branch for your contribution:
   ```bash
   git checkout -b feature/your-theme-name
   ```

## Theme Development

### Creating a New Theme

1. **Choose a Theme Name**: Use lowercase with hyphens (e.g., `cyberpunk`, `minimal-dark`)

2. **Create Theme Directory**:
   ```
   themes/your-theme-name/
   ├── your-theme-name.css
   ├── README.md
   └── screenshot.png
   ```

3. **Use Templates**: Start with either:
   - [`templates/basic-template.css`](templates/basic-template.css) for simple themes
   - [`templates/advanced-template.css`](templates/advanced-template.css) for complex themes

### Required CSS Variables

All themes must define these essential CSS variables:

```css
:root {
  /* Background Colors */
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f5;
  
  /* Text Colors */
  --text-primary: #333333;
  --text-secondary: #666666;
  
  /* Accent Colors */
  --accent-primary: #007bff;
  
  /* Borders */
  --border-color: #dee2e6;
  
  /* Typography */
  --font-family-primary: -apple-system, BlinkMacSystemFont, sans-serif;
}
```

### Recommended CSS Variables

For enhanced functionality, include these variables:

```css
:root {
  --bg-tertiary: #e0e0e0;
  --text-muted: #999999;
  --accent-secondary: #0056b3;
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-error: #dc3545;
  --border-focus: var(--accent-primary);
  --font-family-mono: 'Courier New', monospace;
}
```

### Theme Structure

#### 1. Copyright Header
All CSS files must include:
```css
/* Theme Name - Copyright Jascha Wanger 2025 */
```

#### 2. CSS Organization
Organize your CSS in this order:
1. CSS Variables (`:root` selector)
2. Base styles (`body`, `html`)
3. Typography (`h1-h6`, `p`, `a`)
4. Components (`button`, `input`, `table`)
5. Utilities and helpers
6. Responsive design (`@media` queries)

#### 3. Dark Mode Support (Optional)
If supporting dark mode, use:
```css
[data-theme="dark"] {
  --bg-primary: #1a1a1a;
  --text-primary: #ffffff;
  /* ... other dark mode variables */
}
```

### Accessibility Requirements

- **Contrast Ratios**: Ensure WCAG AA compliance (4.5:1 for normal text, 3:1 for large text)
- **Focus Indicators**: Provide clear focus styles for interactive elements
- **Reduced Motion**: Support `prefers-reduced-motion` media query
- **Color Independence**: Don't rely solely on color to convey information

Example:
```css
/* Focus styles */
button:focus, input:focus {
  outline: 2px solid var(--accent-primary);
  outline-offset: 2px;
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Submission Guidelines

### Before Submitting

1. **Validate Your Theme**:
   ```bash
   python tools/validate-theme.py themes/your-theme-name/
   ```

2. **Generate Preview**:
   ```bash
   python tools/preview-generator.py themes/your-theme-name/your-theme-name.css
   ```

3. **Test Across Browsers**: Verify compatibility with:
   - Chrome/Chromium 90+
   - Firefox 88+
   - Safari 14+
   - Edge 90+

4. **Test Responsive Design**: Ensure theme works on:
   - Desktop (1200px+)
   - Tablet (768px - 1199px)
   - Mobile (320px - 767px)

### Pull Request Process

1. **Create Descriptive Commit Messages**:
   ```bash
   git commit -m "Add cyberpunk theme with neon styling"
   ```

2. **Push to Your Fork**:
   ```bash
   git push origin feature/your-theme-name
   ```

3. **Create Pull Request** with:
   - Clear title describing the theme
   - Description of theme features and inspiration
   - Screenshots or preview links
   - Confirmation of testing completed

### Pull Request Template

```markdown
## Theme: [Theme Name]

### Description
Brief description of the theme, its inspiration, and key features.

### Features
- [ ] Dark/Light mode support
- [ ] Responsive design
- [ ] Accessibility compliant
- [ ] Custom animations
- [ ] Special components

### Testing Checklist
- [ ] Validated with `validate-theme.py`
- [ ] Generated preview with `preview-generator.py`
- [ ] Tested on multiple browsers
- [ ] Tested on multiple screen sizes
- [ ] Verified accessibility compliance

### Screenshots
[Include screenshots or link to preview]
```

## Code Standards

### CSS Guidelines

1. **Use CSS Custom Properties**: Always use variables for colors, spacing, and fonts
2. **Mobile-First**: Write mobile styles first, then enhance for larger screens
3. **Consistent Naming**: Use kebab-case for class names and variables
4. **Comments**: Document complex styles and design decisions
5. **Performance**: Avoid expensive CSS operations and excessive nesting

### File Organization

```
themes/theme-name/
├── theme-name.css          # Main theme file
├── README.md              # Theme documentation
├── screenshot.png         # Theme preview image
└── variants/              # Optional: theme variants
    ├── theme-name-dark.css
    └── theme-name-light.css
```

### Documentation Standards

Each theme must include a `README.md` with:

1. **Theme Description**: What the theme looks like and its purpose
2. **Features List**: Key features and capabilities
3. **Installation Instructions**: How to use the theme
4. **Customization Guide**: How to modify colors and styles
5. **Browser Support**: Compatibility information
6. **Screenshots**: Visual examples of the theme

## Testing

### Automated Testing

Run the validation tool before submitting:

```bash
# Validate single theme
python tools/validate-theme.py themes/your-theme/your-theme.css

# Validate all themes in directory
python tools/validate-theme.py themes/your-theme/

# Strict mode (warnings as errors)
python tools/validate-theme.py --strict themes/your-theme/
```

### Manual Testing

1. **Visual Testing**: Generate and review HTML preview
2. **Accessibility Testing**: Use tools like axe-core or WAVE
3. **Performance Testing**: Check CSS file size and complexity
4. **Cross-Browser Testing**: Test in multiple browsers and devices

### Preview Generation

Generate HTML previews to test your theme:

```bash
# Generate preview for single theme
python tools/preview-generator.py themes/your-theme/your-theme.css

# Generate and open in browser
python tools/preview-generator.py --open themes/your-theme/your-theme.css
```

## Documentation

### Theme README Template

Use this template for theme documentation:

```markdown
# Theme Name

Brief description of the theme.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

Instructions for using the theme.

## Customization

How to customize colors and styles.

## Browser Support

Compatibility information.

## Screenshots

![Theme Preview](screenshot.png)

## License

Copyright Jascha Wanger 2025. All rights reserved.
```

### Code Comments

Document your CSS with helpful comments:

```css
/* === CYBERPUNK THEME VARIABLES === */
:root {
  /* Neon color palette inspired by cyberpunk aesthetics */
  --cyberpunk-cyan: #00ffff;    /* Primary neon accent */
  --cyberpunk-magenta: #ff00ff; /* Secondary neon accent */
  
  /* Glow effects for authentic neon look */
  --cyberpunk-glow: 0 0 10px currentColor, 0 0 20px currentColor;
}

/* === GLOWING TEXT EFFECT === */
.glow-text {
  /* Creates authentic neon glow using multiple text shadows */
  text-shadow: var(--cyberpunk-glow);
}
```

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and improve
- Follow project guidelines and standards

### Getting Help

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check existing documentation first

### Recognition

Contributors will be recognized in:
- Theme documentation
- Repository contributors list
- Release notes for significant contributions

## License and Copyright

- All themes must include "Copyright Jascha Wanger 2025" in CSS headers
- Themes are licensed under the same terms as the main project
- By contributing, you agree to license your work under these terms

## Questions?

If you have questions about contributing, please:

1. Check this documentation first
2. Search existing issues and discussions
3. Create a new issue with the "question" label
4. Be specific about what you need help with

Thank you for contributing to Tootles Themes! 🎨