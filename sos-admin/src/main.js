import Vue from 'vue';
import VueRouter from 'vue-router';
import VueCodeMirror from 'vue-codemirror';
import App from './App';

Vue.use(VueRouter);
Vue.use(VueCodeMirror);

const Home = require('./views/Home');
const Contacts = require('./views/Contacts');
const Messages = require('./views/Messages');
const Query = require('./views/Query');

const router = new VueRouter({
  routes: [
    { path: '/', component: Home },
    { path: '/contacts', component: Contacts },
    { path: '/messages', component: Messages },
    { path: '/query', component: Query },
  ],
});

const app = new Vue({
  router,
  template: '<App />',
  components: { App },
});

app.$mount('#appframe');
