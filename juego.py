import pygame
import sys

NEGRO = (0, 0, 0)

def bucle_juego(ventana):
    fuente = pygame.font.Font(None, 50)
    jugando = True
    reloj = pygame.time.Clock()

    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                jugando = False 

        ventana.fill((200, 200, 255))
        ANCHO, ALTO = ventana.get_size()
        texto = fuente.render("Aquí va el juego  (ESC para volver)", True, NEGRO)
        ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2))
        pygame.display.flip()
        reloj.tick(60)