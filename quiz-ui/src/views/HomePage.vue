<template>
  <div class="home text-center">
    <h1>Welcome</h1>

    <p>Test your general culture on our site! </p>

    <img src="@/assets/bigbrain.jpeg" height="300">
    
    <HighScoresDisplay/>
    <router-link to="/start-new-quiz-page" class="btn btn-custom">Start !</router-link>
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

<style>

.btn-custom{
  background-color: white;
  color: red;
}

</style> 