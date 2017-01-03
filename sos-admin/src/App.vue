<template>
  <div id="app">
    <Navigation></Navigation>

    <router-view></router-view>
  </div>
</template>

<script>
import Navigation from './components/layout/Navigation';

export default {
  name: 'app',
  components: {
    Navigation,
  },
};
</script>

<style lang="scss">
#app {
  
}
</style>
