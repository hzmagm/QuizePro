<template>
    <div class="question">
      
      <img v-if="question.image" :src="question.image" />
      <a @click="$emit('answer-selected', 3)">La réponse D</a>
    </div>
</template>
  
<script>
  //import quizApiService from "@/services/QuizApiService";
  
  //var registeredScores=[];
  
  export default {
    name: "QuestionDisplay",
    data() {
      return {
        
      };
    },
    props: {  
        question: {    
            type: Object  
        }
    },

    emits: ["answer-selected"],

    async created() {
      console.log("Composant Question Display 'created'");
      //registeredScores=quizApiService.getQuizInfo()
    }
  };
</script>