<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template> 
  <nav class="navbar around justify-content-between">
    <div class="title">
    <RouterLink to="/home">
      <img alt="Vue logo" class="logo d-inline-block align-center" src="@/assets/trueLogo.svg" width="50" height="50" />
    </RouterLink>
    <span class="navbar-brand mb-0 h1">BrainPulse</span>         
    </div>
    <RouterLink to="/admin">Admin</RouterLink>
  </nav>
    
  <main class="container mt-4 mb-4 p-4  rounded shadow ">
    <RouterView />
  </main>

  <footer class="around text-center py-3 ">
      <p>Adresse : 123 Rue Principale, Champs-sur-Marne, France</p>
      <p>Téléphone : +33 6 12 34 56 78</p>
      <p>Email : quizpro@gmail.com</p>
  </footer>
</template>

<style scoped>

#app{
  display: initial;
  margin:0;
}


.logo {
  display: block;
  margin-left: 5px;
}


nav{
  background-color: #08489B;
}

footer{
  background-color: #042148;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}



.container{
  background-color: #ADD4F3;
  color: black;
  margin-bottom: 5px;
  align-content: normal;
}

</style>
