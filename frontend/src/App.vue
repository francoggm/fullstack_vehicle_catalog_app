<template>
  <v-app class="grey lighten-4">
    <Navbar/>
    <v-content class="pl-10 pr-10 pt-10">
      <router-view/>
    </v-content>

  </v-app>
</template>

<script>
import Navbar from './components/Navbar.vue'
import axios from 'axios'

export default {
  name: 'App',

  data: () => ({
    //
  }),
  methods: {
    refreshToken() {
      const self = this;
      this.interval = setInterval(function(){
        if (self.$store.state.token.length > 0){
          const path = self.$store.state.ip + ":" + self.$store.state.port + "/auth/refresh_token"
          axios
          .get(path, {headers: {'x-access-token': self.$store.state.token}})
          .then((res) => {
            console.log(res)
            self.$store.dispatch("setToken", res['data']['token'])
          })
          .catch((err) => {
            console.log(err)
            const error = err['response']['data']['message']
            if (error != ''){
              self.$store.dispatch("setToken", '')
              self.$store.dispatch("setAdmin", false)
              self.$router.push('/login')
  
              self.$store.dispatch("setAlert", true)
              self.$store.dispatch("setAlertText", "Error em atualizar token, logue novamente!")
              self.$store.dispatch("setAlertColor", "red")
            } else {
              console.log("Muito cedo para atualizar token!")
            }
          })
        }
      }, 300000)
    }
  },
  created(){
    document.title = "Catalog"
    this.refreshToken()
  },
  components: {
    Navbar
  }
};
</script>
<style>
.v-application--wrap{
  min-height: 90vh !important;
}
</style>
