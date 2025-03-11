let currentPlayer = 'X';
let gameBoard = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('click', handleCellClick);
});

async function handleCellClick(e) {
    const index = parseInt(e.target.dataset.index);
    
    if (gameBoard[index] !== '' || !gameActive) return;

    // Human player move
    makeMove(index, 'X');

    if (checkWin(gameBoard, 'X')) {
        showWinMessage('Player X wins!', 'X');
        return;
    }

    if (isBoardFull(gameBoard)) {
        document.getElementById('status').textContent = "Game Draw!";
        gameActive = false;
        return;
    }

    // Delay AI move for a more natural feel
    setTimeout(async () => {
        const response = await fetch('http://127.0.0.1:5000/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ board: gameBoard }),
        });

        const data = await response.json();
        const aiMove = data.move;

        makeMove(aiMove, 'O');

        if (checkWin(gameBoard, 'O')) {
            showWinMessage('Player O wins!', 'O');
            return;
        }

        if (isBoardFull(gameBoard)) {
            document.getElementById('status').textContent = "Game Draw!";
            gameActive = false;
        }
    }, 500); // Delay for a better UX
}

function makeMove(index, player) {
    gameBoard[index] = player;
    const cell = document.querySelector(`[data-index="${index}"]`);
    cell.textContent = player;
    cell.classList.add("pop-animation");

    setTimeout(() => cell.classList.remove("pop-animation"), 200); // Animation effect

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    if (gameActive) {
        document.getElementById('status').textContent = `Player ${currentPlayer}'s turn`;
    }
}

function checkWin(board, player) {
    const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];

    return winPatterns.find(pattern => 
        pattern.every(index => board[index] === player)
    );
}

function showWinMessage(message, player) {
    document.getElementById('status').textContent = message;
    gameActive = false;

    // Highlight winning cells
    const winningPattern = checkWin(gameBoard, player);
    if (winningPattern) {
        winningPattern.forEach(index => {
            document.querySelector(`[data-index="${index}"]`).classList.add("winning");
        });
    }
}

function isBoardFull(board) {
    return board.every(cell => cell !== '');
}

function resetGame() {
    gameBoard = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    currentPlayer = 'X';
    document.querySelectorAll('.cell').forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('winning-cell'); // Remove highlight
    });
    document.getElementById('status').textContent = 'Player X\'s turn';
}

//scoreboard
let scoreX = 0;
let scoreO = 0;

function showWinMessage(message, player) {
    document.getElementById('status').textContent = message;
    gameActive = false;

    const winningPattern = checkWin(gameBoard, player);
    if (winningPattern) {
        winningPattern.forEach(index => {
            document.querySelector(`[data-index="${index}"]`).classList.add("winning");
        });
    }

    // Update scoreboard
    if (player === 'X') {
        scoreX++;
        document.getElementById('scoreX').textContent = scoreX;
    } else if (player === 'O') {
        scoreO++;
        document.getElementById('scoreO').textContent = scoreO;
    }
}

function updateScore(player) {
    const scoreElement = player === 'X' ? document.getElementById('scoreX') : document.getElementById('scoreO');

    if (player === 'X') {
        scoreX++;
        scoreElement.textContent = scoreX;
    } else {
        scoreO++;
        scoreElement.textContent = scoreO;
    }

    // Add animation class
    scoreElement.classList.add('score-animate');

    // Remove animation class after animation ends
    setTimeout(() => {
        scoreElement.classList.remove('score-animate');
    }, 1000);
}

function showWinMessage(message, player) {
    document.getElementById('status').textContent = message;
    gameActive = false;

    updateScore(player);
}
function checkWin(board, player) {
    const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6] // Diagonals
    ];

    for (let pattern of winPatterns) {
        if (pattern.every(index => board[index] === player)) {
            pattern.forEach(index => {
                document.querySelector(`[data-index="${index}"]`).classList.add('winning-cell');
            });
            return true;
        }
    }
    return false;
}
