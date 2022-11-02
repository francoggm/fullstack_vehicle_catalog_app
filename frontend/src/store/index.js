import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    ip: 'http://127.0.0.1',
    port: '5000',
    selectedPage: 0,
    token: '',
    userAdmin: false,
    alert: false,
    alertText: '',
    alertColor: "red"
  },
  getters: {
  },
  mutations: {
    CHANGE_TOKEN(state, payload){
      if (payload.length == 0)
        state.userAdmin = false;
      state.token = payload;
    },
    CHANGE_ADMIN(state, payload){
      state.userAdmin = payload;
    },
    CHANGE_ALERT(state, payload){
      state.alert = payload;
    },
    CHANGE_ALERT_COLOR(state, payload){
      state.alertColor = payload;
    },
    CHANGE_ALERT_TEXT(state, payload){
      state.alertText = payload;
    },
    CHANGE_SELECTED_PAGE(state, payload){
      state.selectedPage = payload;
    }
  },
  actions: {
    setToken(context, payload){
      context.commit('CHANGE_TOKEN', payload)
    },
    setAdmin(context, payload){
      context.commit('CHANGE_ADMIN', payload)
    },
    setAlert(context, payload){
      context.commit('CHANGE_ALERT', payload)
    },
    setAlertText(context, payload){
      context.commit('CHANGE_ALERT_TEXT', payload)
    },
    setAlertColor(context, payload){
      context.commit('CHANGE_ALERT_COLOR', payload)
    },
    setSelectedPage(context, payload){
      context.commit('CHANGE_SELECTED_PAGE', payload)
    }

  },
  modules: {
  },
});
