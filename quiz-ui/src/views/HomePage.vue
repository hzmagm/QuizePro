<template>
  <div class="home">
    <h1>Home page</h1>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
    <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

var registeredScores=[];

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    registeredScores=quizApiService.getQuizInfo()
  }
};
</script>

<style></style>