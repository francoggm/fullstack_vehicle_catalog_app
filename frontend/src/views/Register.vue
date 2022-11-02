<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <v-app>
        <v-content >
            <v-container fluid fill-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4>
                        <v-card dar class="elevation-12">
                            <v-toolbar dark>
                                <v-icon left>mdi-account-plus-outline</v-icon>
                                <v-toolbar-title>Registro</v-toolbar-title>
                            </v-toolbar>
                            <v-card-subtitle class="text-center mb-3">
                                Registre-se para Utilizar as Funções
                            </v-card-subtitle>
                            <v-card-text>
                                <v-form v-model="valid">
                                    <v-text-field
                                        prepend-icon="mdi-account"
                                        v-model="userName"
                                        name="user"
                                        label="Nome"
                                        type="text"
                                        required
                                        :rules="nameRules"
                                    ></v-text-field>
                                    <v-text-field
                                        prepend-icon="mdi-email"
                                        v-model="userEmail"
                                        name="email"
                                        label="Email"
                                        type="email"
                                        required
                                        :rules="emailRules"
                                    ></v-text-field>
                                    <v-text-field
                                        name="password"
                                        prepend-icon="mdi-lock"
                                        v-model="userPassword"
                                        label="Password"
                                        type="password"
                                        class="mb-5"
                                        required
                                        :rules="[passwordRequired, passwordLength, passwordMatchs]"
                                    >
                                    </v-text-field>
                                    <v-text-field
                                        name="password"
                                        prepend-icon="mdi-lock"
                                        v-model="userPassword1"
                                        label="Repeat Password"
                                        type="password"
                                        class="mb-5"
                                        required
                                        :rules="[passwordRequired, passwordLength, passwordMatchs]"
                                    >
                                    </v-text-field>
                                    <v-alert
                                        v-model="alert"
                                        dismissible
                                        color="red"
                                        border="left"
                                        elevation="2"
                                        colored-border
                                        icon="mdi-alert-circle"
                                        >
                                        {{alertText}}
                                    </v-alert>
                                    <v-card-actions>
                                        <v-btn block depressed :dark="valid" :disabled="!valid" @click="registerUser">Registrar</v-btn>
                                    </v-card-actions>
                                </v-form>
                            </v-card-text>
                        </v-card>
                        <div style="display: flex;" class="mt-5 login">
                            <span class="text-overline">Já possui uma conta?</span>
                            <v-btn class="ml-5" dark to="/login">
                                Login
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
        userName: '',
        userEmail: '',
        userPassword: '',
        userPassword1: '',
        valid: false,
        alert: false,
        alertText: '',
        nameRules: [
            v => !!v || "Nome necessário!",
            v => v.length >= 3 || "Nome muito curto!"
        ],
        emailRules: [
            v => !!v || "Email necessário!",
            v => /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'Email necessário!',
        ],
        // passwordRules: [
        //     v => !!v || "Senha necessária!"
        // ]
    }),
    computed: {
        passwordMatchs() {
            return this.userPassword == this.userPassword1 ? true : "Senhas não correspondem!";
        },
    },
    methods: {
        passwordRequired(value){
            if(value)
                return true;
            return "Senha necessária";
        },
        passwordLength(value){
            if(value.length >= 6)
                return true;
            return "Senha deve ter no mínimo 6 caracteres";
        },
        registerUser(){
            if (this.valid){
                const path = this.$store.state.ip + ":" + this.$store.state.port + "/auth/register"
                axios
                .post(path, {
                    name: this.userName,
                    email: this.userEmail,
                    password: this.userPassword
                })
                .then((res) => {
                    let response = res['data']['message']
                    if (response == "User has been registered"){
                        this.$router.push("/login")
                    }
                })
                .catch((err) => {
                    let error = err.response['data']['message']
                    if (error == "Error creating new user, missing informations"){
                        this.alert = true;
                        this.alertText = "Informações inválidas";
                    }
                    else {
                        this.alert = true;
                        this.alertText = "Erro no registro, tente novamente!";
                    }
                })
            }
        }
    },
    created(){
        this.$store.dispatch("setSelectedPage", 2)
    }
}
</script>

<style scoped>
.login {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>