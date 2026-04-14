<script>
  import { onMount } from 'svelte';
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

  onMount(() => {
    // Native JS Audio API for persistent background music
    const audioUrl = import.meta.env.BASE_URL + "music.mp3";
    const bgm = new Audio(audioUrl);
    bgm.loop = true;
    bgm.volume = 0.5; // Set to 50% so it's not deafening

    // Attempt to play immediately (sometimes works if domain is trusted)
    bgm.play().catch(() => {});

    // Auto-play workaround: play on valid user interactions
    let hasInteracted = false;
    const handleInteraction = () => {
      if (!hasInteracted) {
        bgm.play().then(() => {
          hasInteracted = true;
          // Playback started successfully, remove listeners
          window.removeEventListener('click', handleInteraction);
          window.removeEventListener('keydown', handleInteraction);
          window.removeEventListener('touchstart', handleInteraction);
        }).catch(() => {
          // Playback failed, wait for next user action
        });
      }
    };

    window.addEventListener('click', handleInteraction);
    window.addEventListener('keydown', handleInteraction);
    window.addEventListener('touchstart', handleInteraction);

    return () => {
      bgm.pause();
      window.removeEventListener('click', handleInteraction);
      window.removeEventListener('keydown', handleInteraction);
      window.removeEventListener('touchstart', handleInteraction);
    };
  });
</script>

<div class="app-container">
  <!-- Dynamic Background Stairs removed as requested -->

  <!-- Water reflection overlay pattern -->
  <div class="bg-layer"></div>

  <!-- Main character image/video -->
  <div class="character-wrapper">
    <video src="{import.meta.env.BASE_URL}background-real.mp4" autoplay loop muted playsinline class="character-image"></video>
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
    transform: translateX(-19vw); /* Replaced -370px with vw for consistent relative layout across display sizes */
  }

  @keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-30px) rotate(2deg); }
  }
</style>
