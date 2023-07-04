<template>
  <div id="wrapperr">
    <nav class="navbar is-info">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Commenting</strong>
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false"
           data-target="navbar-menu"></a>

      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <button @click="logout()" class="button is-danger">Log out</button>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>

            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>

<script>
import axios from 'axios'

export default {
  data() {
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            this.$store.commit('removeToken')

            this.$router.push('/log-in')
        },
    }
}
</script>