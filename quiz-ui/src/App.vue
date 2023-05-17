<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" />
        <span class="navbar-brand mb-0 h1" style="left: 10px;">QuizProNavbar</span>
      
        <div id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <RouterLink to="/home">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/score">Admin (temporariliy leads to Score)</RouterLink>
            </li>          
          </ul>         
        </div>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

RouterView{
  background-color: aqua;
}



.logo {
  display: block;
  margin-left: 5px;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
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

@media (min-width: 1024px) {
  header {
    /*display: flex;*/
    place-items: center;
    
  }


  header .wrapper {
    display: flex;
    place-items: space-between;
    flex-wrap: wrap;
  }

  
}
</style>
