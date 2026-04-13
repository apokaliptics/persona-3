<script>
  let { label, index, color = "cyan", isSkill = false } = $props();
</script>

<div class="menu-item-wrapper" style="transform: translateX({index * -5}vw);">
  <div class="menu-item-inner">
    {#if isSkill}
      <div class="skill-bg"></div>
    {/if}
    
    <div class="hover-bg"></div>
    
    <button class="menu-btn {color}">
      <span class="btn-text">{label}</span>
    </button>
  </div>
</div>

<style>
  .menu-item-wrapper {
    position: relative;
    margin: -1vh 0; /* Overlap buttons vertically slightly to make them tight */
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

  .hover-bg {
    position: absolute;
    top: 5px;
    left: 0px;
    right: 0px;
    bottom: 5px;
    background-image: url('/hover-texture.png');
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 0.2s, transform 0.2s;
    pointer-events: none;
    z-index: 1;
    clip-path: polygon(10% 0, 100% 0, 90% 100%, 0 100%);
    transform: skewX(-15deg);
  }

  /* User request: "use the first texture as the texture as the user hovers through the button however remember to adjust opacity to like 30% so that it doesn't hide the entire button" */
  .menu-item-wrapper:hover .hover-bg {
    opacity: 0.3;
  }

  .menu-btn {
    position: relative;
    background: none;
    border: none;
    cursor: pointer;
    font-family: inherit;
    font-size: min(6vw, 5rem);
    font-style: italic;
    font-weight: 900;
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
    text-shadow: 2px 2px 5px rgba(0,0,0,0.5); /* Pop out from background */
  }

  /* Base color classes */
  .white .btn-text { -webkit-text-stroke-color: #fff; color: #fff;}
  .cyan .btn-text { -webkit-text-stroke-color: var(--highlight-cyan); color: var(--highlight-cyan); }
  .darkblue .btn-text { -webkit-text-stroke-color: rgba(6, 68, 161, 0.9); color: rgba(6, 68, 161, 0.9); }

  /* Hover state for text */
  .menu-item-wrapper:hover .btn-text {
    color: var(--pink-hover);
    -webkit-text-stroke-color: var(--pink-hover);
    text-shadow: 0 0 15px rgba(255, 71, 133, 0.8), 2px 2px 0px rgba(0,0,0,0.8);
    transform: translateX(10px);
  }

  /* Special SKILL visual layout (Persona 3 reference) */

  .skill-bg {
    position: absolute;
    top: -10%;
    left: 20px;
    width: 300px;
    height: 120%;
    background-color: var(--pink-bg);
    clip-path: polygon(15% 0, 100% 0, 85% 100%, 0 100%);
    z-index: 1;
    transform: skewX(-15deg);
    box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
  }
</style>
