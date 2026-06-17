<template>
  <div class="min-h-screen">
    <Navbar />
    <Settings />
    <p>Howdy!</p>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import Navbar from '/src/components/Navbar.vue'
  import Settings from '/src/components/Settings.vue'
  
  onMounted(() => window.scroll(0, 0))
</script>
