<template>
    <div class="highScores">

        <h2>Les 10 meilleurs scores</h2>

            <table class="table">
              
            <thead>
                <tr>
                <th scope="col">Name</th>
                <th scope="col">Score</th>
                </tr>
            </thead>
            
            <tbody>
                
                <tr v-for="(scoreEntry,index) in previousScores" v-bind:key="index">
                  <td>{{scoreEntry.pseudoName}}</td>
                
                  <td>{{scoreEntry.score}}</td>
                </tr>
            </tbody>
            </table>
    </div>
</template>
  
<script>
    

  import quizApiService from "@/services/QuizApiService";
  
  
  export default {
    name: "HighScoreDisplay",
    data() {
      return {
        previousScores:{
          "scores":[]
        }
      };
    },
    

    async created() {
      console.log("Sous-Composant HighScoresDisplay 'created'");
      try{
        var scoresResponse=await quizApiService.getHighScores();
        this.previousScores= scoresResponse.data.slice(0,10);
      }
      catch(error){
        console.log(error);
      }
    }
  };
</script>