// Restart Game Button 
var restartButton = document.querySelector("#b");
// Grabs all the squares
var allSquares = document.querySelectorAll("td");
// Clear all squares
function clearAllSquares() {
    for (var i = 0;i < allSquares.length; i++) {
        allSquares[i].textContent = "";
    }
}

// Check the sqaure marker

// Add event listener to all the buttons
restartButton.addEventListener("click", clearAllSquares);
allSquares.forEach(element => element.addEventListener("click", function(){
    if (element.textContent === "") {
        element.textContent = "X";    
    } else if (element.textContent === "X") {
        element.textContent = "O";
    } else {
        element.textContent = "";
    }
    if (["XXX"].includes(allSquares[0].textContent + allSquares[1].textContent + allSquares[2].textContent) || 
    ["XXX"].includes(allSquares[3].textContent + allSquares[4].textContent + allSquares[5].textContent) || 
    ["XXX"].includes(allSquares[6].textContent + allSquares[7].textContent + allSquares[8].textContent) || 
    ["XXX"].includes(allSquares[0].textContent + allSquares[3].textContent + allSquares[6].textContent) || 
    ["XXX"].includes(allSquares[1].textContent + allSquares[4].textContent + allSquares[7].textContent) || 
    ["XXX"].includes(allSquares[2].textContent + allSquares[5].textContent + allSquares[8].textContent) || 
    ["XXX"].includes(allSquares[0].textContent + allSquares[4].textContent + allSquares[8].textContent) || 
    ["XXX"].includes(allSquares[2].textContent + allSquares[4].textContent + allSquares[6].textContent)
    ){
        alert("Player 1 wins!");
        clearAllSquares();
    } else if (["OOO"].includes(allSquares[0].textContent + allSquares[1].textContent + allSquares[2].textContent) || 
    ["OOO"].includes(allSquares[3].textContent + allSquares[4].textContent + allSquares[5].textContent) || 
    ["OOO"].includes(allSquares[6].textContent + allSquares[7].textContent + allSquares[8].textContent) || 
    ["OOO"].includes(allSquares[0].textContent + allSquares[3].textContent + allSquares[6].textContent) || 
    ["OOO"].includes(allSquares[1].textContent + allSquares[4].textContent + allSquares[7].textContent) || 
    ["OOO"].includes(allSquares[2].textContent + allSquares[5].textContent + allSquares[8].textContent) || 
    ["OOO"].includes(allSquares[0].textContent + allSquares[4].textContent + allSquares[8].textContent) || 
    ["OOO"].includes(allSquares[2].textContent + allSquares[4].textContent + allSquares[6].textContent)
    ){
        alert("Player 2 wins!");
        clearAllSquares();
    }
}));

