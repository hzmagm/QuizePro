<template>
  <div class="start-new-quiz-page">
    <h1>This is the quiz page</h1>
    
    <form>
      <div class ="form-group">
        <p>Saisissez votre nom</p>
        <input type="text" v-model="username" placeholder="Username" class="form-control">
      </div>
      <button type="submit" @click="launchNewQuiz" class="btn btn-light">Commencer</button>
    </form>
  </div>
</template>

<script>
import participationStorageService from "../services/ParticipationStorageService.js";

let username = ""

export default {
  name: "NewQuizPage",
  data() {
    return {
    };
  },
  methods:{
    launchNewQuiz(){
      username = participationStorageService.getPlayerName()
      console.log("Launch new quiz with", this.username);
      this.$router.push('/questions');
    },
  },
  async created() {
    console.log("Composant NewQuiz page 'created'");
  }
};
</script>

<style>

</style>
