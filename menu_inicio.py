import pygame
import sys
import math
from configuracion import menu_configuracion
from intro import intro_del_juego

ANCHO, ALTO = 1920, 1080
BLANCO = (255, 255, 255)

try:
    fuente_titulo = pygame.font.Font("fuentes/Fredoka-VariableFont.ttf", 90)
    fuente_opciones = pygame.font.Font("fuentes/Fredoka-VariableFont.ttf", 50)
except:
    fuente_titulo = pygame.font.Font(None, 90)
    fuente_opciones = pygame.font.Font(None, 50)

opciones = ["Iniciar partida", "Configuración", "Salir"]
opcion_seleccionada = 0
tamaño_actual = [50 for _ in opciones]
t = 0
fade = 255

def pantalla_inicio(ventana, fondo=None, titulo_img=None):
    global opcion_seleccionada, t, fade
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
                        intro_del_juego(ventana, fondo)
                    elif opciones[opcion_seleccionada] == "Configuración":
                        menu_configuracion(ventana)
                    elif opciones[opcion_seleccionada] == "Salir":
                        pygame.quit()
                        sys.exit()

        ventana.fill((20, 20, 40))
        if fondo:
            ventana.blit(fondo, (0, 0))

        if titulo_img:
            nuevo_alto = 460
            factor = nuevo_alto / titulo_img.get_height()
            nuevo_ancho = int(titulo_img.get_width() * factor)
            titulo_img_scaled = pygame.transform.smoothscale(
                titulo_img, (nuevo_ancho, nuevo_alto)
            )
            y_logo = ALTO // 2 - nuevo_alto // 2 - 80
            ventana.blit(titulo_img_scaled, (50, y_logo))
        else:
            y_logo = 50

        base_x = 80
        base_y = y_logo + (titulo_img.get_height() if titulo_img else 0) + 20
        separacion = 80

        for i in range(len(opciones)):
            target = 62 if i == opcion_seleccionada else 50
            if tamaño_actual[i] < target:
                tamaño_actual[i] += 2
            elif tamaño_actual[i] > target:
                tamaño_actual[i] -= 2

        t += 0.1
        brillo = int(40 * math.sin(t) + 215)
        color_sel = (brillo, brillo, 255)

        for i, opcion in enumerate(opciones):
            try:
                fuente_tmp = pygame.font.Font("fuentes/Fredoka-VariableFont.ttf", tamaño_actual[i])
            except:
                fuente_tmp = pygame.font.Font(None, tamaño_actual[i])

            sombra = fuente_tmp.render(opcion, True, (0, 0, 0))
            ventana.blit(sombra, (base_x + 3, base_y + i * separacion + 3))

            color = color_sel if i == opcion_seleccionada else BLANCO
            texto = fuente_tmp.render(opcion, True, color)
            ventana.blit(texto, (base_x, base_y + i * separacion))

        if fade > 0:
            overlay = pygame.Surface((ANCHO, ALTO))
            overlay.fill((0, 0, 0))
            overlay.set_alpha(fade)
            ventana.blit(overlay, (0, 0))
            fade -= 2

        pygame.display.flip()
        reloj.tick(60)