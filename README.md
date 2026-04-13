# Persona 3 Reload UI Implementation

A web-based recreation of the iconic, highly stylized Persona 3 menu interface built entirely with Svelte 5 and CSS. This project focuses on pure CSS aesthetics, avoiding heavy 3D rendering libraries like WebGL or Three.js in favor of standard transform math, layered blend modes, and CSS animations.

## Features

- **Fluid Curved Menu:** The menu items follow a mathematical quadratic curve (parabola) to dynamically scale and curve around background elements, perfectly matching the original slanted menu style.
- **Aggressive Chaotic Tilt:** Each list item utilizes a scripted pseudo-random formula (`Math.sin(index)`) to generate a unique, aggressive baseline slant while keeping the overarching italic lean consistent.
- **Layered Lighting Cursors:** On hover, the components spawn a dual-layered, skewed highlight layer leveraging `mix-blend-mode: screen`, gaussian blurs across CSS gradients, and textured backgrounds.
- **Dynamic Stack Depth:** Heavy usage of negative margins paired with a reverse-ordered `z-index` so that the slanted words geometrically stack on top of each other.
- **Fullscreen Video Background:** Clean, muted, full-bleed autoplaying video integration to support dynamic shifting water effects mirroring the game's actual main menu loop.

## Setup & Installation

This project is built using modern **Svelte 5** and **Vite**.

### Prerequisites
- Node.js (v18+ recommended)
- npm or pnpm

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/apokaliptics/persona-3.git
   cd persona-3
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the Development Server:**
   Launch the high-performance Vite dev server with hot-module replacement (HMR).
   ```bash
   npm run dev
   ```
   Open `http://localhost:5173/` in your browser.

## Project Structure

- `src/App.svelte`: The main application boundary. It houses the fullscreen layout styling, the underlying `background-real.mp4` video layer, and the dataset array containing the navigation items.
- `src/lib/MenuButton.svelte`: The complex button component. This handles the mathematical curve offsets, pseudo-random tilt calculations, and the intricate hover lighting pseudo-DOM elements.
- `src/app.css`: The global stylesheet defining the deep blue aesthetics, the custom fallback font stacks targeting `Rodin Pro -> Rubik`, and global resets.
- `public/`: Assets directory containing `background-real.mp4`, and `hover-texture.png`. Since they are in `public`, they aren't processed by Vite and are accessed via standard root path (`/`).

## How to Customize

### Adjusting the Curve
If you need to change how sharply the menu hugs the left side of the screen, adjust the multiplier inner math inside `src/lib/MenuButton.svelte`:
```svelte
<div style="transform: translateX({(index - 4.5) * (index - 4.5) * [YOUR MULTIPLIER] - [OFFSET]}vw);">
```

### Adjusting Chaotic Tilt
Inside `src/lib/MenuButton.svelte`, the `tilt` variable handles how wild the rotational offset is per word.
```javascript
// Change the multipliers to reduce or increase the aggressive tilt limits
const tilt = -13 + Math.sin(index * 123.45) * 9;
```

## Production Build

To build the optimized static asset payload for production environments (like Vercel, Netlify, or Github Pages):
```bash
npm run build
```
This produces a `/dist` folder containing minified CSS/JS and localized assets.

To preview your production build locally:
```bash
npm run preview
```
