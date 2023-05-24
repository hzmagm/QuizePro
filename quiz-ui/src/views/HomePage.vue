<template>
  <div class="home">
    <h1>Bienvenue</h1>

    <p>Viens tester ta culture générale en jouant à notre quiz!</p>


    
    <HighScoresDisplay/>
    <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  </div>
</template>

<script>
import HighScoresDisplay from "../components/HighScoresDisplay.vue";

export default {
  name: "HomePage",
  data() {
    return {
      
    };
  },
  components: {  
    HighScoresDisplay
  },
  async created() {
    console.log("Composant Home page 'created'");
    
  }
};
</script>

<style></style> 