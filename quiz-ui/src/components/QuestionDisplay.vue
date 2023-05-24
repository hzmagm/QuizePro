<template>
    <div class="question" v-if="question">
      <h2 class="text-center">{{ question.questionTitle }}</h2>
      <h3 class="text-center"> {{ question.questionText }}</h3>    
      <img v-if="question.image" src="question.image" height="250"/>
      <img v-if="!question.image" src="@/assets/questionmark.png" height="250"/>
      <table >
        <tr v-for="(possibleAnswer, index) in question.possibleAnswers" :key="index"><a @click="$emit('answer-selected', index)">{{ index+1 }} ) {{ possibleAnswer.text }}</a></tr>
        
      </table>
    </div>
</template>
  
<script>

  
  export default {
    name: "QuestionDisplay",
    data() {
      return {
        questionTitle: "",
        questionText: "",
        possibleAnswers: [],
        image: ""
      };
    },
    props: {  
      question: {
        type: Object
      }
        /*
        {
          questionTitle: "",
          questionText: "",
          possibleAnswers: []
          image
        }
      */         
    },

    emits: ["answer-selected"],

    async created() {
      console.log("Sous-Composant Question Display 'created'");
      console.log(this.question.questionText);
      this.questionTitle=this.question.questionTitle;
      this.questionText=this.question.questionText;
      this.possibleAnswers=this.question.possibleAnswers;
      this.image = this.question.image;
      //console.log(this.questionTitle);//bizarrement title et text ne s'affichent pas sans un log
      //console.log(this.question);
    }
  };
</script>