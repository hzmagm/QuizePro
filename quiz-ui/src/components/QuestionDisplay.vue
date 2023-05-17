<template>
    <div class="question">

      <h2>Texte question?</h2>
      
      <img v-if="question.image" :src="question.image" />
      <table>
      <tr><a @click="$emit('answer-selected', 0)">La réponse A</a></tr>
      <tr><a @click="$emit('answer-selected', 1)">La réponse B</a></tr>
      <tr><a @click="$emit('answer-selected', 2)">La réponse C</a></tr>
      <tr><a @click="$emit('answer-selected', 3)">La réponse D</a></tr>
      </table>
    </div>
</template>
  
<script>
  //import quizApiService from "@/services/QuizApiService";
  
  
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
    }
  };
</script>