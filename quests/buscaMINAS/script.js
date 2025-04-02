let board = [];
let flags = [];
let rows, cols, mines;
let revealed = [];
let timer = 0;
let interval;
let currentDifficulty = "8-10";
let gameStarted = false;
let playerName = "Anónimo";

function showGame() {
    // Pedir el nombre del jugador y asegurarse de que se almacene correctamente
    const inputName = prompt("Ingresa tu nombre:");
    playerName = inputName && inputName.trim() !== "" ? inputName.trim() : "Anónimo";
    console.log("Nombre del jugador:", playerName); // Depuración

    // Ocultar todas las pantallas excepto la del juego
    document.getElementById("start-menu").classList.add("hidden");
    document.getElementById("instructions").classList.add("hidden");
    document.getElementById("difficulty-menu").classList.add("hidden");
    document.getElementById("game").classList.remove("hidden");
    gameStarted = true;
    startGame();
    displayRanking(); // Actualizar el ranking para reflejar el nombre
}

function showInstructions() {
    document.getElementById("start-menu").classList.add("hidden");
    document.getElementById("instructions").classList.remove("hidden");
    document.getElementById("difficulty-menu").classList.add("hidden");
    document.getElementById("game").classList.add("hidden");
}

function showDifficulty() {
    document.getElementById("start-menu").classList.add("hidden");
    document.getElementById("instructions").classList.add("hidden");
    document.getElementById("difficulty-menu").classList.remove("hidden");
    document.getElementById("game").classList.add("hidden");
}

function backToMenu() {
    document.getElementById("instructions").classList.add("hidden");
    document.getElementById("difficulty-menu").classList.add("hidden");
    document.getElementById("game").classList.add("hidden");
    document.getElementById("start-menu").classList.remove("hidden");
    gameStarted = false;
    clearInterval(interval);
}

function setDifficulty(r, m) {
    currentDifficulty = `${r}-${m}`;
    showGame();
}

function startGame() {
    const [size, mineCount] = currentDifficulty.split("-");
    rows = parseInt(size);
    cols = rows;
    mines = parseInt(mineCount);
    board = [];
    revealed = [];
    flags = [];
    timer = 0;
    clearInterval(interval);
    document.getElementById("timer").textContent = "Tiempo: 0s";
    document.getElementById("game-message").classList.add("hidden");
    interval = setInterval(updateTimer, 1000);
    generateBoard();
    renderBoard();
}

function generateBoard() {
    for (let i = 0; i < rows; i++) {
        board[i] = [];
        revealed[i] = [];
        flags[i] = [];
        for (let j = 0; j < cols; j++) {
            board[i][j] = 0;
            revealed[i][j] = false;
            flags[i][j] = false;
        }
    }
    let placed = 0;
    while (placed < mines) {
        const r = Math.floor(Math.random() * rows);
        const c = Math.floor(Math.random() * cols);
        if (board[r][c] !== "M") {
            board[r][c] = "M";
            placed++;
        }
    }
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (board[i][j] !== "M") {
                board[i][j] = countMines(i, j);
            }
        }
    }
}

function countMines(r, c) {
    let count = 0;
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            const nr = r + i;
            const nc = c + j;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] === "M") {
                count++;
            }
        }
    }
    return count;
}

function renderBoard() {
    if (!gameStarted) return;
    const gameBoard = document.getElementById("game-board");
    const cellSize = rows > 16 ? 30 : 40;
    gameBoard.style.gridTemplateColumns = `repeat(${cols}, ${cellSize}px)`;
    gameBoard.innerHTML = "";
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const cell = document.createElement("div");
            cell.classList.add("cell");
            cell.style.width = `${cellSize}px`;
            cell.style.height = `${cellSize}px`;
            cell.addEventListener("click", () => revealCell(i, j));
            cell.addEventListener("contextmenu", (e) => {
                e.preventDefault();
                toggleFlag(i, j);
            });
            if (revealed[i][j]) {
                cell.classList.add("revealed");
                cell.textContent = board[i][j] === "M" ? "💣" : board[i][j] || "";
            } else if (flags[i][j]) {
                cell.classList.add("flag");
                cell.textContent = "🚩";
            }
            gameBoard.appendChild(cell);
        }
    }
}

function toggleFlag(r, c) {
    if (revealed[r][c]) return;
    flags[r][c] = !flags[r][c];
    renderBoard();
}

function revealCell(r, c) {
    if (!gameStarted || revealed[r][c] || flags[r][c]) return;
    revealed[r][c] = true;
    if (board[r][c] === "M") {
        document.querySelectorAll(".cell").forEach(cell => cell.classList.add("revealed"));
        clearInterval(interval);
        showGameMessage("¡Boom! Perdiste.");
        return;
    }
    if (board[r][c] === 0) {
        for (let i = -1; i <= 1; i++) {
            for (let j = -1; j <= 1; j++) {
                const nr = r + i;
                const nc = c + j;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    revealCell(nr, nc);
                }
            }
        }
    }
    renderBoard();
    checkWin();
}

function checkWin() {
    if (!gameStarted) return;
    let unrevealed = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (!revealed[i][j] && board[i][j] !== "M") unrevealed++;
        }
    }
    if (unrevealed === 0) {
        clearInterval(interval);
        document.body.style.animation = "shake 0.5s";
        saveRanking();
        showGameMessage("¡Ganaste!");
    }
}

function updateTimer() {
    if (!gameStarted) return;
    timer++;
    document.getElementById("timer").textContent = `Tiempo: ${timer}s`;
}

function saveRanking() {
    const ranking = JSON.parse(localStorage.getItem("ranking") || "[]");
    ranking.push({ name: playerName, time: timer, board: `${rows}x${rows}` });
    ranking.sort((a, b) => a.time - b.time);
    localStorage.setItem("ranking", JSON.stringify(ranking.slice(0, 10)));
    displayRanking();
}

function displayRanking() {
    const ranking = JSON.parse(localStorage.getItem("ranking") || "[]");
    const tbody = document.getElementById("ranking-body");
    const playerRankingInfo = document.getElementById("player-ranking-info");
    tbody.innerHTML = "";

    // Mostrar la tabla del ranking
    ranking.forEach(entry => {
        const tr = document.createElement("tr");
        tr.innerHTML = `<td>${entry.name}</td><td>${entry.time}s</td><td>${entry.board}</td>`;
        tbody.appendChild(tr);
    });

    
    const playerEntry = ranking.find(entry => entry.name === playerName);
    if (playerEntry) {
        const position = ranking.indexOf(playerEntry) + 1;
        playerRankingInfo.textContent = `Jugador: ${playerName} - Tiempo: ${playerEntry.time}s - Posición: ${position}`;
    } else {
        playerRankingInfo.textContent = `Jugador: ${playerName} - Aún no tienes puntuación`;
    }
}

function showGameMessage(message) {
    const gameMessage = document.getElementById("game-message");
    gameMessage.textContent = message;
    gameMessage.classList.remove("hidden");
}

document.addEventListener("DOMContentLoaded", () => {
    displayRanking();
});