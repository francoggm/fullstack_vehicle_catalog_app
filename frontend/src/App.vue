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
<style>
.v-application--wrap{
  min-height: 90vh !important;
}
</style>
