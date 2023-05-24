<template>
  <div class="questionManager" v-if="currentQuestion">
    <h1 class="text-center">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>

<script>

import QuestionDisplay from "../components/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService.js";



export default {
  name: "QuestionManager",
  data() {
    return{
      currentQuestion:{
        questionTitle: "",
        questionText: "",
        possibleAnswers: [],
        image: ""
      },

      currentQuestionPosition: 1,
      totalNumberOfQuestion:10,
      chosenAnswers:[],
      score:0
    }
  },

  components: {  
    QuestionDisplay
  },
  
  async created() {
    console.log("Composant Question Manager 'created'");
    this.score=0;
    this.loadQuestionByPosition(1);
  },

  methods:{
    async loadQuestionByPosition(position){
      try{
        
        var response = await quizApiService.getQuestion(position);
        console.log(response.data[0]);
        this.currentQuestion={
          questionTitle: response.data[0].title,
          questionText: response.data[0].text,
          possibleAnswers: response.data[0].answers,
          image: response.data[0].image
        };

      }
      catch(error){
        console.log(error);
      }     
    },

    
    async answerClickedHandler(position){
  
      this.chosenAnswers.push(position);


      if(JSON.parse(JSON.stringify(this.currentQuestion.possibleAnswers[position].isCorrect))==true){
        this.score++;
      }

      if(this.currentQuestionPosition== this.totalNumberOfQuestion){
        this.endQuiz();
      }
      else{
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      }
      console.log("question num "+this.currentQuestionPosition + "/" +this.totalNumberOfQuestion);
      console.log("score "+ this.score);
      
    },


    async endQuiz(){
      console.log(this.chosenAnswers);

      try{
        participationStorageService.saveParticipationScore(this.score);
        var updateScoreResponse = await quizApiService.updateScore(participationStorageService.getPlayerId(),this.score);
        console.log(updateScoreResponse);
        this.$router.push('/score');
      }
      catch(error){
        console.warn(error);
      }
    }
  }
};
</script>
