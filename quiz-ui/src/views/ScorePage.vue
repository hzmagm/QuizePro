<template>
  <div class="Score">
        <h1>Score: {{ score }}</h1>
        <p>Your score is {{ score }}</p>

  </div>

  <h2>Vos scores précédents</h2>

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
  </table>

  <HighScoresDisplay/>

  <router-link to="/home">Retour</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService.js";
import HighScoresDisplay from "../components/HighScoresDisplay.vue";


var score=0;

var previousScores = [];

export default {
  name: "ScorePage",
  data() {
    return {
      
    };
  },
  components: {  
    HighScoresDisplay
  },
  async created() {
    console.log("Composant Home page 'created'");
    score=participationStorageService.getParticipationScore();
    //registeredScores=quizApiService.getQuizInfo()
  }
};
</script>

<style></style>
