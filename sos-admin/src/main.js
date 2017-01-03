import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App';

Vue.use(VueRouter);

const Home = { template: '<div>home</div>' };
const Foo = { template: '<div>foo</div>' };
const Bar = { template: '<div>bar</div>' };

const router = new VueRouter({
  routes: [
    { path: '/', component: Home },
    { path: '/foo', component: Foo },
    { path: '/bar', component: Bar },
  ],
});

const app = new Vue({
  router,
  template: '<App />',
  components: { App },
});

app.$mount('#wrapper');
