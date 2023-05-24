//let playerName = ""
//let participationScore = 0

export default {
  clear() {
		// todo : implement
    //playerName = "";
    //participationScore = 0;
  },
  savePlayerName(playerName) {
    try{
      window.localStorage.setItem("playerName", playerName);
    }
    catch(error){
      console.warn(error);
    }
		
  },

  savePlayerId(playerId) {
    try{
      window.localStorage.setItem("playerId", playerId);
    }
    catch(error){
      console.warn(error);
    }
		
  },
  getPlayerId() {
    //return playerName;
    return window.localStorage.getItem("playerId");
    //or save the set as variable and send it here		
		// todo : implement
  },
  getPlayerName() {
    //return playerName;
    return window.localStorage.getItem("playerName");
    //or save the set as variable and send it here		
		// todo : implement
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
		//this.participationScore=participationScore
  },
  getParticipationScore() {
		// todo : implement
    return window.localStorage.getItem("participationScore");
  }
};