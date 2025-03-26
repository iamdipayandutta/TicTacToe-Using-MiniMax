const board = document.getElementById("board");
const cells = document.querySelectorAll(".cell");
const status = document.getElementById("status");
const API_URL = "http://localhost:8080";

let gameState = {
    board: ["", "", "", "", "", "", "", "", ""],
    turn: "X",
    winner: null
};

function updateUI() {
    cells.forEach((cell, index) => {
        cell.textContent = gameState.board[index];
        cell.classList.remove("winning");
    });

    if (gameState.winner) {
        status.textContent = `Player ${gameState.winner} Wins!`;
    } else if (!gameState.board.includes("")) {
        status.textContent = "It's a Draw!";
    } else {
        status.textContent = `Player ${gameState.turn}'s turn`;
    }
}

async function handleCellClick(index) {
    if (gameState.winner || gameState.board[index] !== "") return;

    try {
        const response = await fetch(`${API_URL}/move`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ index: index })
        });

        if (!response.ok) throw new Error('Invalid move');
        
        gameState = await response.json();
        updateUI();
        
    } catch (error) {
        console.error('Error:', error);
    }
}

async function resetGame() {
    try {
        const response = await fetch(`${API_URL}/reset`, {
            method: 'POST'
        });
        gameState = await response.json();
        updateUI();
    } catch (error) {
        console.error('Error:', error);
    }
}

async function initGame() {
    try {
        const response = await fetch(`${API_URL}/state`);
        gameState = await response.json();
        updateUI();
    } catch (error) {
        console.error('Error:', error);
    }
}

cells.forEach((cell, index) => {
    cell.addEventListener("click", () => handleCellClick(index));
});

initGame();
