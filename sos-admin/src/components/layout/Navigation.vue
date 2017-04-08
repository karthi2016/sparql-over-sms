<template>
  <nav class="navbar navbar-toggleable-md navbar-inverse bg-inverse">
    <a class="navbar-brand" href="#/">SPARQL over SMS</a>
    <div class="navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="nav-link" to="/agents">Agents</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/messages">Messages</router-link>
        </li>
      </ul>
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
