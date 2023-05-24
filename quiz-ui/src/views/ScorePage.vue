<template>
  <div class="Score text-center">
        <h1>Score: {{ score }}</h1>
        <p v-if= "score>8">Bien joué champion(ne), vérifie si tu as ta place parmis les plus grands!</p>
        <p v-if= "score<5">Aïe, continue l'école!</p>
        <p v-if= "score<=8 && score>=5">Pas mal!</p>

        <HighScoresDisplay/>
  </div>
  <router-link to="/home">Retour</router-link>
</template>

<script>
import participationStorageService from "../services/ParticipationStorageService.js";
import HighScoresDisplay from "../components/HighScoresDisplay.vue";

export default {
  name: "ScorePage",
  data() {
    return {
      score:0
    };
  },
  components: {  
    HighScoresDisplay
  },
  async created() {
    console.log("Composant Home page 'created'");
    try{
      this.score=participationStorageService.getParticipationScore();
      console.log(this.score);
    }
    catch(error){
      console.log(error);
    }
  }
};
</script>

<style></style>
