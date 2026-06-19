<template>
  <div class="min-h-screen">
    <Navbar />
    <LoginForm />
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import Navbar from '/src/components/Navbar.vue'
  import LoginForm from '/src/components/LoginForm.vue'

  onMounted(() => window.scroll(0, 0))
</script>
