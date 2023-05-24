export default {
  clear() {
    window.localStorage.removeItem("playerName");
    window.localStorage.removeItem("playerId");
    window.localStorage.removeItem("participationScore");
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
    return window.localStorage.getItem("playerId");
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem("participationScore");
  }
};