<template>
  <div class="Score text-center">
        <h1>Score: {{ score }}</h1>
        <p v-if= "score>8">GG champion, look for your name in the Hall of Fame</p>
        <p v-if= "score<5">Ouch, keep going to school! </p>
        <p v-if= "score<=8 && score>=5">Not bad!</p>

        <HighScoresDisplay/>
  </div>
  <button class="btn btn-custom" @click="resetParticipation" >Retour</button>
</template>

<script>
import participationStorageService from "../services/ParticipationStorageService.js";
import HighScoresDisplay from "../components/HighScoresDisplay.vue";

export default {
  name: "ScorePage",
  data() {
    return {
      score:0
    };
  },
  components: {  
    HighScoresDisplay
  },

  async created() {
      console.log("Composant Home page 'created'");
      console.log("score"+ this.score);
      console.log("local storage score"+ participationStorageService.getParticipationScore());

      try{
        this.score=participationStorageService.getParticipationScore();
        console.log(this.score);
        console.log("updated version 2");
      }
      catch(error){
        console.log(error);
      }
    },

  methods:{
    async resetParticipation(){
    console.log("Reset");
    participationStorageService.clear();
    this.score = 0;
    this.$router.push('/home');
  }
  },

  
};
</script>

<style>
.btn-custom{
  background-color: white;
  color: red;
}</style>
