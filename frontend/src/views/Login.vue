<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <v-app>
        <v-content >
            <v-container fluid fill-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4>
                        <v-card dar class="elevation-12">
                            <v-toolbar dark>
                                <v-icon left>mdi-login</v-icon>
                                <v-toolbar-title>Login</v-toolbar-title>
                            </v-toolbar>
                            <v-card-subtitle class="text-center mb-3">
                                Logue para Utilizar as Funções
                            </v-card-subtitle>
                            <v-card-text>
                                <v-form v-model="valid">
                                    <v-text-field
                                        :disabled="disabledButtons"
                                        prepend-icon="mdi-email"
                                        v-model="userEmail"
                                        name="login"
                                        label="Email"
                                        type="email"
                                        required
                                        :rules="emailRules"
                                    ></v-text-field>
                                    <v-text-field
                                        :disabled="disabledButtons"
                                        name="password"
                                        prepend-icon="mdi-lock"
                                        v-model="userPassword"
                                        label="Password"
                                        type="password"
                                        class="mb-5"
                                        required
                                        :rules="passwordRules"
                                    >
                                    </v-text-field>
                                    <v-alert
                                        v-model="alert"
                                        dismissible
                                        :color=alertColor
                                        border="left"
                                        elevation="2"
                                        colored-border
                                        :icon=alertIcon
                                        >
                                        {{alertText}}
                                    </v-alert>
                                    <v-card-actions>
                                        <v-btn block depressed :dark="valid" :disabled="!valid" @click="loginUser">Login</v-btn>
                                    </v-card-actions>
                                </v-form>
                            </v-card-text>
                        </v-card>
                        
                        <div style="display: flex;" class="mt-5 register">
                            <span class="text-overline">Não possui uma conta?</span>
                            <v-btn class="ml-5" dark to="/register">
                                Registrar
                            </v-btn>
                        </div>

                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
import axios from 'axios'

export default {
    data: () => ({
        userEmail: '',
        userPassword: '',
        alert: false,
        alertText: '',
        alertColor: 'red',
        alertIcon: 'mdi-alert-circle',
        valid: false,
        emailRules: [
            v => !!v || "Email necessário!",
            v => /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'Email necessário!',
        ],
        passwordRules: [
            v => !!v || "Senha necessária!"
        ]
    }),
    computed: {
        disabledButtons(){
            if (this.$store.state.token.length == 0)
                return false;
            return true;
        }
    },
    methods: {
        loginUser(){
            if (this.valid){
                const path = this.$store.state.ip + ":" + this.$store.state.port + "/auth/login"
                axios
                .post(path, {
                    email: this.userEmail,
                    password: this.userPassword
                })
                .then((res) => {
                    this.alert = true;
                    this.alertColor = "green";
                    this.alertIcon = "mdi-check-circle";
                    this.alertText = "Logado com sucesso!"

                    const token = res['data']['token']
                    const admin = res['data']['admin']
                    
                    this.$store.dispatch("setToken", token)
                    this.$store.dispatch("setAdmin", admin)
                    
                })
                .catch((err) => {
                    let error = err.response['data']['message']
                    this.alert = true;
                    this.alertColor = "red";
                    this.alertIcon = "mdi-alert-circle";

                    if (error == "Error logging, wrong password!"){
                        this.alertText = "Senha errada!";
                    }
                    else if(error == "Error logging, email not found!"){ 
                        this.alertText = "Usuário não encontrado!";
                    }
                    else {
                        this.alertText = "Erro no login, tente novamente!";
                    }
                })
            }
        }
    },
    created(){
        this.$store.dispatch("setSelectedPage", 1)
    }
}
</script>

<style scoped>
    .form-login{
        max-width: 500px;
    }
    .register {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>