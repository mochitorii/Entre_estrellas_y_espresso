import pygame
from menu_inicio import pantalla_inicio

pygame.init()

ANCHO, ALTO = 1920, 1080
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Entre Estrellas y Espresso")

try:
    fondo = pygame.image.load("imagenes/fondo_inicio.jpg").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
except:
    fondo = None

try:
    titulo_img = pygame.image.load("imagenes/titulo.png").convert_alpha()
except:
    titulo_img = None
pantalla_inicio(ventana, fondo, titulo_img)

pygame.quit()