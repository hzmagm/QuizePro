<template>
  <div class="start-new-quiz-page text-center">
    <h1>Give it a shot!</h1>
    
    <form>
      <div class ="form-group">
        <p>We just need your name</p>
        <div class="row">
          <div class="col-md-8">
            <input type="text" v-model="username" placeholder="Pseudo" class="form-control">
          </div>

          <div class="col-md-4">
            <a  @click="launchNewQuiz" class="btn btn-light">Start</a>
          </div>
        </div>
      </div>
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
        participationStorageService.saveParticipationScore(0);
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
