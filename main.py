import pygame
pygame.init()

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
    nuevo_ancho = 450
    nuevo_alto = int(450 * (titulo_img.get_height() / titulo_img.get_width()))
    titulo_img = pygame.transform.smoothscale(titulo_img, (nuevo_ancho, nuevo_alto))

except:
    titulo_img = None
pantalla_inicio(ventana, fondo, titulo_img)

pygame.quit()