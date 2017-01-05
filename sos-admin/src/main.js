import Vue from 'vue';
import VueRouter from 'vue-router';
import BootstrapVue from 'bootstrap-vue';
import App from './App';

Vue.use(VueRouter);
Vue.use(BootstrapVue);

const Home = require('./views/Home');
const Contacts = require('./views/Contacts');
const Messages = require('./views/Messages');

const router = new VueRouter({
  routes: [
    { path: '/', component: Home },
    { path: '/contacts', component: Contacts },
    { path: '/messages', component: Messages },
  ],
});

const app = new Vue({
  router,
  template: '<App />',
  components: { App },
});

app.$mount('#appframe');
