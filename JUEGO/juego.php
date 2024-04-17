<?php
require 'pygame.php';
require 'random.php';

// Inicialización de Pygame
pygame_init();

// Configuración de la pantalla
$pantalla_ancho = 800;
$pantalla_alto = 600;
$pantalla = pygame_display_set_mode([$pantalla_ancho, $pantalla_alto]);
pygame_display_set_caption('Juego Espacial');

// Colores
$NEGRO = [0, 0, 0];
$BLANCO = [255, 255, 255];
$ROJO = [255, 0, 0];
$AZUL = [0, 0, 255];
$VERDE = [0, 255, 0];

$velocidad_estrellas = 0.1;  // Más bajo es más lento
$contador_estrellas = 0;

// Lista para almacenar las estrellas
$estrellas = [];

// Clases y Funciones

class Explosion extends pygame_sprite_Sprite {
    function __construct($center) {
        parent::__construct();
        $this->images = [];  // Lista para almacenar las imágenes de la animación
        $this->index = 0;  // Índice de la imagen actual
        $this->counter = 0;  // Contador para controlar la velocidad de la animación

        // Cargar imágenes
        for ($i = 0; $i < 9; $i++) {
            $img = pygame_image_load("explosion$i.png")->convert_alpha();  // Asegúrate de tener imágenes de explosión numeradas del 0 al 8
            pygame_image_set_colorkey($img, $NEGRO);  // Establecer color transparente si es necesario
            array_push($this->images, $img);
        }
        
        $this->image = $this->images[$this->index];
        $this->rect = $this->image->get_rect(center=$center);
    }
        
    function update() {
        $this->counter += 1;
        if ($this->counter >= 3) {  // Controlar la velocidad de la animación
            $this->index += 1;
            if ($this->index >= count($this->images)) {
                $this->kill();  // Eliminar la animación una vez que termine
            } else {
                $this->image = $this->images[$this->index];
            }
            $this->counter = 0;
        }
    }
}

class Nave extends pygame_sprite_Sprite {
    function __construct($color, $controles, $x, $y) {
        parent::__construct();
        $this->image = pygame_Surface([20, 20], pygame_SRCALPHA);
        $this->color = $color;
        $this->controles = $controles;
        $this->viva = True;
        // Dibujar un triángulo horizontal
        $puntos = [[0, 10], [20, 0], [20, 20]];
        pygame_draw_polygon($this->image, $this->color, $puntos);
        $this->rect = $this->image->get_rect(center=[$x, $y]);
    }

    function update() {
        $keys = pygame_key_get_pressed();
        if ($this->controles == 'WASD') {
            if ($keys[pygame_K_w] && $this->rect->top > 0) {
                $this->rect->y -= 5;
            }
            if ($keys[pygame_K_s] && $this->rect->bottom < $pantalla_alto) {
                $this->rect->y += 5;
            }
            if ($keys[pygame_K_a] && $this->rect->left > 0) {
                $this->rect->x -= 5;
            }
            if ($keys[pygame_K_d] && $this->rect->right < $pantalla_ancho) {
                $this->rect->x += 5;
            }
        } else {
            if ($keys[pygame_K_UP] && $this->rect->top > 0) {
                $this->rect->y -= 5;
            }
            if ($keys[pygame_K_DOWN] && $this->rect->bottom < $pantalla_alto) {
                $this->rect->y += 5;
            }
            if ($keys[pygame_K_LEFT] && $this->rect->left > 0) {
                $this->rect->x -= 5;
            }
            if ($keys[pygame_K_RIGHT] && $this->rect->right < $pantalla_ancho) {
                $this->rect->x += 5;
            }
        }
    }
}

class Proyectil extends pygame_sprite_Sprite {
    function __construct($x, $y) {
        parent::__construct();
        $this->image = pygame_Surface([10, 4]);
        pygame_fill($this->image, $BLANCO);
        $this->rect = $this->image->get_rect();
        $this->rect->center = [$x, $y];
    }

    function update() {
        $this->rect->x += 10;  // Velocidad del proyectil horizontal
        if ($this->rect->left > $pantalla_ancho) {
            $this->kill();  // Eliminar el proyectil si sale de la pantalla
        }
    }
}

class ObjetoExplotable extends pygame_sprite_Sprite {
    function __construct() {
        parent::__construct();
        $this->image = pygame_Surface([20, 20]);
        pygame_fill($this->image, $ROJO);
        $this->rect = $this->image->get_rect();
        $this->rect->x = $pantalla_ancho;
        $this->rect->y = random_randint(0, $pantalla_alto);
    }

    function update() {
        $this->rect->x -= 5;
        if ($this->rect->right < 0) {
            $this->kill();
        }
    }
}

class Obstaculo extends pygame_sprite_Sprite {
    function __construct() {
        parent::__construct();
        $this->image = pygame_Surface([20, 20]);
        pygame_fill($this->image, $BLANCO);
        $this->rect = $this->image->get_rect();
        $this->rect->x = $pantalla_ancho;
        $this->rect->y = random_randint(0, $pantalla_alto);
    }

    function update() {
        $this->rect->x -= 5;
        if ($this->rect->right < 0) {
            $this->kill();
        }
    }
}

class Objeto extends pygame_sprite_Sprite {
    function __construct($color, $tipo, $x, $y) {
        parent::__construct();
        $this->image = pygame_Surface([20, 20], pygame_SRCALPHA);
        pygame_fill($this->image, [0, 0, 0, 0]);  // Fondo transparente
        if ($tipo == 'triangulo') {
            $puntos = [[0, 0], [20, 10], [0, 20]];
            pygame_draw_polygon($this->image, $color, $puntos);
        } else {
            pygame_draw_rect($this->image, $color, [0, 0, 20, 20], 1);
        }
        $this->rect = $this->image->get_rect();
        $this->rect->center = [$x, $y];
        $this->tipo = $tipo;
    }

    function update() {
        $this->rect->x -= 5;
        if ($this->rect->right < 0) {
            $this->rect->left = $pantalla_ancho;
            $this->rect->y = random_randrange($pantalla_alto);
        }
    }
}

function reiniciar_juego() {
    global $juego_terminado, $todos_los_sprites, $proyectiles, $objetos_explotables, $obstaculos, $nave_jugador1, $nave_jugador2, $tiempo_inicio_jugador1, $tiempo_inicio_jugador2, $puntuacion_jugador1, $puntuacion_jugador2;
    $juego_terminado = False;
    $todos_los_sprites->empty();
    $proyectiles->empty();
    $objetos_explotables->empty();
    $obstaculos->empty();

    // Reiniciar posiciones de las naves
    $nave_jugador1 = new Nave($AZUL, 'WASD', $pantalla_ancho / 2, $pantalla_alto - 50);
    $nave_jugador2 = new Nave($VERDE, 'FLECHAS', $pantalla_ancho / 3, $pantalla_alto - 50);
    $todos_los_sprites->add($nave_jugador1, $nave_jugador2);

    // Reiniciar temporizadores
    $tiempo_ultimo_disparo = pygame_time_get_ticks();
    $tiempo_ultimo_objeto = pygame_time_get_ticks();
    // Reiniciar tiempos y puntuaciones
    $tiempo_inicio_jugador1 = pygame_time_get_ticks();
    $tiempo_inicio_jugador2 = pygame_time_get_ticks();
    $puntuacion_jugador1 = 0;
    $puntuacion_jugador2 = 0;
}

// Grupos de Sprites
$todos_los_sprites = new pygame_sprite_Group();
$objetos_destructibles = new pygame_sprite_Group();
$objetos_indestructibles = new pygame_sprite_Group();
$proyectiles = new pygame_sprite_Group();
$objetos_explotables = new pygame_sprite_Group();
$obstaculos = new pygame_sprite_Group();

// Creación de Naves
$nave_jugador1 = new Nave($AZUL, 'WASD', $pantalla_ancho / 2, $pantalla_alto - 50);
$nave_jugador2 = new Nave($VERDE, 'FLECHAS', $pantalla_ancho / 3, $pantalla_alto - 50);
$todos_los_sprites->add($nave_jugador1, $nave_jugador2);
// Estado del Juego
$juego_terminado = False;

// Tiempos de inicio para cada jugador
$tiempo_inicio_jugador1 = pygame_time_get_ticks();
$tiempo_inicio_jugador2 = pygame_time_get_ticks();

// Puntuaciones (tiempos de supervivencia) para cada jugador
$puntuacion_jugador1 = 0;
$puntuacion_jugador2 = 0;

// Temporizador para controlar la frecuencia de disparo
$tiempo_ultimo_disparo = pygame_time_get_ticks();
$frecuencia_disparo = 500;  // Milisegundos entre disparos

// Temporizador para controlar la generación de objetos y obstáculos
$tiempo_ultimo_objeto = pygame_time_get_ticks();
$frecuencia_objetos = 2000;  // Milisegundos entre la generación de nuevos objetos

// Función para inicializar estrellas
function iniciar_estrellas($num_estrellas) {
    global $estrellas, $pantalla_ancho, $pantalla_alto;
    for ($i = 0; $i < $num_estrellas; $i++) {
        $x = random_randint(0, $pantalla_ancho);
        $y = random_randint(0, $pantalla_alto);
        $velocidad = random_choice([-1.9, -1.5, -1.15]);  // Velocidades negativas para moverse hacia la izquierda
        array_push($estrellas, [$x, $y, $velocidad]);
    }
}

// Inicializar un número menor de estrellas para un efecto más natural
iniciar_estrellas(30);

// Bucle del Juego
$corriendo = True;
while ($corriendo) {
    $tiempo_actual = pygame_time_get_ticks();
    $eventos = pygame_event_get();
    foreach ($eventos as $evento) {
        if ($evento->type == pygame_QUIT) {
            $corriendo = False;
        }
    }

    if (!$juego_terminado) {
        $todos_los_sprites->update();
    }

    pygame_fill($pantalla, $NEGRO);
    foreach ($estrellas as $estrella) {
        $estrella[0] += $estrella[2];  // Mover estrella horizontalmente a su velocidad
        if ($estrella[0] < 0) {
            $estrella[0] = $pantalla_ancho;  // Reiniciar posición en el borde derecho
            $estrella[1] = random_randint(0, $pantalla_alto);  // Nueva posición y aleatoria
        }
        pygame_draw_circle($pantalla, $BLANCO, [int($estrella[0]), $estrella[1]], 1);
    }
    
    $explosion = new Explosion($nave_jugador1->rect->center);  // Crear una explosión en el centro de la nave
    $todos_los_sprites->add($explosion);
    $explosion = new Explosion($nave_jugador2->rect->center);  // Crear una explosión en el centro de la nave
    $todos_los_sprites->add($explosion);

    // Disparar proyectiles con control de tiempo solo si las naves están vivas
    if ($tiempo_actual - $tiempo_ultimo_disparo > $frecuencia_disparo) {
        if ($nave_jugador1->alive()) {
            $proyectil_jugador1 = new Proyectil($nave_jugador1->rect->right, $nave_jugador1->rect->centery);
            $todos_los_sprites->add($proyectil_jugador1);
            $proyectiles->add($proyectil_jugador1);
        }
        if ($nave_jugador2->alive()) {
            $proyectil_jugador2 = new Proyectil($nave_jugador2->rect->right, $nave_jugador2->rect->centery);
            $todos_los_sprites->add($proyectil_jugador2);
            $proyectiles->add($proyectil_jugador2);
        }
        $tiempo_ultimo_disparo = $tiempo_actual;
    }

    // Generar objetos y obstáculos con control de tiempo
    if ($tiempo_actual - $tiempo_ultimo_objeto > $frecuencia_objetos) {
        $nuevo_objeto_explotable = new ObjetoExplotable();
        $nuevo_obstaculo = new Obstaculo();
        $todos_los_sprites->add($nuevo_objeto_explotable, $nuevo_obstaculo);
        $objetos_explotables->add($nuevo_objeto_explotable);
        $obstaculos->add($nuevo_obstaculo);
        $tiempo_ultimo_objeto = $tiempo_actual;
    }

    $todos_los_sprites->draw($pantalla);
    
    $colisiones_explotables = pygame_sprite_groupcollide($proyectiles, $objetos_explotables, True, True);
    $colisiones_obstaculos = pygame_sprite_spritecollide($nave_jugador1, $obstaculos, False) || pygame_sprite_spritecollide($nave_jugador2, $obstaculos, False);
    if ($colisiones_obstaculos) {
        // Aquí puedes manejar lo que sucede cuando una nave colisiona con un obstáculo
        if (pygame_sprite_spritecollide($nave_jugador1, $obstaculos, False)) {
            $nave_jugador1->kill();
        }
        if (pygame_sprite_spritecollide($nave_jugador2, $obstaculos, False)) {
            $nave_jugador2->kill();
        }
        
        // Actualizar puntuaciones si las naves están vivas
        if ($nave_jugador1->alive()) {
            $puntuacion_jugador1 = $tiempo_actual - $tiempo_inicio_jugador1;
        } else {
            // Detener el tiempo cuando la nave del jugador 1 es destruida
            if ($puntuacion_jugador1 == 0) {
                $puntuacion_jugador1 = $tiempo_actual - $tiempo_inicio_jugador1;
            }
        }

        if ($nave_jugador2->alive()) {
            $puntuacion_jugador2 = $tiempo_actual - $tiempo_inicio_jugador2;
        } else {
            // Detener el tiempo cuando la nave del jugador 2 es destruida
            if ($puntuacion_jugador2 == 0) {
                $puntuacion_jugador2 = $tiempo_actual - $tiempo_inicio_jugador2;
            }
        }
    }

    // Verificar si ambas naves han sido destruidas
    if (!$nave_jugador1->alive() && !$nave_jugador2->alive()) {
        $juego_terminado = True;
    }

    // Dibujar en la pantalla
    if ($juego_terminado) {
        // Mostrar mensaje de Game Over
        $fuente = pygame_font_SysFont('Arial', 36);
        $texto_game_over = $fuente->render('GAME OVER', True, $BLANCO);
        $texto_puntuacion_jugador1 = $fuente->render('Tiempo Jugador 1: ' . $puntuacion_jugador1 // 1000 . ' segundos', True, $BLANCO);
        $texto_puntuacion_jugador2 = $fuente->render('Tiempo Jugador 2: ' . $puntuacion_jugador2 // 1000 . ' segundos', True, $BLANCO);
        $texto_revancha = $fuente->render('Revancha?', True, $BLANCO);
        $rect_texto_revancha = $texto_revancha->get_rect(center=[$pantalla_ancho // 2, $pantalla_alto // 2 + 50]);
        pygame_blit($pantalla, $texto_game_over, [$pantalla_ancho // 2 - $texto_game_over->get_width() // 2, $pantalla_alto // 2 - $texto_game_over->get_height() // 2]);
        pygame_blit($pantalla, $texto_puntuacion_jugador1, [$pantalla_ancho // 2 - $texto_puntuacion_jugador1->get_width() // 2, $pantalla_alto // 2 + $texto_game_over->get_height()]);
        pygame_blit($pantalla, $texto_puntuacion_jugador2, [$pantalla_ancho // 2 - $texto_puntuacion_jugador2->get_width() // 2, $pantalla_alto // 2 + $texto_game_over->get_height() * 2]);
        pygame_blit($pantalla, $texto_revancha, $rect_texto_revancha->topleft);

        // Cambiar el color del texto a rojo cuando el mouse está encima
        $mouse_pos = pygame_mouse_get_pos();
        if ($rect_texto_revancha->collidepoint($mouse_pos)) {
            $texto_revancha = $fuente->render('Revancha?', True, $ROJO);
            pygame_blit($pantalla, $texto_revancha, $rect_texto_revancha->topleft);
        }
    } else {
        $todos_los_sprites->draw($pantalla);
    }

    // Actualizar la pantalla
    pygame_display_flip();

    // Reiniciar el juego si se selecciona la opción de revancha
    $eventos = pygame_event_get();
    foreach ($eventos as $evento) {
        if ($evento->type == pygame_MOUSEBUTTONDOWN && $juego_terminado) {
            $pos = pygame_mouse_get_pos();
            if ($texto_revancha->get_rect(topleft=[$pantalla_ancho // 2 - $texto_revancha->get_width() // 2, $pantalla_alto // 2 + $texto_game_over->get_height()])->collidepoint($pos)) {
                reiniciar_juego();
            }
        }
    }

    // Control de FPS
    pygame_time_Clock()->tick(60);
}

pygame_quit();
?>

