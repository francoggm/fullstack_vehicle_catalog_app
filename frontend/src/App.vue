<template>
  <v-app class="grey lighten-4">
    <Navbar/>
    <v-content class="pa-10">
      <router-view/>
    </v-content>

  </v-app>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',

  data: () => ({
    //
  }),
  created(){
    document.title = "Catalog"
  },
  components: {
    Navbar
  }
};
</script>
