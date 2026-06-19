<template>
  <section class="relative flex flex-col min-h-[calc(100dvh-4rem)] items-center justify-center px-6 overflow-hidden">
    <h1 class="text-balance text-5xl sm:text-6xl font-bold tracking-tight">
      Jellyfin Login
    </h1>
    <form
      class="relative w-full max-w-2xl animate-slide-up space-y-3 mt-5"
      @submit.prevent="submitForm"
    >
      <label
        class="block text-xs font-semibold uppercase tracking-wider text-base-content/50 mt-4"
        >
        Username
      </label>
      <input
        type="text"
        :placeholder="Username"
        :class="['input-modern', compact ? 'h-11 text-sm' : 'h-14 text-base']"
        v-model.trim="formData.username"
        autocomplete="username"
        required
      />
      <label
        class="block text-xs font-semibold uppercase tracking-wider text-base-content/50"
        >
        Password
      </label>
      <input
        type="password"
        :placeholder="Password"
        :class="['input-modern', compact ? 'h-11 text-sm' : 'h-14 text-base']"
        v-model.trim="formData.password"
        autocomplete="current-password"
        required
      />
      <button
        class="btn btn-primary btn-sm h-10 px-6 rounded-full"
        type="submit"
      >
        Login
      </button>
    </form>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import API from '/src/model/api'
import router from '/src/router'

const formData = ref({
  username: '',
  password: ''
})

const access_token = localStorage.getItem('jf_access_token');
if (access_token) {
  router.push({ name: 'Home' })
}

function submitForm() {
  try {
    API.authenticateLogin(
      formData.value.username,
      formData.value.password,
    ).then((res) => {
      localStorage.setItem('jf_access_token', res.data.access_token);
      localStorage.setItem('user_id', res.data.user_id);
      router.push({ name: 'Home' });
    });
  } catch (error) {
    console.error(error.response?.data);  // shows FastAPI 422 detail
  }
}
</script>