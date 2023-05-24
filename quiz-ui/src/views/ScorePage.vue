<template>
  <div class="Score">
        <h1>Score: {{ score }}</h1>
        <p v-if= "score>8">Bien joué champion(ne), vérifie si tu as ta place parmis les plus grands!</p>
        <p v-if= "score<5">Aïe, continue l'école!</p>
        <p v-if= "score<8 && score>5">Pas mal!</p>

  </div>

  <!--<h2>Vos scores précédents</h2>

  <table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Score</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <div ></div>
        <th v-for="scoreEntry in previousScores" v-bind:key="scoreEntry.date">{{scoreEntry.date}}</th>
      </tr>
    </tbody>
  </table>-->

  <HighScoresDisplay/>

  <router-link to="/home">Retour</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
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
    //registeredScores=quizApiService.getQuizInfo()
  }
};
</script>

<style></style>
