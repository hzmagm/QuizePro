<template>
  <div class="questionManager" v-if="currentQuestion">
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>

<script>

import QuestionDisplay from "../components/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService.js";
import { callWithErrorHandling } from "vue";

var score = 0;

export default {
  name: "QuestionManager",
  data() {
    return{
      currentQuestion:{
        questionTitle: "",
        questionText: "",
        possibleAnswers: []
      },

      currentQuestionPosition: 1,
      totalNumberOfQuestion:10,
      chosenAnswers:[]
    }
  },

  components: {  
    QuestionDisplay
  },
  
  async created() {
    console.log("Composant Question Manager 'created'");
    try{
      var test = await quizApiService.getQuestion(5);
      console.log(test.data);
    }
    catch(error){
      console.log(error);
    }
    //console.log("playing with "+ participationStorageService.getPlayerName())
    this.loadQuestionByPosition(1);
    //registeredScores=quizApiService.getQuizInfo()
  },

  methods:{
    async loadQuestionByPosition(position){
      try{
        
        var response = await quizApiService.getQuestion(position);
        console.log(response.data[0].answers);
        this.currentQuestion={
          questionTitle: response.data[0].title,
          questionText: response.data[0].text,
          possibleAnswers: response.data[0].answers
        };

      }
      catch(error){
        console.log(error);
      }     
    },

    
    async answerClickedHandler(position){
      
      //console.log(JSON.parse(JSON.stringify(this.currentQuestion.possibleAnswers[position].isCorrect)));

      this.chosenAnswers.push(position);


      if(JSON.parse(JSON.stringify(this.currentQuestion.possibleAnswers[position].isCorrect))==true){
        score++;
      }

      if(this.currentQuestionPosition== this.totalNumberOfQuestion){
        this.endQuiz();
      }
      else{
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      }
      console.log("question num "+this.currentQuestionPosition + "/" +this.totalNumberOfQuestion);
      console.log("score "+ score);
      
    },


    async endQuiz(){
      //register score
      console.log(this.chosenAnswers);

      try{
        participationStorageService.saveParticipationScore(score);
        var updateScoreResponse = await quizApiService.updateScore(participationStorageService.getPlayerId(),score);
        console.log(updateScoreResponse);
        this.$router.push('/score');
      }
      catch(error){
        console.warn(error);
      }
      //send to result page
    }
  }
};
</script>
