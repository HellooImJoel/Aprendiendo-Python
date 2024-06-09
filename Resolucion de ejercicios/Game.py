# platformer_game.py

import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataformas")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Clases
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.velocidad_y = 0

    def update(self):
        self.velocidad_y += 1  # Gravedad
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5
        if teclas[pygame.K_SPACE]:
            self.saltar()

        # Actualizar posición vertical
        self.rect.y += self.velocidad_y

        # Limitar movimiento del jugador dentro de la pantalla
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            self.velocidad_y = 0

    def saltar(self):
        # Solo puede saltar si está en el suelo
        if self.rect.bottom >= ALTO:
            self.velocidad_y = -20

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()

# Crear el jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Crear plataformas
plataforma_suelo = Plataforma(0, ALTO - 40, ANCHO, 40)
plataformas.add(plataforma_suelo)
todos_los_sprites.add(plataforma_suelo)

# Bucle principal del juego
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar
    todos_los_sprites.update()

    # Comprobar colisiones
    if pygame.sprite.spritecollide(jugador, plataformas, False):
        jugador.rect.bottom = plataforma_suelo.rect.top
        jugador.velocidad_y = 0

    # Dibujar / Renderizar
    PANTALLA.fill(BLANCO)
    todos_los_sprites.draw(PANTALLA)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(60)

pygame.quit()
sys.exit()
