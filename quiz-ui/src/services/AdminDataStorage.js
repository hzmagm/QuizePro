export default {
    clear() {
        window.localStorage.removeItem("token")
    },
    saveToken(token) {
      try{
        window.localStorage.setItem("token", token);
      }
      catch(error){
        console.warn(error);
      }
          
    },
    getToken() {
      //return token;
      return window.localStorage.getItem("token");
      //or save the set as variable and send it here		
          // todo : implement
    }
  };