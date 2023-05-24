<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
    <nav class="navbar navbar-expand navbar-dark around">
        <a class="navbar-brand" href="#"><img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" /></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
      
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

  <footer class="around text-center py-3 ">
      <p>Adresse : 123 Rue Principale, Champs-sur-Marne, France</p>
      <p>Téléphone : +33 12 34 56 78</p>
      <p>Email : quizpro@gmail.com</p>
  </footer>
</template>

<style scoped>

:root{
  background-color: #f1f1f1;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}



#app{
    display: initial;
    margin:0;
  }

  body{
    display: initial;
    
  }


.logo {
  display: block;
  margin-left: 5px;
}

main{
  flex:1;
}

.around{
  background-color: #08489B;
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

  

  background-color: #ADD4F3;
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
