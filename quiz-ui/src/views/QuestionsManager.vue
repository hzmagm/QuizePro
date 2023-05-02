<template>
  <div class="questionManager">
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
  </div>
</template>

<script>

import QuestionDisplay from "./QuestionDisplay.vue";

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
      totalNumberOfQuestion:10
    }
  },

  components: {  
    QuestionDisplay
  },
  
  async created() {
    console.log("Composant Question Manager 'created'");
    this.loadQuestionByPosition(0);
    //registeredScores=quizApiService.getQuizInfo()
  },

  methods:{
    async loadQuestionByPosition(position){

    },

    async answerClickedHandler(position){
      this.loadQuestionByPosition(position);
      if(position== this.currentQuestion.possibleAnswers.length){
        this.endQuiz();
      }
    },


    async endQuiz(){
      //send to result page
    }
  }
};
</script>
