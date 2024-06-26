// Variables globales 
let canvas, ctx; 
let player1, player2;
let gameRunning = true; 
let stars = []; // Array para las estrellas 
const numStars = 100; // Número de estrellas en el fondo 
let redEnemies = []; 
let whiteEnemies = []; 
let player1Projectiles = []; 
let player2Projectiles = []; 
const fireRate = 500; // Frecuencia de disparo en milisegundos 
let lastFiredPlayer1 = Date.now(); 
let lastFiredPlayer2 = Date.now(); 
let startTime = Date.now(); // Guarda el tiempo al inicio del juego 
let elapsedTime = 0; // Tiempo transcurrido 
let gameOver = false; 
let playerInitials = ''; 
let animationFrameId; // ID para cancelar el bucle del juego 
// Función para crear enemigos rojos con posición x aleatoria en el lado derecho del canvas 
function createRedEnemy() { 
    return { 
        x: canvas.width + Math.random() * 200, // Generar enemigos en el lado derecho del canvas 
        y: Math.random() * canvas.height, 
        width: 20, 
        height: 20, 
        color: 'red', 
        destructible: true 
    }; 
} 
// Función para crear enemigos blancos con posición x aleatoria en el lado derecho del canvas 
function createWhiteEnemy() { 
    return { 
        x: canvas.width + Math.random() * 200, // Generar enemigos en el lado derecho del canvas 
        y: Math.random() * canvas.height, 
        width: 20, 
        height: 20, 
        color: 'white', 
        destructible: false 
    }; 
} 
// Función para crear estrellas 
function createStars() { 
    stars = []; 
    for (let i = 0; i < numStars; i++) { 
        stars.push({ 
            x: Math.random() * canvas.width, 
            y: Math.random() * canvas.height, 
            size: Math.random() * 3 
        }); 
    } 
} 
// Función para dibujar estrellas 
function drawStars(ctx) { 
    stars.forEach(star => { 
        ctx.fillStyle = 'white'; 
        ctx.fillRect(star.x, star.y, star.size, star.size); 
    }); 
} 
// Función para mover las estrellas 
function moveStars() { 
    for (let star of stars) { 
        star.y += 1.5; // Velocidad a la que se mueven las estrellas 
        if (star.y > canvas.height) { 
            star.y = 0; 
            star.x = Math.random() * canvas.width; 
        } 
    } 
} 
// Función para crear una nave 
function createShip(color, controls) { 
    return { 
        x: 30, 
        y: canvas.height / 2, 
        width: 20, 
        height: 20, 
        color: color, 
        controls: controls, 
        score: 0, 
        alive: true, 
        moveUp: false, 
        moveDown: false, 
        moveLeft: false, 
        moveRight: false 
    }; 
} 
// Función para dibujar la nave con forma de triángulo 
function drawShip(ship, ctx) { 
    ctx.fillStyle = ship.color; 
    ctx.beginPath(); 
    ctx.moveTo(ship.x - ship.width / 2, ship.y); 
    ctx.lineTo(ship.x + ship.width / 2, ship.y + ship.height / 2); 
    ctx.lineTo(ship.x + ship.width / 2, ship.y - ship.height / 2); 
    ctx.closePath(); 
    ctx.fill(); 
} 
// Función para actualizar la posición de los enemigos 
function updateEnemies(enemies) { 
    for (let enemy of enemies) { 
        enemy.x -= 5; // Velocidad a la que se mueven los enemigos 
        if (enemy.x + enemy.width < 0) { 
            // Si el enemigo sale del canvas, lo reinicias al otro lado 
            enemy.x = canvas.width; 
            enemy.y = Math.random() * canvas.height; 
        } 
    } 
} 
// Función para dibujar enemigos 
function drawEnemy(enemy, ctx) { 
    ctx.fillStyle = enemy.color; 
    ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height); 
} 
function handleGameOver() {
    // Detiene el bucle del juego
    cancelAnimationFrame(animationFrameId);

    // Actualiza las puntuaciones en la pantalla de 'Game Over'
    document.getElementById('player1Score').textContent = 'Tiempo Jugador 1: ' + player1.timeAlive.toFixed(2) + ' segundos';
    document.getElementById('player2Score').textContent = 'Tiempo Jugador 2: ' + player2.timeAlive.toFixed(2) + ' segundos';

    // Muestra la pantalla de 'Game Over' y oculta el canvas del juego
    document.getElementById('gameOverDisplay').style.display = 'block';
    document.getElementById('gameCanvas').style.display = 'none';

    // Muestra el botón de revancha
    document.getElementById('rematchButton').style.display = 'block';

    // Determina y muestra el ganador
    determineWinner();
}


function playerLost(player) {
    if (player.alive) {
        player.alive = false;
        // Calcula el tiempo de supervivencia en el momento de la pérdida
        player.timeAlive = (Date.now() - player.startTime) / 1000;
        // Mueve la nave fuera de la pantalla
        player.x = -100;

        // Verifica si ambos jugadores han perdido para detener el juego
        if (!player1.alive && !player2.alive) {
            gameRunning = false;
            handleGameOver();
        }
    }
}
function decideTieBreaker() {
    // Lógica para declarar que los enemigos ganaron en caso de empate
    return '¡Los enemigos ganan!';
}


// Función para determinar el ganador
function determineWinner() {
    let winnerText = '';
    if (player1.timeAlive > player2.timeAlive) {
        winnerText = '¡Jugador 1 gana!';
    } else if (player2.timeAlive > player1.timeAlive) {
        winnerText = '¡Jugador 2 gana!';
    } else {
        // En caso de empate, decide un ganador por otro criterio
        winnerText = decideTieBreaker();
    }
    document.getElementById('winner').textContent = winnerText;
}

function updateScore(player) {
    // Asegúrate de que el identificador del jugador sea 'player1' o 'player2'
    let playerId = player === player1 ? 'player1' : 'player2';
    // Actualizar la puntuación del jugador en el elemento correspondiente
    document.getElementById(playerId + 'Score').textContent = 'Puntuación ' + playerId.charAt(0).toUpperCase() + playerId.slice(1) + ': ' + player.score;
}


// Función para detectar colisiones y manejar el fin del juego
function checkCollisions(players, enemies) {
    players.forEach(player => {
        if (player.alive) {
            enemies.forEach(enemy => {
                if (detectCollision(player, enemy)) {
                    // El jugador ha colisionado con un enemigo y ha perdido
                    playerLost(player);
                }
            });
        }
    });

    // Verificar si ambos jugadores han muerto antes de llamar a handleGameOver
    let alivePlayers = players.filter(player => player.alive);
    if (alivePlayers.length === 0 && !gameOver) {
        gameOver = true;
        handleGameOver();
    }
}


// Función para mostrar la pantalla de "Game Over" y determinar el ganador
// Función para manejar el fin del juego

function updateDisplayWithPlayerInitials(initials) { 
    // Actualiza el elemento de visualización con las iniciales del jugador 
    // Asegúrate de tener un elemento en tu HTML con el id 'playerInitialsDisplay' 
    document.getElementById('playerInitialsDisplay').textContent = initials; 
} 
// Función para mostrar el botón de revancha y manejar eventos 
function displayRematchButton() { 
    // Obtener el botón por su ID 
    const rematchButton = document.getElementById('rematchButton'); 
    // Mostrar el botón 
    rematchButton.style.display = 'block'; 
    // Manejar el evento de clic para reiniciar el juego 
    rematchButton.addEventListener('click', function() { 
        // Reiniciar el juego 
        restartGame(); 
    }); 
} 
// Asegúrate de que esta función se llame solo una vez al cargar la página o al reiniciar el juego 
function setupRematchButton() { 
    const rematchButton = document.getElementById('rematchButton'); 
    // Eliminar cualquier manejador de evento previo para evitar duplicados 
    rematchButton.removeEventListener('click', restartGame); 
    // Agregar el manejador de evento de clic para reiniciar el juego 
    rematchButton.addEventListener('click', restartGame); 
} 

function restartGame() {
    // Recargar la página
    window.location.reload();
}

function drawTime(ctx, time) { 
    ctx.font = '20px Arial'; 
    ctx.fillStyle = 'white'; 
    ctx.fillText('Tiempo: ' + time, canvas.width - 150, 30); 
} 
// También asegúrate de que la función detectCollision esté definida y funcione correctamente 
function detectCollision(player, enemy) { 
    // Calcular el centro de la nave y del enemigo 
    let playerCenterX = player.x + player.width / 2; 
    let playerCenterY = player.y + player.height / 2; 
    let enemyCenterX = enemy.x + enemy.width / 2; 
    let enemyCenterY = enemy.y + enemy.height / 2; 
    // Calcular la distancia entre los centros de la nave y del enemigo 
    let distanceX = playerCenterX - enemyCenterX; 
    let distanceY = playerCenterY - enemyCenterY; 
    let distance = Math.sqrt(distanceX * distanceX + distanceY * distanceY); 
    // Determinar si hay colisión basándose en la distancia 
    return distance < (player.width / 2 + enemy.width / 2); 
} 
function initGame() { 
    canvas = document.getElementById('gameCanvas'); 
    ctx = canvas.getContext('2d'); 
    canvas.width = 800; // Ancho del canvas 
    canvas.height = 600; // Alto del canvas 
    player1 = createShip('blue', { up: 'w', left: 'a', down: 's', right: 'd' }); 
    player2 = createShip('green', { up: 'ArrowUp', left: 'ArrowLeft', down: 'ArrowDown', right: 'ArrowRight' });
    player1.startTime = Date.now();
    player2.startTime = Date.now();
    redEnemies = Array(5).fill().map(createRedEnemy); // Crea 5 enemigos rojos 
    whiteEnemies = Array(5).fill().map(createWhiteEnemy); // Crea 5 enemigos blancos 
    createStars(); 
    document.addEventListener('keydown', function(event) { 
        handleKey(event, true); 
    }); 
    document.addEventListener('keyup', function(event) { 
        handleKey(event, false); 
    }); 
    startTime = Date.now(); // Añade esta línea para guardar el tiempo al inicio del juego 
    gameLoop(); 
} 
// Función para manejar eventos de teclado 
function handleKey(event, isKeyDown) { 
    const key = event.key.toLowerCase(); // Convertir la tecla a minúsculas 
    if (player1.controls && key === player1.controls.up.toLowerCase()) { 
        player1.moveUp = isKeyDown; 
    } else if (player1.controls && key === player1.controls.left.toLowerCase()) { 
        player1.moveLeft = isKeyDown; 
    } else if (player1.controls && key === player1.controls.down.toLowerCase()) { 
        player1.moveDown = isKeyDown; 
    } else if (player1.controls && key === player1.controls.right.toLowerCase()) { 
        player1.moveRight = isKeyDown; 
    } 
    if (player2.controls && key === player2.controls.up.toLowerCase()) { 
        player2.moveUp = isKeyDown; 
    } else if (player2.controls && key === player2.controls.left.toLowerCase()) { 
        player2.moveLeft = isKeyDown; 
    } else if (player2.controls && key === player2.controls.down.toLowerCase()) { 
        player2.moveDown = isKeyDown; 
    } else if (player2.controls && key === player2.controls.right.toLowerCase()) { 
        player2.moveRight = isKeyDown; 
    } 
} 
// Bucle principal del juego
function gameLoop() {
    if (!gameRunning) {
        return; // Si el juego no está en ejecución, salimos de la función para evitar bucles adicionales
    }
    // Calcula el tiempo transcurrido en segundos
    const currentTime = Date.now();
    elapsedTime = Math.floor((currentTime - startTime) / 1000);

    // Actualiza el estado del juego
    updateGame();

    // Renderiza el juego con el tiempo transcurrido
    renderGame(elapsedTime);

    // Disparar automáticamente si ha pasado el tiempo de la frecuencia de disparo
    if (player1.alive && currentTime - lastFiredPlayer1 > fireRate) {
        player1Projectiles.push(createProjectile(player1));
        lastFiredPlayer1 = currentTime;
    }
    if (player2.alive && currentTime - lastFiredPlayer2 > fireRate) {
        player2Projectiles.push(createProjectile(player2));
        lastFiredPlayer2 = currentTime;
    }

    // Solicitar el siguiente frame de animación
    animationFrameId = requestAnimationFrame(gameLoop);
}

// Función para detectar colisiones de proyectiles con enemigos 
function checkProjectileCollisions(projectiles, enemies) { 
    for (let projectile of projectiles) { 
        for (let enemy of enemies) { 
            if ( 
                enemy.color === 'red' && // Solo verificar colisión con bloques rojos 
                projectile.x < enemy.x + enemy.width && 
                projectile.x + projectile.width > enemy.x && 
                projectile.y < enemy.y + enemy.height && 
                projectile.y + projectile.height > enemy.y 
            ) { 
                // Si hay colisión con un bloque rojo, eliminar el proyectil y el enemigo 
                projectiles.splice(projectiles.indexOf(projectile), 1); 
                enemies.splice(enemies.indexOf(enemy), 1); 
            } 
        } 
    } 
} 
// Función para actualizar el estado del juego 
function updateGame() { 
    moveStars(); 
    updateRedEnemies(); 
    drawRedEnemies(); // Actualizar enemigos rojos 
    updateEnemies(whiteEnemies); 
    checkCollisions([player1, player2], redEnemies); 
    checkCollisions([player1, player2], whiteEnemies); 
    // Dibujar la animación de explosión para cada jugador si es necesario 
    [player1, player2].forEach(player => { 
        if (player.exploding) { 
            drawExplosion(player); 
        } 
    }); 
    // Actualizar la posición de los jugadores si están vivos 
    if (player1.alive) {
        if (player1.moveUp && player1.y > 0) player1.y -= 5; // Aumenta este valor para incrementar la velocidad
        if (player1.moveDown && player1.y < canvas.height - player1.height) player1.y += 5; // Aumenta este valor para incrementar la velocidad
        if (player1.moveLeft && player1.x > 0) player1.x -= 5; // Aumenta este valor para incrementar la velocidad
        if (player1.moveRight && player1.x < canvas.width - player1.width) player1.x += 5; // Aumenta este valor para incrementar la velocidad
    }
    if (player2.alive) {
        if (player2.moveUp && player2.y > 0) player2.y -= 5; // Aumenta este valor para incrementar la velocidad
        if (player2.moveDown && player2.y < canvas.height - player2.height) player2.y += 5; // Aumenta este valor para incrementar la velocidad
        if (player2.moveLeft && player2.x > 0) player2.x -= 5; // Aumenta este valor para incrementar la velocidad
        if (player2.moveRight && player2.x < canvas.width - player2.width) player2.x += 5; // Aumenta este valor para incrementar la velocidad
    }
    // Mover y dibujar proyectiles 
    moveProjectiles(player1Projectiles); 
    moveProjectiles(player2Projectiles); 
    checkProjectileCollisions(player1Projectiles, redEnemies); 
    checkProjectileCollisions(player2Projectiles, redEnemies); 
} 
// Función para dibujar proyectiles 
function drawProjectile(projectile, ctx) { 
    ctx.fillStyle = projectile.color; 
    ctx.fillRect(projectile.x, projectile.y, projectile.width, projectile.height); 
} 
// Función para actualizar la posición de los enemigos rojos 
function updateRedEnemies() { 
    // Actualizar la posición de los enemigos rojos existentes 
    for (let enemy of redEnemies) { 
        enemy.x -= 5; // Velocidad a la que se mueven los enemigos rojos 
        if (enemy.x + enemy.width < 0) { 
            // Si el enemigo sale del canvas, lo reinicias al otro lado 
            enemy.x = canvas.width; 
            enemy.y = Math.random() * canvas.height; 
        } 
    } 
    // Verificar si necesitamos agregar más enemigos rojos 
    if (redEnemies.length < 5) { 
        const newEnemiesCount = 5 - redEnemies.length; 
        const newEnemies = Array(newEnemiesCount).fill().map(createRedEnemy); 
        redEnemies.push(...newEnemies); 
    } 
} 
// Función para dibujar enemigos rojos en el canvas 
function drawRedEnemies() { 
    redEnemies.forEach(enemy => drawEnemy(enemy, ctx)); 
} 
// Función para crear proyectiles 
function createProjectile(player) { 
    return { 
        x: player.x + player.width, 
        y: player.y + player.height / 2, 
        width: 10, 
        height: 4, 
        color: 'yellow' 
    }; 
} 
// Función para mover proyectiles 
function moveProjectiles(projectiles) { 
    for (let projectile of projectiles) { 
        projectile.x += 10; // Velocidad del proyectil 
        if (projectile.x > canvas.width) { 
            projectiles.splice(projectiles.indexOf(projectile), 1); // Eliminar proyectil si sale del canvas 
        } 
    } 
} 
// Función para renderizar el juego 
function renderGame() { 
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpiar el canvas 
    drawStars(ctx); 
    drawRedEnemies(); // Dibujar enemigos rojos 
    drawTime(ctx, elapsedTime); // Añade esta línea para dibujar el tiempo 
    whiteEnemies.forEach(enemy => drawEnemy(enemy, ctx)); 
    drawShip(player1, ctx); 
    drawShip(player2, ctx); 
    player1Projectiles.forEach(projectile => drawProjectile(projectile, ctx)); 
    player2Projectiles.forEach(projectile => drawProjectile(projectile, ctx)); 
} 
// Iniciar el juego cuando todo el contenido haya cargado 
window.onload = function() { 
    initGame(); 
    setupRematchButton(); 
};