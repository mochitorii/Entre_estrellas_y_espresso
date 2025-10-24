import pygame
import sys
from juego import bucle_juego
from configuracion import menu_configuracion

ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
GRIS = (180, 180, 180)
AZUL = (100, 149, 237)
NEGRO = (0, 0, 0)

fuente_titulo = pygame.font.Font(None, 90)
fuente_opciones = pygame.font.Font(None, 50)

opciones = ["Iniciar partida", "Configuración", "Salir"]
opcion_seleccionada = 0

def pantalla_inicio(ventana, fondo, titulo_img):
    global opcion_seleccionada
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[opcion_seleccionada] == "Iniciar partida":
                        bucle_juego(ventana)
                    elif opciones[opcion_seleccionada] == "Configuración":
                        menu_configuracion(ventana)
                    elif opciones[opcion_seleccionada] == "Salir":
                        pygame.quit()
                        sys.exit()

        # Fondo
        if fondo:
            ventana.blit(fondo, (0, 0))
        else:
            ventana.fill((20, 20, 40))

        # Título
        if titulo_img:
            titulo_rect = titulo_img.get_rect(center=(ANCHO//2, 180))
            ventana.blit(titulo_img, titulo_rect)
        else:
            texto_titulo = fuente_titulo.render("Café Eclipse ☕", True, AZUL)
            ventana.blit(texto_titulo, (ANCHO//2 - texto_titulo.get_width()//2, 160))

        # Opciones
        for i, opcion in enumerate(opciones):
            color = BLANCO if i == opcion_seleccionada else GRIS
            texto = fuente_opciones.render(opcion, True, color)
            x = ANCHO // 2 - texto.get_width() // 2
            y = 330 + i * 60
            ventana.blit(texto, (x, y))
            if i == opcion_seleccionada:
                pygame.draw.polygon(ventana, AZUL, [
                    (x - 30, y + 20),
                    (x - 10, y + 10),
                    (x - 10, y + 30)
                ])

        pygame.display.flip()
        reloj.tick(60)
 