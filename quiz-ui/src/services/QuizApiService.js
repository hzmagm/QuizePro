import axios from "axios";
import adminDataStorage from "./AdminDataStorage";

const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {

    return this.call("get", "questions/quiz-info");
  },
  getQuestion(position) {

    return this.call("get", "/questions?position="+position);
  },

  createParticipant(name){
    const data = {
      "pseudoName":name,    
    };
    return this.call("post","participations/add", data);
  },

  updateScore(id, score){

    const data = {
      "score":score
      
    };
    
    return this.call("put","participations/"+id, data)
    
  },

  getHighScores(){
    return this.call("get","participations/all_ordered");
  },

  login(password){

    const data = {
      "password":password,      
    };

    return this.call("post","/admin/login", data)
  },


//ADMIN ENDPOINTS

  createQuestion(data){

    return this.call("post","admin/questions/", data, this.token)
  },




  updateQuestion(questionId,title,text,image,position,possibleAnswers){

    const data = {
      "title":title,
      "text":text,
      "image":image,
      "position":position,
      "possibleAnswers":possibleAnswers    
    };

    return this.call("put","questions/"+questionId, data, this.token);
    
  },



  deleteQuestion(questionId){

    this.token = adminDataStorage.getToken();
    console.log("token"+ this.token);
    return this.call("DELETE","admin/questions/"+questionId, null, this.token);
  },



  deleteAllQuestions(){

    return this.call("delete","admin/questions/all", null, this.token);
  },


  deleteAllParticipants(){

    this.call("delete","admin/participations/all", null, this.token);
  },

  getQuestions(){
    return this.call("get","questions/");
  }

};