<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <nav>
    <v-app-bar flat>
      <v-toolbar-title class="text-uppercase grey--text">
        <span class="font-weight-light">Vehicles</span>
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
                    v-for="(item, i) in links"
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

      <v-btn color="grey" text class="ml-2">
        <span>Sign Out</span>
        <v-icon right>mdi-logout-variant</v-icon>
      </v-btn>

    </v-app-bar>
  </nav>
</template>

<script>
export default {
    data(){
        return {
            selectedPage: 0,
            links: [
                {icon: 'mdi-car-search', text: 'Catalog', route: '/catalog'},
                {icon: 'mdi-account-supervisor', text: 'Admin', route: '/admin'},
            ]
        }
    }
}
</script>