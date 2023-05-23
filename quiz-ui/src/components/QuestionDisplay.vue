<template>
    <div class="question" v-if="question">
      <h2>{{ question.questionTitle }}</h2>
      <h3> {{ question.questionText }}</h3>    
      <!--<img v-if="questioObject.image" :src="questioObject.image" />-->
      <table >
        <tr v-for="(possibleAnswer, index) in question.possibleAnswers" :key="index"><a @click="$emit('answer-selected', index)">{{ possibleAnswer.text }}</a></tr>
        
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
        possibleAnswers: []
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
      //console.log(this.questionTitle);//bizarrement title et text ne s'affichent pas sans un log
      //console.log(this.question);
    }
  };
</script>