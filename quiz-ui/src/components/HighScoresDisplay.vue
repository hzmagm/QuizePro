<template>
    <div class="highScores">

        <h2>Les meilleurs scores</h2>
        <div > <p>taille tableau {{ previousScores.size }}</p></div>

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
                
                <th v-for="scoreEntry in previousScores.scores" v-bind:key="scoreEntry.date">{{scoreEntry.date}}</th>
                <th v-for="scoreEntry in previousScores.scores" v-bind:key="scoreEntry.name">{{scoreEntry.date}}</th>
                <th v-for="scoreEntry in previousScores.scores" v-bind:key="scoreEntry.score">{{scoreEntry.date}}</th>
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
          "scores":[],
          "size": 1
        }
      };
    },
    

    async created() {
      console.log("Sous-Composant HighScoresDisplay 'created'");
      try{
        var scoresResponse=await quizApiService.getQuizInfo();
        this.previousScores= scoresResponse.data;
        console.log(scoresResponse.data);
      }
      catch(error){
        console.log(error);
      }
    }
  };
</script>