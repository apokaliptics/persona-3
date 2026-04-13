<script>
  import './app.css';
  import MenuButton from './lib/MenuButton.svelte';

  const menuItems = [
    { label: "SKILL", color: "cyan" },
    { label: "ITEM", color: "cyan" },
    { label: "EQUIP", color: "cyan" },
    { label: "PERSONA", color: "cyan" },
    { label: "STATS", color: "darkblue" },
    { label: "QUEST", color: "darkblue" },
    { label: "SOCIAL LINK", color: "darkblue" },
    { label: "CALENDAR", color: "darkblue" },
    { label: "SYSTEM", color: "cyan" }
  ];
</script>

<div class="app-container">
  <!-- Dynamic Background Stairs removed as requested -->

  <!-- Water reflection overlay pattern -->
  <div class="bg-layer"></div>

  <!-- Main character image/video -->
  <div class="character-wrapper">
    <video src="/background-real.mp4" autoplay loop muted playsinline class="character-image"></video>
  </div>

  <!-- Right Side Interactive Menu (Staircase list) -->
  <nav class="menu-container">
    {#each menuItems as item, index}
      <MenuButton 
        label={item.label} 
        index={index} 
        isSkill={item.label === 'SKILL'}
        color={item.color} 
      />
    {/each}
  </nav>
</div>

<style>
  .app-container {
    width: 100vw;
    height: 100vh;
    position: relative;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    overflow: hidden;
  }

  .character-wrapper {
    position: absolute;
    left: 0;
    top: 0;
    height: 100vh;
    width: 100vw;
    z-index: 0;
    pointer-events: none;
  }

  .character-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }

  .menu-container {
    z-index: 5;
    display: flex;
    flex-direction: column;
    margin-right: 5vw;
    margin-top: 5vh;
    transform: translateX(-370px);
  }

  @keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-30px) rotate(2deg); }
  }
</style>
