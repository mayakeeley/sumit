<template>
  <div class="font-avenir antialiased text-center">
    <nav class="flex justify-center p-7">
      <router-link :to="{ name: 'Home' }">Home</router-link>
      <template v-if="isLoggedIn">
        |
        <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
        |
        <router-link :to="{ name: 'Cashflow' }">Cashflow</router-link>
        |
        <span id="logout" @click="logout()">Logout</span>
      </template>
      <template v-else>
        |
        <router-link to="/login" data-cy="login">Login</router-link>
        |
        <router-link to="/signup">Signup</router-link>
      </template>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'App',
  setup() {
    const store = useStore()
    const router = useRouter()

    async function logout() {
      await store.dispatch('setUser', null)
      router.push({ name: 'Home' })
    }

    return {
      logout,
      isLoggedIn: computed(() => store.getters.isLoggedIn),
    }
  },
}
</script>
