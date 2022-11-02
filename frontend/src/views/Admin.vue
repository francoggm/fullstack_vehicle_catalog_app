<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <v-content v-if="this.$store.state.userAdmin">
        <v-layout align-center justify-center column>
            <v-card width="60%" class="pa-5 mb-12">
                <v-card-title class="justify-center">Usuários</v-card-title> 
                <v-simple-table>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left"><strong>Nome</strong></th>
                                <th class="text-left"><strong>Email</strong></th>
                                <th class="text-left"><strong>ID Público</strong></th>
                                <th class="text-left"><strong>Admin</strong></th>
                                <th class="text-left"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="user in users"
                                :key="user.public_id"
                            >
                                <td>{{user.name}}</td>
                                <td>{{user.email}}</td>
                                <td>{{user.public_id}}</td>
                                <td v-if="user.admin">
                                    Sim
                                </td>
                                <td v-else>
                                    Não
                                </td>
                                <td class="pb-3 pt-3">
                                    <v-dialog
                                        transition="dialog-bottom-transition"
                                        max-width="600"
                                        v-model="dialogPromote"
                                    >
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-btn class="mr-3" fab small color="grey darken-1" v-bind="attrs" v-on="on" dark v-if="!user.admin">
                                                <v-icon>mdi-shield-crown</v-icon>
                                            </v-btn>
                                        </template>
                                        <template v-slot:default="dialogPromote">
                                            <v-card>
                                                <v-toolbar
                                                dark
                                                >
                                                    Promover Usuário
                                                </v-toolbar>
                                                <v-card-text class="text-center" >
                                                    <div class="text-h6 mt-3 center">
                                                        Você tem certeza que deseja promover <strong>{{user.name}}</strong> para Administrador?
                                                    </div>
                                                </v-card-text>
                                                <v-card-actions class="justify-center">
                                                    <v-btn dark color="green lighten-1" class="mr-4" @click="promoteUser(user.public_id)">
                                                        Promover
                                                    </v-btn>
                                                    <v-btn dark color="grey lighten-1" @click="dialogPromote.value = false">Cancelar</v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </template>
                                    </v-dialog>
                                    <v-dialog
                                        transition="dialog-bottom-transition"
                                        max-width="600"
                                        v-model="dialogExclude"
                                    >
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-btn fab small color="red darken-2" dark v-bind="attrs" v-on="on">
                                                <v-icon>mdi-delete</v-icon>
                                            </v-btn>
                                        </template>
                                        <template v-slot:default="dialogExclude">
                                            <v-card>
                                                <v-toolbar
                                                dark
                                                >
                                                    Excluir Usuário
                                                </v-toolbar>
                                                <v-card-text class="text-center" >
                                                    <div class="text-h6 mt-3 center">
                                                        Você tem certeza que deseja excluir <strong>{{user.name}}</strong>?
                                                    </div>
                                                </v-card-text>
                                                <v-card-actions class="justify-center">
                                                    <v-btn dark color="red darken-2" class="mr-4" @click="excludeUser(user.public_id)">
                                                        Deletar
                                                    </v-btn>
                                                    <v-btn dark color="grey lighten-1" @click="dialogExclude.value = false">Cancelar</v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </template>
                                    </v-dialog>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>
            <v-card width="60%" class="pa-5 mb-12">
                <v-card-title class="justify-center">Veículos</v-card-title>
                <v-simple-table>
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="text-left"></th>
                                <th class="text-left"><strong>Nome</strong></th>
                                <th class="text-left"><strong>Marca</strong></th>
                                <th class="text-left"><strong>Modelo</strong></th>
                                <th class="text-left"><strong>Preço</strong></th>
                                <th class="text-left"><strong>Quilometragem</strong></th>
                                <th class="text-left"><strong>Registro</strong></th>
                                <th class="text-left"><strong>ID</strong></th>
                                <th class="text-left"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="vehicle in vehicles"
                                :key="vehicle.id"
                            >
                                <td>
                                    <v-list-item-avatar>
                                        <v-img src="../assets/novo-hb20-3.webp"></v-img>
                                    </v-list-item-avatar>
                                </td>
                                <td>{{vehicle.name}}</td>
                                <td>{{vehicle.brand}}</td>
                                <td>{{vehicle.model}}</td>
                                <td>{{vehicle.format_price}}</td>
                                <td>{{vehicle.format_mileage}}</td>
                                <td>{{vehicle.format_register_date}}</td>
                                <td>{{vehicle.id}}</td>
                                <td class="pb-3 pt-3">

                                    <v-dialog
                                        transition="dialog-bottom-transition"
                                        max-width="600"
                                    >
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-btn class="mr-3" fab small color="grey darken-1" dark v-bind="attrs" v-on="on">
                                                <v-icon>mdi-pencil</v-icon>
                                            </v-btn>
                                        </template>
                                        <template v-slot:default="dialogEditVehicle">
                                            <v-card class="pa-5">
                                                <v-card-title class="mb-3 justify-center">Editar Veículo</v-card-title>
                                                <v-card-text>
                                                    <v-row>
                                                        <v-col>
                                                            <v-file-input
                                                            solo
                                                            disabled
                                                            placeholder="Escolha uma Imagem"
                                                            prepend-icon="mdi-camera"
                                                            label="Avatar"
                                                            show-size
                                                            ></v-file-input>
                                                        </v-col>
                                                    </v-row>
                                                    <v-row>
                                                        <v-col>
                                                            <v-text-field
                                                                v-model="vehicle.name"
                                                                solo
                                                                placeholder="Nome"
                                                                hint="Nome"
                                                                persistent-hint
                                                                prepend-icon="mdi-car-select"
                                                            ></v-text-field>
                                                        </v-col>
                                                        <v-col>
                                                            <v-text-field
                                                                v-model="vehicle.brand"
                                                                solo
                                                                placeholder="Marca"
                                                                hint="Marca"
                                                                persistent-hint
                                                                prepend-icon="mdi-car-settings"
                                                            ></v-text-field>
                                                        </v-col>
                                                    </v-row>
                                                    <v-row>
                                                        <v-col>
                                                            <v-text-field
                                                                v-model="vehicle.model"
                                                                solo
                                                                placeholder="Modelo"
                                                                hint="Modelo"
                                                                persistent-hint
                                                                prepend-icon="mdi-car-clock"
                                                            >
                                                            </v-text-field>
                                                        </v-col>
                                                        <v-col> 
                                                            <v-text-field
                                                                v-model="vehicle.price"
                                                                solo
                                                                placeholder="Preço"
                                                                hint="Preço"
                                                                persistent-hint
                                                                prepend-icon="mdi-car-info"
                                                                type="number"
                                                            >
                                                            </v-text-field>
                                                        </v-col>
                                                        <v-col>
                                                            <v-text-field
                                                                v-model="vehicle.mileage"
                                                                solo
                                                                placeholder="Quilometragem"
                                                                hint="Quilometragem"
                                                                persistent-hint
                                                                type="number"
                                                                prepend-icon="mdi-car-speed-limiter"
                                                            >
                                                            </v-text-field>
                                                        </v-col>
                                                    </v-row>
                                                </v-card-text>
                                                <v-card-actions class="justify-end">
                                                    <v-btn class="mr-5" dark color="green lighten-1" @click="updateVehicle(vehicle)">
                                                        Salvar
                                                    </v-btn>
                                                    <v-btn dark color="grey lighten-1" @click="dialogEditVehicle.value = false">
                                                        Fechar
                                                    </v-btn>
                                                </v-card-actions>
                                            </v-card>
                                            
                                        </template>
                                    </v-dialog>

                                    <v-dialog
                                        transition="dialog-bottom-transition"
                                        max-width="600"
                                    >
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-btn fab small color="red darken-2" dark v-bind="attrs" v-on="on">
                                                <v-icon>mdi-delete</v-icon>
                                            </v-btn>
                                        </template>
                                        <template v-slot:default="dialogExcludeVehicle">
                                            <v-card>
                                                <v-toolbar
                                                dark
                                                >
                                                    Excluir Veículo
                                                </v-toolbar>
                                                <v-card-text class="text-center" >
                                                    <div class="text-h6 mt-3 center">
                                                        Você tem certeza que deseja excluir <strong>{{vehicle.brand}} - {{vehicle.name}}</strong>?
                                                    </div>
                                                </v-card-text>
                                                <v-card-actions class="justify-center">
                                                    <v-btn dark color="red darken-2" class="mr-4" @click="excludeVehicle(vehicle.id)">
                                                        Deletar
                                                    </v-btn>
                                                    <v-btn dark color="grey lighten-1" @click="dialogExcludeVehicle.value = false">
                                                        Cancelar
                                                    </v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </template>
                                    </v-dialog>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-card>
        </v-layout>
    </v-content>
</template>

<script>
import axios from 'axios'

export default {
    data: () => ({
        users: [],
        vehicles: [],
        dialogExclude: false,
        dialogPromote: false,
        dialogExcludeVehicle: false
    }),
    methods: {
        excludeUser(public_id){
            const config = {
                headers: {
                    'x-access-token': this.$store.state.token,
                }
            }
            const path = this.$store.state.ip + ":" + this.$store.state.port + "/user/" + public_id
            axios
            .delete(path, config)
            .then((res) => {
                this.dialogExclude = false;
                this.getUsers();
            })
            .catch((err) => {
                console.log(err)
                const error = err['response']['data']['message']
                if (error == "Invalid token"){
                    this.tokenExpired();
                }
            })
        },
        excludeVehicle(id){
            const config = {
                headers: {
                    'x-access-token': this.$store.state.token,
                }
            }
            const path = this.$store.state.ip + ":" + this.$store.state.port + "/vehicle/" + id
            axios
            .delete(path, config)
            .then((res) => {
                this.dialogExcludeVehicle = false;
                this.getVehicles();
            })
            .catch((err) => {
                console.log(err)
                const error = err['response']['data']['message']
                if (error == "Invalid token"){
                    this.tokenExpired();
                }
            })
        },
        updateVehicle(vehicle){
            const path = this.$store.state.ip + ":" + this.$store.state.port + "/vehicle/" + vehicle.id
            axios({
                method: "put",
                url: path,
                headers: {
                    'x-access-token': this.$store.state.token
                }
            })
        },
        promoteUser(public_id){
            console.log(public_id)
            const path = this.$store.state.ip + ":" + this.$store.state.port + "/user/" + public_id
            axios({
                method: "put",
                url: path,
                data: {},
                headers: {
                    'x-access-token': this.$store.state.token
                }
            })
            .then((res) => {
                console.log(res)
                this.dialogPromote = false;
                this.getUsers();
            })
            .catch((err) => {
                console.log(err)
                const error = err['response']['data']['message']
                if (error == "Invalid token"){
                    this.tokenExpired(); 
                }
            })
        },
        getUsers(){
            const path = this.$store.state.ip + ":" + this.$store.state.port + "/user"
            const config = {
                headers: {
                    'x-access-token': this.$store.state.token,
                }
            }
            axios
            .get(path, config)
            .then((res) => {
                this.users = res['data']['users']
            })
            .catch((err) => {
                console.log(err)
                const error = err['response']['data']['message']
                if (error == "Invalid token"){
                    this.tokenExpired();
                }
            })
        },
        getVehicles(){
            const path = this.$store.state.ip + ":" + this.$store.state.port + "/vehicle"
            axios
            .get(path)
            .then((res) => {
                this.vehicles = res.data['vehicles']
            })
            .catch((err) => {
                console.log(err)
            })
        },
        tokenExpired(){
            this.$store.dispatch("setToken", '')
            this.$store.dispatch("setAdmin", false)
            this.$router.push('/login')

            this.$store.dispatch("setAlert", true)
            this.$store.dispatch("setAlertText", "Token expirado favor logar novamente!")
            this.$store.dispatch("setAlertColor", "red")
        }
    },
    beforeMount(){
        this.$store.dispatch("setSelectedPage", 1)
        if (!this.$store.state.userAdmin){
            this.$router.push('/login')
            this.$store.dispatch("setAlert", true)
            this.$store.dispatch("setAlertText", "Você precisar ser Admin para acessar essa página!")
            this.$store.dispatch("setAlertColor", "red")
        }
        else {
            this.getUsers()
            this.getVehicles()
        }
    },
    updated(){
        if (this.users.length == 0)
            this.tokenExpired()
    }
}
</script>