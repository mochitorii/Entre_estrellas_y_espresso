import pygame
import sys

pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
fuente = pygame.font.Font(None, 50)

def bucle_juego(ventana):
    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                jugando = False  # volver al menú

        ventana.fill((200, 200, 255))
        texto = fuente.render("Aquí va el juego 🎮 (ESC para volver)", True, NEGRO)
        ventana.blit(texto, (400 - texto.get_width()//2, 300))
        pygame.display.flip()
