<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <v-app>
        <v-content v-if="this.$store.state.userAdmin">
            oi
        </v-content>
    </v-app>
</template>

<script>
export default {
    beforeMount(){
        if (!this.$store.state.userAdmin)
            this.$router.push('/login')
    }
}
</script>