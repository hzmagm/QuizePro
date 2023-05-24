<template>
    <div class="admin">
      <h1>V.I.P Access</h1>

      <form v-if="!loggedIn">
        <div class ="form-group">
          <p>Password</p>
          <input type="Mot de passe" v-model="password" class="form-control">
        </div>

        <a @click="login"  class="btn btn-primary">Login</a>
      </form>

      <div v-if="(loggedIn && !showing)||(loggedIn && !editing)">
        <table >
          <tr v-for="(question,index) in questions" v-bind:key="index" @click="showQuestion(index)"><a>{{ question.title }}</a></tr>
        </table>
        <button class="btn btn-primary" @click="createMode">Add</button>
      </div>

      <div v-if="showing && loggedIn">
        <h2>{{ currentQuestion.title }}</h2>
        <h3> {{ currentQuestion.text }}</h3>    
        <table >
          <tr v-for="(possibleAnswer, index) in currentQuestion.answers" :key="index"><p>{{ possibleAnswer.text }}</p></tr>
        </table>
        <button class="btn btn-warning" @click="editMode">Edit</button>
        <button class="btn btn-danger" @click="deleteQuestion">Delete</button>
      </div>


      <form v-if="loggedIn && (editing || adding)">
        <div class ="form-group">
          <label>Position</label>
          <input type="number" min="1" max = "{{ questions.length }}" class="form-control" v-model="questionBody.position">
          <label>Title</label>
          <input type="text" class="form-control" v-model="questionBody.title">
          <label>Text</label>
          <input type="text" class="form-control" v-model="questionBody.text">
          <label>Possible Answers</label>
          <input type="text" class="form-control" v-model="questionBody.possibleAnswers[0].text">
          <input type="radio" name="correct" v-model.number="selectedAnswerIndex" value="0">
          <input type="text" class="form-control" v-model="questionBody.possibleAnswers[1].text">
          <input type="radio" name="correct" v-model.number="selectedAnswerIndex" value="1">
          <input type="text" class="form-control" v-model="questionBody.possibleAnswers[2].text">
          <input type="radio" name="correct" v-model.number="selectedAnswerIndex" value="2">
          <input type="text" class="form-control" v-model="questionBody.possibleAnswers[3].text">
          <input type="radio" name="correct" v-model.number="selectedAnswerIndex" value="3">

        </div>
        <a v-if="editing" @click="confirmEdit"  class="btn btn-warning">Confirm</a>
        <a v-if="adding" @click="confirmCreate"  class="btn btn-primary">Confirm</a>
        <a  @click="showMainPage" class="btn btn-light">Cancel</a>
      
      </form>

      <div v-if="loggedIn">
        <button class="btn btn-danger" @click="logout">Logout</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  import quizApiService from "@/services/QuizApiService";
  import adminDataStorage from "@/services/AdminDataStorage";
  
  
  export default {
    name: "HomePage",
    data() {
      return {
        loggedIn:false,
        editing: false,
        showing: false,
        adding: false,
        password:"",
        questions:[],
        questionIndex:0,
        questionId:0,
        currentQuestion:{
          questionTitle: "",
          questionText: "",
          possibleAnswers: [
          ]
        },
        questionBody:{
          title:"",
          text:"",
          image:"",
          position:0,
          possibleAnswers:[
            {
              text:"",
              isCorrect:false

            },
            {
              text:"",
              isCorrect:false
            },
            {
              text:"",
              isCorrect:false
            },
            {
              text:"",
              isCorrect:false
            }],
          
        },
        selectedAnswerIndex:0
      };
    },
    
    async created() {
      console.log("Composant Admin page 'created'");
      
    },

    methods:{
      async login(){
        console.log(this.password);
       

          const data = {
            password: this.password
          };

          try{
            const tokenResponse = await axios.post("http://127.0.0.1:5000/admin/login", data);// we had a problem using QuizAPIService, response was undefined
            adminDataStorage.saveToken(tokenResponse.data.token);
            console.log("Log token response");
            //console.log(quizApiService.token);
            this.loggedIn = true;
            this.getQuestions();
          }
          catch(error){
            console.log(error);
          }    
        
      },

      showMainPage(){
        this.getQuestions();
        this.editing=false;
        this.showing=false;
        this.adding = false;
      },

      logout(){
        this.loggedIn=false;
        this.editing=false;
        this.showing=false;
      },

      showQuestion(index){
        this.editing=false;
        this.showing=true;
        console.log(index);
        this.questionIndex=index;
        
        this.currentQuestion=this.questions[index];
        this.questionId=this.currentQuestion.id;
        console.log(this.currentQuestion);
        

      },

      editMode(index){
        console.log(index);
        this.showing = false;
        this.adding = false;
        this.editing=true;
      },

      async deleteQuestion(){
        console.log(quizApiService.instance);
        if (window.confirm("Delete this question?")) {
          
          console.log("Question to del"+ this.questionId);

          try{        
            var deleteResponse = await quizApiService.deleteQuestion(this.questionId);
            console.log(deleteResponse);          
          }
          catch(error){
            console.log(error);
          }

          this.showMainPage();
        }       
        
      },

      createMode(){
        console.log("create mode")
        this.editing= false;
        this.showing= false;
        this.adding= true;

      },

      async confirmCreate(){
        try{
          console.log("selected"+this.selectedAnswerIndex);
          console.log(this.questionBody.possibleAnswers[0]);
          this.questionBody.possibleAnswers[this.selectedAnswerIndex].isCorrect=true;
          var response = await quizApiService.createQuestion(this.questionBody);
          this.questions= response.data
          console.log(response.data);
          
        }
        catch(error){
          console.log(error);
        }  
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