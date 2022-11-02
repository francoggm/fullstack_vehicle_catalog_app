import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    ip: 'http://127.0.0.1',
    port: '5000',
    token: '',
    userAdmin: false
  },
  getters: {
  },
  mutations: {
    CHANGE_TOKEN(state, payload){
      if (payload.length == 0)
        state.userAdmin = false;
      state.token = payload
    },
    CHANGE_ADMIN(state, payload){
      state.userAdmin = payload
    }
  },
  actions: {
    setToken(context, payload){
      context.commit('CHANGE_TOKEN', payload)
    },
    setAdmin(context, payload){
      context.commit('CHANGE_ADMIN', payload)
    }
  },
  modules: {
  },
});
