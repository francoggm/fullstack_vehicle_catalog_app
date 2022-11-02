<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <nav>
    <v-app-bar flat>
      <v-toolbar-title class="text-uppercase grey--text" style="cursor: pointer" @click="$router.push('/catalog')">
        <span  class="font-weight-light">Vehicles</span>
        <span> Catalog</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu flat offset-y>
        <template v-slot:activator="{on, attrs}">
            <v-btn color="grey" text v-bind="attrs" v-on="on">
                <v-icon left>mdi-menu</v-icon>
                <span>Menu</span>
            </v-btn>
        </template>
        <v-list>
            <v-list-item-group
                v-model="selectedPage"
                color="primary"
            >
                <v-list-item
                    dense
                    v-for="(item, i) in linksList"
                    :key="i"
                    @click="$router.push(item.route)"
                >
                    <v-list-item-icon>
                        <v-icon>{{item.icon}}</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title v-text="item.text"></v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-list>
      </v-menu>

      <v-btn v-if="this.$store.state.token.length > 0" color="red" text class="ml-2" @click="logoutUser" to="/login">
        <span>Sign Out</span>
        <v-icon right>mdi-logout-variant</v-icon>
      </v-btn>
      
      <v-btn v-if="this.$store.state.token.length == 0" color="green" text class="ml-2" to="/login">
        <span>Login</span>
        <v-icon right>mdi-login</v-icon>
      </v-btn>

    </v-app-bar>
  </nav>
</template>

<script>
export default {
    data(){
        return {
            selectedPage: 0,
        }
    },
    computed: {
        linksList(){
            let links = [{icon: 'mdi-car-search', text: 'Catálogo', route: '/catalog'}]
            if (this.$store.state.token.length > 0){
                links.push({icon: 'mdi-account-supervisor', text: 'Admin', route: '/admin'})
            } else {
                links.push({icon: 'mdi-login', text: 'Login', route: '/login'})
                links.push({icon: 'mdi-account-plus-outline', text: 'Registro', route: '/register'})
            }
            return links  
        }
    },
    methods: {
        logoutUser(){
            this.$store.dispatch("setToken", '')
        }
    }
}
</script>