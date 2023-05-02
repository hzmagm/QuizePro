let playerName = ""
let participationScore = 0

export default {
  clear() {
		// todo : implement
  },
  savePlayerName(playerName) {
    try{
      playerName=window.localStorage.setItem("playerName", playerName);
    }
    catch(error){
      console.warn(error);
    }
		
  },
  getPlayerName() {
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