import pygame
import sys

BLANCO = (255, 255, 255)

def menu_configuracion(ventana):
    fuente = pygame.font.Font(None, 50)
    volver = False
    reloj = pygame.time.Clock()

    while not volver:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                    volver = True

        ventana.fill((30, 30, 50))
        ANCHO, ALTO = ventana.get_size()
        texto = fuente.render("Menú de configuración (ESC para volver)", True, BLANCO)
        ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2))
        pygame.display.flip()
        reloj.tick(60)