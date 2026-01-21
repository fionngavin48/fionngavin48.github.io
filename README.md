# Portfolio Website

A modern, cyberpunk-themed personal portfolio website built with pure HTML, CSS, and vanilla JavaScript. Features a sleek dark design with glitch effects, smooth animations, and interactive elements.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

## 🚀 Features

- **Responsive Design** - Fully optimized for desktop, tablet, and mobile devices
- **Glitch Effect** - Interactive text glitch animation on name hover
- **Smooth Animations** - Fade-in and slide animations for enhanced user experience
- **Copy to Clipboard** - One-click email copy with visual feedback tooltip
- **Film Grain Effect** - Subtle texture overlay for aesthetic appeal
- **Custom Scrollbar** - Themed scrollbar matching the overall design
- **Project Showcase** - Grid layout displaying projects with hover effects
- **Social Links** - Quick access to GitHub, LinkedIn, and email

## 🛠️ Technologies Used

- **HTML5** - Semantic markup structure
- **CSS3** - Custom animations, flexbox, grid, and CSS variables
- **JavaScript** - Clipboard API integration and DOM manipulation
- **Google Fonts** - IBM Plex Mono & Space Mono typefaces

## 📁 Project Structure

```
portfolio/
│
├── index.html          # Main HTML structure
├── styles.css          # All styling and animations
└── README.md           # Project documentation
```

## 🎨 Design Highlights

### Color Palette
- **Primary Background**: `#000000` (Pure Black)
- **Secondary Background**: `#0a0a0a` (Near Black)
- **Accent Blue**: `#4a9eff` (Bright Blue)
- **Accent Cyan**: `#00d9ff` (Electric Cyan)
- **Text Primary**: `#ffffff` (White)
- **Text Secondary**: `#b0b0b0` (Light Gray)

### Typography
- **Headers**: Space Mono (Monospace)
- **Body**: IBM Plex Mono (Monospace)

### Key CSS Features
- CSS Grid for project layout
- CSS Flexbox for responsive elements
- CSS Custom Properties (variables) for theming
- Keyframe animations for smooth transitions
- Pseudo-elements for decorative effects

## 🚦 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- A text editor (VS Code, Sublime Text, etc.)
- Git (optional, for cloning)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/fionngavin48/fionngavin48.github.io.git
```

2. **Navigate to the project directory**
```bash
cd fionngavin48.github.io
```

3. **Open in browser**
```bash
# Simply open index.html in your preferred browser
# Or use a local server:
python -m http.server 8000
# Then visit http://localhost:8000
```

## 📝 Customization

### Updating Personal Information

1. **Change name and title** - Edit the header section in `index.html`:
```html
<h1 class="glitch" data-text="YOUR NAME">YOUR NAME</h1>
<p class="subtitle">Your Title <span class="dot">•</span> Your Field</p>
```

2. **Update email address** - Modify both the link and JavaScript:
```html
<a href="mailto:your.email@example.com" class="link-btn email-btn" id="emailBtn">
```
```javascript
const email = 'your.email@example.com';
```

3. **Change social links** - Update href attributes in the header:
```html
<a href="https://github.com/yourusername" target="_blank" class="link-btn">
```

### Adding Projects

Add new project cards in the projects section:
```html
<div class="project-card">
  <div class="project-header">
    <h3 class="project-title">PROJECT NAME</h3>
    <span class="project-tag">TECH</span>
  </div>
  <p class="project-description">Your project description here.</p>
  <a href="https://github.com/yourusername/project" class="project-link" target="_blank">View Project →</a>
</div>
```

### Modifying Colors

Edit CSS custom properties in `styles.css`:
```css
:root {
  --bg-primary: #000000;
  --accent-green: #4a9eff;
  --accent-cyan: #00d9ff;
  /* Add or modify variables */
}
```

## ✨ Features Breakdown

### Glitch Effect
Hover over the main heading to see a cyberpunk-style glitch animation that splits the text into multiple colored layers.

### Copy to Clipboard
Click the email button to automatically copy the email address and see a confirmation tooltip appear near your cursor.

### Responsive Grid
The projects section uses CSS Grid with `auto-fit` and `minmax()` for a responsive layout that adapts to any screen size.

### Animation Sequence
Elements fade in sequentially on page load using staggered animation delays for a polished appearance.

## 🐛 Known Issues

- None currently reported

## 🔜 Future Enhancements

- [ ] Dark/Light theme toggle
- [ ] Project filtering by technology
- [ ] Blog section integration
- [ ] Contact form with backend integration
- [ ] Performance optimization with lazy loading
- [ ] Accessibility improvements (ARIA labels)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Fionn Gavin**
- GitHub: [@fionngavin48](https://github.com/fionngavin48)
- LinkedIn: [fionngavin](https://linkedin.com/in/fionngavin)
- Email: fgavin@tcd.ie

## 🙏 Acknowledgments

- Font families from [Google Fonts](https://fonts.google.com/)
- Icons from inline SVG
- Inspiration from cyberpunk and terminal aesthetics

## 📊 Browser Support

| Browser | Version |
|---------|---------|
| Chrome  | ✅ Latest |
| Firefox | ✅ Latest |
| Safari  | ✅ Latest |
| Edge    | ✅ Latest |

---

⭐ Star this repository if you found it helpful!

**Built with ❤️ by Fionn Gavin**
