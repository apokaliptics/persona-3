<script>
  let { label, index, color = "cyan", isSkill = false } = $props();

  // Pseudo-randomizing tilt between -22deg and -4deg for a more aggressive chaotic look
  const tilt = -13 + Math.sin(index * 123.45) * 9;
</script>

<div
  class="menu-item-wrapper"
  style="transform: translateX({(index - 4.5) * (index - 4.5) * 0.4 -
    5}vw); z-index: {20 - index};"
>
  <div class="menu-item-inner">
    <button
      class="menu-btn {color}"
      style="transform: skewX(-20deg) rotate({tilt}deg);"
    >
      <!-- Layered Lighting Triangles -->
      <div class="lighting-layer triangle-back"></div>
      <div class="lighting-layer triangle-front"></div>
      <span class="btn-text">{label}</span>
    </button>
  </div>
</div>

<style>
  .menu-item-wrapper {
    position: relative;
    margin: -1.5vh 0; /* Increased negative margin for words to overlap strongly */
    display: flex;
    align-items: center;
    padding: 15px 10px; /* Generous padding to prevent hover loss */
  }

  .menu-item-inner {
    position: relative;
    display: flex;
    align-items: center;
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }

  .menu-item-wrapper:hover {
    z-index: 10;
  }

  .menu-item-wrapper:hover .menu-item-inner {
    transform: translateX(10px) scale(1.05);
  }

  .lighting-layer {
    position: absolute;
    top: -20px;
    bottom: -20px;
    left: -40px;
    right: -40px;
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    pointer-events: none;
    z-index: 1;
  }

  .triangle-back {
    background: linear-gradient(
      135deg,
      rgba(255, 71, 133, 0.9),
      rgba(0, 240, 255, 0.3)
    );
    clip-path: polygon(100% 0, 0 50%, 100% 100%);
    transform: translateX(40px) scale(0.9);
    filter: blur(4px); /* Lighting glow effect */
  }

  .triangle-front {
    background-image: url("/hover-texture.png");
    background-size: cover;
    background-position: center;
    clip-path: polygon(95% 10%, 5% 50%, 95% 90%);
    transform: translateX(20px) scale(0.85);
    mix-blend-mode: screen;
  }

  /* User request for 30% texture and layered lighting */
  .menu-item-wrapper:hover .triangle-back {
    opacity: 0.6;
    transform: translateX(-10px) scale(1);
  }

  .menu-item-wrapper:hover .triangle-front {
    opacity: 0.3;
    transform: translateX(-10px) scale(1);
  }

  .menu-btn {
    position: relative;
    background: none;
    border: none;
    cursor: pointer;
    font-family: inherit;
    font-size: min(6vw, 5rem);
    font-style: italic;
    font-weight: normal;
    line-height: 0.9;
    letter-spacing: -3px;
    text-transform: uppercase;
    transform: skewX(-15deg);
    padding: 0 40px;
    outline: none;
    z-index: 2;
  }

  .btn-text {
    position: relative;
    z-index: 2;
    display: inline-block;
    color: transparent;
    -webkit-text-stroke: 2px currentColor;
    transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* Pop out from background */
  }

  /* Base color classes */
  .white .btn-text {
    -webkit-text-stroke-color: #fff;
    color: #fff;
  }
  .cyan .btn-text {
    -webkit-text-stroke-color: var(--highlight-cyan);
    color: var(--highlight-cyan);
  }
  .darkblue .btn-text {
    -webkit-text-stroke-color: rgba(6, 68, 161, 0.9);
    color: rgba(6, 68, 161, 0.9);
  }

  /* Hover state for text */
  .menu-item-wrapper:hover .btn-text {
    color: var(--pink-hover);
    -webkit-text-stroke-color: var(--pink-hover);
    text-shadow:
      0 0 15px rgba(255, 71, 133, 0.8),
      2px 2px 0px rgba(0, 0, 0, 0.8);
    transform: translateX(10px);
  }
</style>
