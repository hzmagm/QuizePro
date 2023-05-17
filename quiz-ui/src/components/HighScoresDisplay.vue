<template>
    <div class="highScores">

        <h2>Les meilleurs scores</h2>

            <table class="table">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <div ></div>
                <th v-for="scoreEntry in previousScores" v-bind:key="scoreEntry.date">{{scoreEntry.date}}</th>
                </tr>
            </tbody>
            </table>
    </div>
</template>
  
<script>
    
  var previousScores = [];
  
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