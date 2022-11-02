import Vue from 'vue';
import VueRouter from 'vue-router';
import Catalog from '../views/Catalog.vue';
import Admin from '../views/Admin.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/catalog',
    name: 'Catalog',
    component: Catalog,
    alias: ['/home', '/'],
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
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
