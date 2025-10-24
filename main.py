import pygame
from menu_inicio import pantalla_inicio

pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Café Eclipse ☕")

# Cargar imágenes
try:
    fondo = pygame.image.load("assets/fondo_inicio.jpg").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
except:
    fondo = None

try:
    titulo_img = pygame.image.load("assets/titulo.png").convert_alpha()
except:
    titulo_img = None

# Iniciar el juego
pantalla_inicio(ventana, fondo, titulo_img)
