import pygame
import sys

BLANCO = (255, 255, 255)
fuente = pygame.font.Font(None, 50)

def menu_configuracion(ventana):
    volver = False
    while not volver:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE or evento.key == pygame.K_RETURN:
                    volver = True

        ventana.fill((30, 30, 50))
        texto = fuente.render("Menú de configuración (ESC para volver)", True, BLANCO)
        ventana.blit(texto, (400 - texto.get_width()//2, 300))
        pygame.display.flip()
