<template>
  <div id="app">
    <Navigation></Navigation>

    <div id="wrapper" class="container-fluid">
      <router-view></router-view>
    </div>
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

<style lang="css">
  @import '../node_modules/bootstrap/dist/css/bootstrap.css';

  #wrapper {
    margin-top: 1rem;
  }
</style>
