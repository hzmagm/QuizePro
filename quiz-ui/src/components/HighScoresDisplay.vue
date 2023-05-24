<template>
    <div v-if="!empty" class="highScores">

        <h2>Les 10 meilleurs scores</h2>

            <table class="table">
              
            <thead>
                <tr>
                <th scope="col">Pseudo</th>
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

    <div v-if="empty">
    
      <h2>Sois le premier (et donc le meilleur!)</h2>
    
    </div>
</template>
  
<script>
    

  import quizApiService from "@/services/QuizApiService";
  
  
  export default {
    name: "HighScoreDisplay",
    data() {
      return {
        emtpty : false,
        previousScores:{
          "scores":[]
        }
      };
    },
    
    async created() {
      this.empty=false;
      console.log("Sous-Composant HighScoresDisplay 'created'");
      console.log(this.empty);
      try{
        var scoresResponse=await quizApiService.getHighScores();
        this.previousScores= scoresResponse.data.slice(0,10);
        console.log(this.previousScores);

      }
      catch(error){
        console.log(error);
        this.empty=true;
      }
    }
  };
</script>