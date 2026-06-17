<template>
  <div class="min-h-dvh flex flex-col text-base-content">
    <router-view v-slot="{ Component, route }">
      <transition name="page" mode="out-in">
        <component :is="Component" :key="route.fullPath" />
        <p>test</p>
      </transition>
    </router-view>
    <!--<Footer />
    <Settings />-->
  </div>
</template>

<script setup>
import { onBeforeMount } from 'vue'
import Footer from './components/Footer.vue'
import Settings from './components/Settings.vue'
import { useBinaryThemeManager } from './model/theme'
import router from './router'

const themeMgr = useBinaryThemeManager()
onBeforeMount(() => {
  themeMgr.setLightAlias('downtify-light')
  themeMgr.setDarkAlias('downtify-dark')
})

console.log("This page has the thing!")
if(localStorage.getItem('jf_access_token') == null) {
  router.push({ name: 'Login' })
}
</script>

<style>
.page-enter-active,
.page-leave-active {
  transition:
    opacity 0.25s ease,
    transform 0.25s ease;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  transform: translateY(8px);
}
</style>
