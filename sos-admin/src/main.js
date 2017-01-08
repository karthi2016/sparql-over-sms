import Vue from 'vue';
import VueRouter from 'vue-router';
import VueCodeMirror from 'vue-codemirror';
import VueResource from 'vue-resource';
import App from './App';

Vue.use(VueRouter);
Vue.use(VueCodeMirror);
Vue.use(VueResource);

const Query = require('./views/Query');
const Agents = require('./views/Agents');
const Messages = require('./views/Messages');

const router = new VueRouter({
  routes: [
    { path: '/', component: Query },
    { path: '/agents', component: Agents },
    { path: '/messages', component: Messages },
  ],
});

const app = new Vue({
  router,
  template: '<App />',
  components: { App },
});

app.$mount('#appframe');
