import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
pantalla_ancho = 800
pantalla_alto = 600
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption('Juego Espacial')

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

velocidad_estrellas = 0.1  # Más bajo es más lento
contador_estrellas = 0

# Lista para almacenar las estrellas
estrellas = []

# Clases y Funciones

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.images = []  # Lista para almacenar las imágenes de la animación
        self.index = 0  # Índice de la imagen actual
        self.counter = 0  # Contador para controlar la velocidad de la animación

        # Cargar imágenes
        for i in range(9):
            img = pygame.image.load(f'explosion{i}.png').convert_alpha()  # Asegúrate de tener imágenes de explosión numeradas del 0 al 8
            img.set_colorkey(NEGRO)  # Establecer color transparente si es necesario
            self.images.append(img)
            
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=center)
            
        def update(self):
            self.counter += 1
        if self.counter >= 3:  # Controlar la velocidad de la animación
            self.index += 1
            if self.index >= len(self.images):
                self.kill()  # Eliminar la animación una vez que termine
            else:
                self.image = self.images[self.index]
            self.counter = 0
class Nave(pygame.sprite.Sprite):
    def __init__(self, color, controles, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20], pygame.SRCALPHA)
        self.color = color
        self.controles = controles
        self.viva = True 
        # Dibujar un triángulo horizontal
        puntos = [(0, 10), (20, 0), (20, 20)]
        pygame.draw.polygon(self.image, self.color, puntos)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if self.controles == 'WASD':
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= 5
            if keys[pygame.K_s] and self.rect.bottom < pantalla_alto:
                self.rect.y += 5
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= 5
            if keys[pygame.K_d] and self.rect.right < pantalla_ancho:
                self.rect.x += 5
        else:
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= 5
            if keys[pygame.K_DOWN] and self.rect.bottom < pantalla_alto:
                self.rect.y += 5
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT] and self.rect.right < pantalla_ancho:
                self.rect.x += 5

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 4])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += 10  # Velocidad del proyectil horizontal
        if self.rect.left > pantalla_ancho:
            self.kill()  # Eliminar el proyectil si sale de la pantalla
class ObjetoExplotable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pantalla_ancho
        self.rect.y = random.randint(0, pantalla_alto)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pantalla_ancho
        self.rect.y = random.randint(0, pantalla_alto)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()            

class Objeto(pygame.sprite.Sprite):
    def __init__(self, color, tipo, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20], pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Fondo transparente
        pygame.draw.polygon(self.image, color, [(0, 0), (20, 10), (0, 20)]) if tipo == 'triangulo' else pygame.draw.rect(self.image, color, [0, 0, 20, 20], 1)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.tipo = tipo

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = pantalla_ancho
            self.rect.y = random.randrange(pantalla_alto)


def reiniciar_juego():
    global juego_terminado, todos_los_sprites, proyectiles, objetos_explotables, obstaculos, nave_jugador1, nave_jugador2, tiempo_inicio_jugador1, tiempo_inicio_jugador2, puntuacion_jugador1, puntuacion_jugador2
    juego_terminado = False
    todos_los_sprites.empty()
    proyectiles.empty()
    objetos_explotables.empty()
    obstaculos.empty()

    # Reiniciar posiciones de las naves
    nave_jugador1 = Nave(AZUL, 'WASD', pantalla_ancho / 2, pantalla_alto - 50)
    nave_jugador2 = Nave(VERDE, 'FLECHAS', pantalla_ancho / 3, pantalla_alto - 50)
    todos_los_sprites.add(nave_jugador1, nave_jugador2)

    # Reiniciar temporizadores
    tiempo_ultimo_disparo = pygame.time.get_ticks()
    tiempo_ultimo_objeto = pygame.time.get_ticks()
    # Reiniciar tiempos y puntuaciones
    tiempo_inicio_jugador1 = pygame.time.get_ticks()
    tiempo_inicio_jugador2 = pygame.time.get_ticks()
    puntuacion_jugador1 = 0
    puntuacion_jugador2 = 0
    
# Grupos de Sprites
todos_los_sprites = pygame.sprite.Group()
objetos_destructibles = pygame.sprite.Group()
objetos_indestructibles = pygame.sprite.Group()
proyectiles = pygame.sprite.Group()
objetos_explotables = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

# Creación de Naves
nave_jugador1 = Nave(AZUL, 'WASD', pantalla_ancho / 2, pantalla_alto - 50)
nave_jugador2 = Nave(VERDE, 'FLECHAS', pantalla_ancho / 3, pantalla_alto - 50)
todos_los_sprites.add(nave_jugador1, nave_jugador2)
# Estado del Juego
juego_terminado = False

# Tiempos de inicio para cada jugador
tiempo_inicio_jugador1 = pygame.time.get_ticks()
tiempo_inicio_jugador2 = pygame.time.get_ticks()

# Puntuaciones (tiempos de supervivencia) para cada jugador
puntuacion_jugador1 = 0
puntuacion_jugador2 = 0

# Temporizador para controlar la frecuencia de disparo
tiempo_ultimo_disparo = pygame.time.get_ticks()
frecuencia_disparo = 500  # Milisegundos entre disparos

# Temporizador para controlar la generación de objetos y obstáculos
tiempo_ultimo_objeto = pygame.time.get_ticks()
frecuencia_objetos = 2000  # Milisegundos entre la generación de nuevos objetos
    
# Función para inicializar estrellas
def iniciar_estrellas(num_estrellas):
    for i in range(num_estrellas):
        x = random.randint(0, pantalla_ancho)
        y = random.randint(0, pantalla_alto)    
        velocidad = random.choice([-1.9, -1.5, -1.15])  # Velocidades negativas para moverse hacia la izquierda
        estrellas.append([x, y, velocidad])
        
# Inicializar un número menor de estrellas para un efecto más natural
iniciar_estrellas(30)



# Bucle del Juego
corriendo = True
while corriendo:
    tiempo_actual = pygame.time.get_ticks()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    if not juego_terminado:
        todos_los_sprites.update()

    pantalla.fill(NEGRO)
    for estrella in estrellas:
        estrella[0] += estrella[2]  # Mover estrella horizontalmente a su velocidad
        if estrella[0] < 0:
            estrella[0] = pantalla_ancho  # Reiniciar posición en el borde derecho
            estrella[1] = random.randint(0, pantalla_alto)  # Nueva posición y aleatoria
        pygame.draw.circle(pantalla, BLANCO, (int(estrella[0]), estrella[1]), 1)
        
        explosion = Explosion(nave_jugador1.rect.center)  # Crear una explosión en el centro de la nave
        todos_los_sprites.add(explosion)
        explosion = Explosion(nave_jugador2.rect.center)  # Crear una explosión en el centro de la nave
        todos_los_sprites.add(explosion)

        # Disparar proyectiles con control de tiempo solo si las naves están vivas
        if tiempo_actual - tiempo_ultimo_disparo > frecuencia_disparo:
            if nave_jugador1.alive():
                proyectil_jugador1 = Proyectil(nave_jugador1.rect.right, nave_jugador1.rect.centery)
                todos_los_sprites.add(proyectil_jugador1)
                proyectiles.add(proyectil_jugador1)
            if nave_jugador2.alive():
                proyectil_jugador2 = Proyectil(nave_jugador2.rect.right, nave_jugador2.rect.centery)
                todos_los_sprites.add(proyectil_jugador2)
                proyectiles.add(proyectil_jugador2)
            tiempo_ultimo_disparo = tiempo_actual
        
        # Generar objetos y obstáculos con control de tiempo
    if tiempo_actual - tiempo_ultimo_objeto > frecuencia_objetos:
        nuevo_objeto_explotable = ObjetoExplotable()
        nuevo_obstaculo = Obstaculo()
        todos_los_sprites.add(nuevo_objeto_explotable, nuevo_obstaculo)
        objetos_explotables.add(nuevo_objeto_explotable)
        obstaculos.add(nuevo_obstaculo)
        tiempo_ultimo_objeto = tiempo_actual
    

    todos_los_sprites.draw(pantalla)
    
    colisiones_explotables = pygame.sprite.groupcollide(proyectiles, objetos_explotables, True, True)
    colisiones_obstaculos = pygame.sprite.spritecollide(nave_jugador1, obstaculos, False) or pygame.sprite.spritecollide(nave_jugador2, obstaculos, False)
    if colisiones_obstaculos:
        # Aquí puedes manejar lo que sucede cuando una nave colisiona con un obstáculo
        nave_jugador1.kill() if pygame.sprite.spritecollide(nave_jugador1, obstaculos, False) else None
        nave_jugador2.kill() if pygame.sprite.spritecollide(nave_jugador2, obstaculos, False) else None
        
# Actualizar puntuaciones si las naves están vivas
        if nave_jugador1.alive():
            puntuacion_jugador1 = tiempo_actual - tiempo_inicio_jugador1
        else:
            # Detener el tiempo cuando la nave del jugador 1 es destruida
            if puntuacion_jugador1 == 0:
                puntuacion_jugador1 = tiempo_actual - tiempo_inicio_jugador1

        if nave_jugador2.alive():
            puntuacion_jugador2 = tiempo_actual - tiempo_inicio_jugador2
        else:
            # Detener el tiempo cuando la nave del jugador 2 es destruida
            if puntuacion_jugador2 == 0:
                puntuacion_jugador2 = tiempo_actual - tiempo_inicio_jugador2
        
    # Verificar si ambas naves han sido destruidas
    if not nave_jugador1.alive() and not nave_jugador2.alive():
        juego_terminado = True
        # Dibujar en la pantalla
    if juego_terminado:
        # Mostrar mensaje de Game Over
        fuente = pygame.font.SysFont('Arial', 36)
        texto_game_over = fuente.render('GAME OVER', True, BLANCO)
        texto_puntuacion_jugador1 = fuente.render(f'Tiempo Jugador 1: {puntuacion_jugador1 // 1000} segundos', True, BLANCO)
        texto_puntuacion_jugador2 = fuente.render(f'Tiempo Jugador 2: {puntuacion_jugador2 // 1000} segundos', True, BLANCO)
        texto_revancha = fuente.render('Revancha?', True, BLANCO)
        rect_texto_revancha = texto_revancha.get_rect(center=(pantalla_ancho // 2, pantalla_alto // 2 + 50))
        pantalla.blit(texto_game_over, (pantalla_ancho // 2 - texto_game_over.get_width() // 2, pantalla_alto // 2 - texto_game_over.get_height() // 2))
        pantalla.blit(texto_puntuacion_jugador1, (pantalla_ancho // 2 - texto_puntuacion_jugador1.get_width() // 2, pantalla_alto // 2 + texto_game_over.get_height()))
        pantalla.blit(texto_puntuacion_jugador2, (pantalla_ancho // 2 - texto_puntuacion_jugador2.get_width() // 2, pantalla_alto // 2 + texto_game_over.get_height() * 2))
        pantalla.blit(texto_revancha, rect_texto_revancha.topleft)

        # Cambiar el color del texto a rojo cuando el mouse está encima
        mouse_pos = pygame.mouse.get_pos()
        if rect_texto_revancha.collidepoint(mouse_pos):
            texto_revancha = fuente.render('Revancha?', True, ROJO)
            pantalla.blit(texto_revancha, rect_texto_revancha.topleft)
    else:
        todos_los_sprites.draw(pantalla)


    # Actualizar la pantalla
    pygame.display.flip()
    
    # Reiniciar el juego si se selecciona la opción de revancha
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN and juego_terminado:
            pos = pygame.mouse.get_pos()
            if texto_revancha.get_rect(topleft=(pantalla_ancho // 2 - texto_revancha.get_width() // 2, pantalla_alto // 2 + texto_game_over.get_height())).collidepoint(pos):
                reiniciar_juego()

    # Control de FPS
    pygame.time.Clock().tick(60)

pygame.quit()