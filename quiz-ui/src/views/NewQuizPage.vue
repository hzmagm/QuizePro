<template>
  <div class="start-new-quiz-page">
    <h1>Envie d'essayer?</h1>
    
    <form>
      <div class ="form-group">
        <p>On a juste besoin de ton nom!</p>
        <input type="text" v-model="username" placeholder="Username" class="form-control">
      </div>
      <a  @click="launchNewQuiz" class="btn btn-light">Commencer</a>
    </form>
  </div>
</template>

<script>
import participationStorageService from "../services/ParticipationStorageService.js";
import quizApiService from "@/services/QuizApiService";



export default {
  name: "NewQuizPage",
  data() {
    return {
      username:""
    };
  },
  methods:{
    async launchNewQuiz(){
      try{
        participationStorageService.savePlayerName(this.username)
        var newPartResponse = await quizApiService.createParticipant(this.username);
        console.log(newPartResponse);
        participationStorageService.savePlayerId(newPartResponse.data.id);
        console.log("Launch new quiz with", participationStorageService.getPlayerName());
        this.$router.push('/questions');
      }
      catch(error){
        console.log(error);
      }

    },
  },
  async created() {
    console.log("Composant NewQuiz page 'created'");
  }
};
</script>

<style>

</style>
