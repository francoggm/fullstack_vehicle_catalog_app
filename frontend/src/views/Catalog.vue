<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <v-app>
        <v-container fluid grid-list-xl>
            <v-row>
                <v-col>
                    <v-select @change="changeFilter" :items="brandItems" v-model="selectedBrand" solo persistent-hint hint="Marca"></v-select>
                </v-col>
                <v-col>
                    <v-select @change="changeFilter" :items="modelItems" v-model="selectedModel" solo persistent-hint hint="Modelo"></v-select>
                </v-col>
            </v-row>
            <v-row class="mb-3">
                <v-col>
                    <p class="text-caption text-center">{{formatMileage(mileageRange[0])}} - {{formatMileage(mileageRange[1])}}</p>
                    <v-range-slider @change="changeFilter" label="Quilometragem" :min="rangeMileage[0]" :max="rangeMileage[1]" v-model="mileageRange">
                    </v-range-slider>
                </v-col>
                <v-col></v-col>
                <v-col></v-col>
            </v-row>
            <div class="mb-5">
                <v-menu offset-y rounded="lg">
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                            v-bind="attrs"
                            v-on="on"
                            text
                        >
                            <v-icon left>mdi-order-bool-descending-variant</v-icon>
                            <span>Ordenamento</span>
                        </v-btn>    
                    </template>
                    <v-list>
                        <v-list-item-group
                            v-model="selectedOrder"
                            @change="changeOrder"
                        >
                            <v-list-item
                                v-for="(item, index) in orderItems"
                                :key="index"
                            >
                                <v-list-item-title>{{ item }}</v-list-item-title>
                            </v-list-item>
                        </v-list-item-group>
                    </v-list>
                </v-menu>
            </div>
            <v-layout wrap justify-start class="ml-16">
                <v-flex v-for="vehicle in vehicles" :key="vehicle.id" >
                    <v-card color="gray" width="350px">
                        <v-img
                            height="250"
                            src="../assets/novo-hb20-3.webp"
                        ></v-img>
                        <v-card-title>
                            {{vehicle.brand}} {{vehicle.name}}
                        </v-card-title>
                        <v-card-text class="text--primary">
                            {{vehicle.model}} - {{formatMileage(vehicle.mileage)}}
                        </v-card-text>
                        <v-card-title>
                            {{formatPrice(vehicle.price)}}
                        </v-card-title>
                    </v-card>
                </v-flex>
                <!-- <v-flex v-for="vehicle in vehicles" :key="vehicle" class="flex-empty">
                    <v-card width="350px"></v-card>
                </v-flex> -->
            </v-layout>
        </v-container>
    </v-app>
</template>

<script>
import axios from 'axios'

export default {
    data: () => ({
        vehicles: [],
        vehiclesPlaceholder: [],
        brandItems: [],
        modelItems: [],
        mileageRange: [],
        orderItems: ["Menor Preço", "Maior Preço", "Mais Antigo", "Mais Novo"],
        selectedBrand: "Todas",
        selectedModel: "Todos",
        selectedOrder: 1
    }),
    computed: {
        rangeMileage() {
            if (this.vehiclesPlaceholder.length > 0) {
                let values = [];
                this.vehiclesPlaceholder.forEach((item) => {
                    values.push(item.mileage)
                })
                return [Math.min.apply(Math, values), Math.max.apply(Math, values)]
            }
            return 0
        },
    },
    methods: {
        formatMileage(mileage){
            return mileage.toLocaleString(
                undefined
            ).replace(',', '.') + ' km'
        },
        formatPrice(price){
            return 'R$ ' + price.toLocaleString(
                undefined
            ).replace(',', '.')
        },
        brand(){
            if (this.vehicles.length > 0){
                let values = [];
                values.push("Todas");
                this.vehicles.forEach((item) => {
                    values.push(item.brand)
                })
                return values;
            }
            return []
        },
        model(){
            if (this.vehicles.length > 0){
                let values = [];
                values.push("Todos");
                this.vehicles.forEach((item) => {
                    values.push(item.model)
                })
                return values;
            }
            return []
        },
        changeOrder(){
            const choose = this.orderItems[this.selectedOrder]
            let sortedArray = [];
            if (choose == 'Maior Preço'){
                sortedArray = this.vehiclesPlaceholder.sort(
                    (p1, p2) => (p1.price < p2.price) ? 1 : (p1.price > p2.price) ? -1 : 0
                );
            }
            else if(choose == 'Menor Preço'){
                sortedArray = this.vehiclesPlaceholder.sort(
                    (p1, p2) => (p1.price > p2.price) ? 1 : (p1.price < p2.price) ? -1 : 0
                )
            }
            else if (choose == 'Mais Antigo'){
                sortedArray = this.vehiclesPlaceholder.sort(
                    (p1, p2) => (parseInt(p1.model) > parseInt(p2.model)) ? 1 : (parseInt(p1.model) < parseInt(p2.model)) ? -1 : 0
                )
            }
            else if (choose == 'Mais Novo'){
                sortedArray = this.vehiclesPlaceholder.sort(
                    (p1, p2) => (parseInt(p1.model) < parseInt(p2.model)) ? 1 : (parseInt(p1.model) > parseInt(p2.model)) ? -1 : 0
                )
            }
            this.vehicles = sortedArray
        },
        changeFilter(){
            let filterArray = [];
            for (const i in this.vehiclesPlaceholder){
                let vehicle = this.vehiclesPlaceholder[i]

                if (this.selectedModel != "Todos" && this.selectedModel != vehicle.model){
                    continue;
                }
                if(this.selectedBrand != "Todas" && this.selectedBrand != vehicle.brand){
                    continue;
                }
                if (!(this.mileageRange[0] <= vehicle.mileage && this.mileageRange[1] >= vehicle.mileage)){
                    continue;
                }
                filterArray.push(vehicle)
            }
            this.vehicles = filterArray;
        }
    },
    created(){
        const path = this.$store.state.ip + ":" + this.$store.state.port + "/vehicle"
        axios
        .get(path)
        .then((res) => {
            this.vehicles = res.data['vehicles']
            if (this.vehicles){
                this.vehiclesPlaceholder = this.vehicles;
                this.mileageRange = this.rangeMileage
                this.brandItems = this.brand();
                this.modelItems = this.model();
            }
        })
        .catch((err) => {
            console.log(err)
        })
        
    },
    updated(){
        console.log(this.vehiclesPlaceholder)
    }
}
</script>

<style scoped>
    .flex {
        flex-grow: 0;
    }
    .card-items:first-child {
        margin-left: 0px !important;
    }
    .flex-empty {
        height: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
</style>