<?php
session_start();

// Verifica si se recibió una nueva puntuación y un nombre de jugador
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Asegúrate de validar y limpiar adecuadamente los datos de entrada
    $playerName = $_POST['playerName'];
    $score = $_POST['score'];
    // Identifica si es Player1 o Player2
    $playerId = $playerName == 'Player1' ? 1 : 2;
    // Guarda la puntuación en la sesión
    $_SESSION['scores'][$playerId][] = $score;
}

// Función para guardar una nueva puntuación
function saveScore($playerName, $score) {
    // Asegúrate de validar y limpiar adecuadamente los datos de entrada
    $playerId = $playerName == 'Player1' ? 1 : 2;
    // Guarda la puntuación en la sesión
    $_SESSION['scores'][$playerId][] = $score;
}
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $playerInitials = $_POST['playerInitials'];
    $player1Time = $_POST['player1Time'];
    $player2Time = $_POST['player2Time'];
    saveScoresToFile($playerInitials, $player1Time, $player2Time);
}
// Función para mostrar las puntuaciones guardadas
function displayScores() {
    if (!empty($_SESSION['scores'])) {
        echo "<h2>Puntuaciones:</h2>";
        foreach ($_SESSION['scores'] as $playerId => $scores) {
            echo "<h3>Player" . $playerId . "</h3>";
            foreach ($scores as $score) {
                echo "<p>Puntuación: " . htmlspecialchars($score) . "</p>";
            }
        }
    } else {
        echo "<p>No hay puntuaciones guardadas aún.</p>";
    }
}

// Modificar la función para guardar las puntuaciones en un archivo de texto
function saveScoresToFile($playerInitials, $player1Time, $player2Time) {
    $filename = 'scores.txt';
    $content = "{$playerInitials}: Player 1 - {$player1Time}, Player 2 - {$player2Time}\n";
    file_put_contents($filename, $content, FILE_APPEND);
}


displayScores();

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Juego Espacial</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="playerInitialsDisplay"></div>
    <div id="menu">
        <button id="singleplayer">Solo</button>
        <button id="multiplayer">Co-op</button>
        <button id="scores">Puntuaciones</button>
    </div>
    <canvas id="gameCanvas"></canvas>
    <!-- Elementos para la pantalla de Game Over -->
    <div id="gameOverDisplay" style="display: none;">
        <h1>Game Over</h1>
        <p id="player1Score">Puntuación Jugador 1: 0</p>
        <p id="player2Score">Puntuación Jugador 2: 0</p>
        <p id="winner"></p> <!-- Nueva ID para mostrar al ganador -->
        <button id="rematchButton">Revancha</button>
    </div>
    <script src="game.js"></script>
</body>
</html>
