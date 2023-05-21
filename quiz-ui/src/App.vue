<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
        <a class="navbar-brand" href="#"><img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" /></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <span class="navbar-brand mb-0 h1" style="left: 10px;">QuizProNavbar</span>
      
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <RouterLink to="/home">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/admin">Admin</RouterLink>
            </li>          
          </ul>         
        </div>
      </nav>
    </div>
  </header>

  <main class="container mt-4 mb-4 p-4  rounded shadow">

    <RouterView />

  </main>

  <footer class="bg-dark text-center py-3">
      <p>Adresse : 123 Rue Principale, Ville, Pays</p>
      <p>Téléphone : +1 234 567 890</p>
      <p>Email : contact@example.com</p>
  </footer>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

RouterView{
  background-color: aqua;
}

#app{
    display: initial;
    margin:0;
  }

  body{
    display: initial;
    background-color: rgb(190,120,120);
    
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

.container h1{
  color: rgb(140,140,140);
}

.container{

  

  background-color: rgb(84,84,84);
  color: black;
  margin-bottom: 5px;
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
