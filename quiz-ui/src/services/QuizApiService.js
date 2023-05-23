import axios from "axios";

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
    /*
    - **size** : Entier positif retournant le nombre de questions contenues dans le quiz
    - **scores** : tableau d’objets participationResult trié par scores décroissants et dont chaque entrée donne :
      - playerName : nom du joueur
      - score : score obtenu à l’époque
      - date : date de la participation au format dd/MM/yyyy hh:mm:ss
    */
    return this.call("get", "questions/quiz-info");
  },
  getQuestion(position) {/*
    - **question**
    - **position** : entier positif désignant le numéro de la question
    - **title** : texte contenant le titre de la question
    - **position** : position de la question dans le quiz (normalement identique au paramètre d’entrée...)
    - **text** : intitulé de la question
    - **image** : une image au format base 64 associée à la question
    - **possibleAnswers** : liste des réponses possibles contenant chacune :
        - **id :** id base de données de la réponse
        - **text** : intitulé de la réponse
        - **isCorrect** : booléen indiquant si la réponse est la bonne ou non
    */
    // not implemented
    return this.call("get", "/questions?position="+position);
  },

  submitAnswers(playerName,answers){
    /* needs: - **player_name** : le nom du joueur qui poste son questionnaire
              - **answers** : la liste des positions de réponses choisies dans l’ordre des questions du quiz
        returns:
              - **answersSummaries** : tableau de type answerSummary, dont chaque entrée donne, dans l’ordre des questions du quiz :
                - correctAnswerPosition : position de la réponse correcte à la question
                - wasCorrect : état de la réponse fournie par le joueur
              - playerName : nom du joueur tel qu’il a été saisi au début du quiz
              - score : score obtenu
    */
    const data = {
      "playerName":playerName,
      "answers":answers,
      
    };
    
    this.call("post","participation", data)
    
  },

  login(password){
    /* 
    needs password
    returns token : le token en question si le mot de passe est le bon*/

    const data = {
      "password":password,      
    };

    this.call("post","admin/login", data)
  },


  //ADMIN ENDPOINTS

  createQuestion(title,text,image,position,possibleAnswers){
    /*
## Paramètres du corps de requête

- **Question**
    - **title** : le titre de la question
    - **text** : la question en tant que telle
    - **image** : image en base 64
    - **position** : la position de la question dans le quiz. Peut provoquer un décalage des positions des autres questions si cette position est déjà prise. Il est interdit de mettre une position supérieure au nombre de questions déjà en base.
    - **possibleAnswers** : liste des réponses possibles contenant chacune :
        - text : l’intitulé de la réponse elle-même
        - isCorrect : booléen indiquant si la réponse est la bonne ou non (vérification à prévoir pour éviter les doublons)

## Retour

HTTP : 200 - Ok

Payload de retour :

- id : identifiant en base de données de la question créée
    */


    const data = {
      "title":title,
      "text":text,
      "image":image,
      "position":position,
      "possibleAnswers":possibleAnswers    
    };

    this.call("post","questions", data, this.token)
  },




  updateQuestion(questionId,title,text,image,position,possibleAnswers){
    /*
    ## Paramètres de corps de requête

- **Question**
    - **title** : le titre de la question
    - **text** : l’intitulé de la question
    - **image** : image en base 64
    - **position** : la position (potentiellement nouvelle) de la question dans le quiz. Peut provoquer un décalage des positions des autres questions si cette position est déjà prise. Il est interdit de mettre une position supérieure au nombre de questions déjà en base.
    - **possibleAnswers** : liste des réponses possibles contenant chacune :
        - text : l’intitulé de la réponse
        - isCorrect : booléen indiquant si la réponse est la bonne ou non (vérification à prévoir pour éviter les doublons)

## Retour

HTTP : 204 - No Content

Payload de retour : vide
    */
    const data = {
      "title":title,
      "text":text,
      "image":image,
      "position":position,
      "possibleAnswers":possibleAnswers    
    };

    this.call("put","questions/"+questionId, data, this.token);
    
  },



  deleteQuestion(questionId){
    /**
     * ## Paramètres d’URL

- questionId : idenfiant de la question en base de données

## Retour

HTTP : 204 - No Content

Payload de retour : vide
     */

    this.call("delete","questions/"+questionId, null, this.token);
  },



  deleteAllQuestions(){
    /**
     *## Paramètres d’URL

Aucun

## Retour

HTTP : 204 - No Content

Payload de retour : vide
     */

    this.call("delete","questions/all", null, this.token);
  },


  deleteAllParticipants(){
    /**
     *## Paramètres d’URL

Aucun

## Retour

HTTP : 204 - No Content

Payload de retour : vide
     */

    this.call("delete","participationq/all", null, this.token);
  },

  getQuestions(){
    return this.call("get","questions/");
  }


};