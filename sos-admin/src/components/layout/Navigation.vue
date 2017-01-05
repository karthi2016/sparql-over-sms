<template>
  <nav class="navbar navbar-dark navbar-fixed-top bg-inverse">
    <a class="navbar-brand" href="#">SPARQL over SMS</a>
    <div id="navbar">
      <nav class="nav navbar-nav float-xs-left">
        <router-link class="nav-item nav-link" to="/contacts">Contacts</router-link>
        <router-link class="nav-item nav-link" to="/messages">Messages</router-link>
        <router-link class="nav-item nav-link" to="/query">Query</router-link>
      </nav>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'navigation',
};
</script>

<style lang="scss">
  .bg-inverse {
    background-color: #263238 !important;
  }
</style>
