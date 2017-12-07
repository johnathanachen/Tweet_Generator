getID = function(x){
  return document.getElementById(x);
}

submitData = function (){

    var player = getID("player_name").value;
    var score = getID("player_score").value;

    var playerCell = document.createElement("mark");
    var playerCellText = document.createTextNode(player);
    playerCell.appendChild(playerCellText);

    var scoreCell = document.createElement("small");
    var scoreCellText = document.createTextNode(score);
    scoreCell.appendChild(scoreCellText);

    var row = document.createElement("li");
    row.appendChild(playerCell);
    row.appendChild(scoreCell);

    getID("player").appendChild(row);
};
