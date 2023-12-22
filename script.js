window.onload = function() {
    fetchLegalMoves();
}

document.getElementById("startGame").addEventListener("click", function() {
    startNewGame();
    fetchLegalMoves();
});

function startNewGame() {
    fetch('http://localhost:8000/start-new-game')
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => console.error('Error:', error));
}

function fetchLegalMoves() {
    fetch('http://localhost:8000/legal-moves')
        .then(response => response.json())
        .then(data => {
            displayLegalMoves(data.moves);
        })
        .catch(error => console.error('Error:', error));
}

function displayLegalMoves(moves) {
    const movesContainer = document.getElementById("moveButtons");
    movesContainer.innerHTML = '';
    moves.forEach(move => {
        const button = document.createElement("button");
        button.textContent = move;
        button.addEventListener("click", () => makeMove(move));
        movesContainer.appendChild(button);
    });
}

function makeMove(move) {
    if (!move) {
        move = document.getElementById("moveInput").value;
    }
    fetch('http://localhost:8000/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ move: move }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
    fetchLegalMoves();
}
