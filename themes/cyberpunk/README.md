# Cyberpunk Theme

A futuristic, high-contrast theme inspired by cyberpunk aesthetics with neon colors and glowing effects.

## Features

- **Dark Background**: Deep black primary background with subtle grid pattern
- **Neon Colors**: Vibrant cyan, magenta, and green accent colors
- **Glowing Effects**: Text shadows and box shadows create authentic neon glow
- **Monospace Typography**: Courier New font family for that terminal feel
- **High Contrast**: Excellent readability with bright text on dark backgrounds
- **Animated Elements**: Subtle animations including scanning lines and pulse effects
- **Terminal Styling**: Special terminal-like code blocks and containers
- **Responsive Design**: Optimized for both desktop and mobile devices

## Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Background | `#0a0a0a` | Main background |
| Secondary Background | `#1a1a2e` | Panels, inputs |
| Tertiary Background | `#16213e` | Focused elements |
| Cyan | `#00ffff` | Primary accent, headers |
| Magenta | `#ff00ff` | Secondary accent, hover states |
| Green | `#00ff41` | Success states, code blocks |
| Yellow | `#ffff00` | Warning states |
| Red | `#ff073a` | Error states |

## Installation

1. Download the `cyberpunk.css` file
2. Place it in your themes directory
3. Import or link the CSS file in your application:

```html
<link rel="stylesheet" href="path/to/cyberpunk.css">
```

Or import in your CSS:

```css
@import url('path/to/cyberpunk.css');
```

## Usage

The theme automatically styles standard HTML elements. For enhanced effects, use these special classes:

### Status Indicators
```html
<span class="status-online">Online</span>
<span class="status-warning">Warning</span>
<span class="status-error">Error</span>
```

### Containers
```html
<div class="container">Main content area</div>
<div class="panel">Panel with scanning line effect</div>
```

### Terminal Style
```html
<div class="terminal">
  <div class="terminal-prompt">ls -la</div>
  <div>total 42</div>
  <div>drwxr-xr-x 2 user user 4096 Jan 1 12:00 .</div>
</div>
```

### Animations
```html
<div class="flicker">Flickering text</div>
<div class="pulse">Pulsing element</div>
```

## Screenshots

![Cyberpunk Theme Preview](screenshot.png)

*Screenshot showing the cyberpunk theme in action*

## Customization

The theme uses CSS custom properties (variables) for easy customization. Override these variables to modify colors:

```css
:root {
  --cyberpunk-cyan: #00ffff;
  --cyberpunk-magenta: #ff00ff;
  --cyberpunk-green: #00ff41;
  /* Add your custom colors */
}
```

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License

Copyright Jascha Wanger 2025. All rights reserved.

## Contributing

Please see the main repository's [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines on contributing to this theme.

## Issues

If you encounter any issues with this theme, please report them in the main repository's issue tracker.