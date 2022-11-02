import Vue from 'vue';
import VueRouter from 'vue-router';
import Vehicle from '../views/Vehicle.vue';
import Catalog from '../views/Catalog.vue';
import Admin from '../views/Admin.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/catalog',
    name: 'Catalog',
    component: Catalog,
    alias: ['/home', '/'],
  },
  {
    path: '/vehicle/:id',
    name: 'Vehicle',
    component: Vehicle,
  },
  {
    path: '/admin',
    name: 'Administration',
    component: Admin,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
