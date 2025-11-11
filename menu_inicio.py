import pygame
import sys

def pantalla_inicio(ventana, fondo=None, titulo_img=None):
    fuente_titulo = pygame.font.Font(None, 90)
    fuente_opciones = pygame.font.Font(None, 50)
    reloj = pygame.time.Clock()

    opcion_seleccionada = 0
    opciones = ["Iniciar partida", "Configuración", "Salir"]

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
                        from juego import bucle_juego
                        bucle_juego(ventana)
                    elif opciones[opcion_seleccionada] == "Configuración":
                        from configuracion import menu_configuracion
                        menu_configuracion(ventana)
                    elif opciones[opcion_seleccionada] == "Salir":
                        pygame.quit()
                        sys.exit()

        if fondo:
            ventana.blit(fondo, (0, 0))
        else:
            ventana.fill((20, 20, 40))

        if titulo_img:
            titulo_rect = titulo_img.get_rect(center=(ventana.get_width()//2, 180))
            ventana.blit(titulo_img, titulo_rect)
        else:
            texto_titulo = fuente_titulo.render("Entre Estrellas y Espresso", True, (100, 149, 237))
            ventana.blit(texto_titulo, (ventana.get_width()//2 - texto_titulo.get_width()//2, 160))

        for i, opcion in enumerate(opciones):
            color = (255, 255, 255) if i == opcion_seleccionada else (180, 180, 180)
            texto = fuente_opciones.render(opcion, True, color)
            x = ventana.get_width() // 2 - texto.get_width() // 2
            y = 330 + i * 60
            ventana.blit(texto, (x, y))
            if i == opcion_seleccionada:
                pygame.draw.polygon(ventana, (100, 149, 237), [
                    (x - 30, y + 20),
                    (x - 10, y + 10),
                    (x - 10, y + 30)
                ])

        pygame.display.flip()
        reloj.tick(60)