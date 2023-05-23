<template>
    <div class="admin">
      <h1>Admin page</h1>

      

      <form v-if="!loggedIn">
        <div class ="form-group">
          <p>Mot de passe</p>
          <input type="password" v-model="password" class="form-control">
        </div>
        <a @click="login"  class="btn btn-primary">Login</a>
      </form>

      <div v-if="(loggedIn && !showing)||(loggedIn && !editing)">
        <table >
          <tr v-for="(question,index) in questions" v-bind:key="index" @click="showQuestion(index)"><a>{{ question.title }}</a></tr>
        </table>
      </div>

      <div v-if="showing">
        <p>Supposed to be showing</p>
        <h2>{{ currentQuestion.title }}</h2>
        <h3> {{ currentQuestion.text }}</h3>    
        <!--<img v-if="questioObject.image" :src="questioObject.image" />-->
        <table >
          <tr v-for="(possibleAnswer, index) in currentQuestion.answers" :key="index"><p>{{ possibleAnswer.text }}</p></tr>
        </table>
        <button class="btn btn-warning" >Edit</button>
        <button class="btn btn-danger" >Delete</button>
      </div>


      <!--<form v-if="loggedIn && editing">
        <div class ="form-group">
          <label>Title</label>
          <input type="text" class="form-control">
          <label>Text</label>
          <input type="text" class="form-control">
        </div>
        <a @click="login"  class="btn btn-warn">Edit</a>
      
      </form>-->
        
      

      <div v-if="loggedIn">
        <button class="btn btn-danger" @click="logout">Logout</button>
      </div>
    </div>
  </template>
  
  <script>

  import quizApiService from "@/services/QuizApiService";
  
  var token="";
  
  export default {
    name: "HomePage",
    data() {
      return {
        loggedIn:false,
        editing: false,
        showing: false,
        password:"",
        questions:[],
        questionIndex:0,
        currentQuestion:{
          questionTitle: "",
          questionText: "",
          possibleAnswers: []
        },
      };
    },
    
    async created() {
      console.log("Composant Admin page 'created'");
      
    },

    methods:{
      async login(){
        console.log(this.password)
        try{
          var tokenResponse = await quizApiService.login(this.password);
          console.log(tokenResponse);
          this.loggedIn = true;
          this.getQuestions();
        }
        catch(error){
          console.log(error);
        }
      },

      logout(){
        this.loggedIn=false;
      },

      showQuestion(index){
        console.log(index);
        this.currentQuestion=this.questions[index];
        console.log(this.currentQuestion);
        this.showing=true;

      },

      editQuestion(index){
        console.log(index);
        
        this.editing=true;
      },

      async getQuestions(){
        try{
          var response = await quizApiService.getQuestions();
          this.questions= response.data
          console.log(response.data);
          
        }
        catch(error){
          console.log(error);
        }  
      }
    }
  };
  </script>
  
  <style></style>