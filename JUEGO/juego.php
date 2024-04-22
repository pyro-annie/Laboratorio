<?php
session_start();

// Verifica si se recibió una nueva puntuación y un nombre de jugador
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Asegúrate de validar y limpiar adecuadamente los datos de entrada
    $playerName = $_POST['playerName'];
    $player1TimeAlive = $_POST['player1TimeAlive'];
    $player2TimeAlive = $_POST['player2TimeAlive'];
    
    // Guarda la puntuación en la sesión
    $_SESSION['scores'][$playerName] = array('player1' => $player1TimeAlive, 'player2' => $player2TimeAlive);
    
    // Guardar las puntuaciones en un archivo
    saveScoresToFile($playerName, $player1TimeAlive, $player2TimeAlive);
}

// Función para guardar las puntuaciones en un archivo de texto
function saveScoresToFile($playerName, $player1TimeAlive, $player2TimeAlive) {
    $filename = 'scores.txt';
    $content = "{$playerName}: Player 1 - {$player1TimeAlive}, Player 2 - {$player2TimeAlive}\n";
    file_put_contents($filename, $content, FILE_APPEND);
}

// Función para mostrar las puntuaciones guardadas
function displayScores() {
    if (file_exists('scores.txt')) {
        $scores = file_get_contents('scores.txt');
        echo "<h2>Puntuaciones:</h2>";
        echo nl2br($scores);
    } else {
        echo "<p>No hay puntuaciones guardadas aún.</p>";
    }
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
    <button id="uploadScores">Subir Puntuajes</button>
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
    <script>
        // Asegúrate de que este código se ejecute después de que se haya cargado el archivo game.js
        document.getElementById('uploadScores').addEventListener('click', function() {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'juego.php', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function() {
                // Manejar la respuesta del servidor aquí
                console.log(this.responseText);
            };
            xhr.send('playerName=' + encodeURIComponent(playerInitials) +
                     '&player1TimeAlive=' + encodeURIComponent(player1.timeAlive) +
                     '&player2TimeAlive=' + encodeURIComponent(player2.timeAlive));
        });
    </script>
</body>
</html>
