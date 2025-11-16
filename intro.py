import pygame
import sys
import math
from juego import bucle_juego

ANCHO, ALTO = 1920, 1080

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

try:
    fuente_texto = pygame.font.Font("fuentes/Fredoka-VariableFont.ttf", 42)
except:
    fuente_texto = pygame.font.Font(None, 42)


def rect_texto(ventana):
    s = pygame.Surface((ANCHO, 250), pygame.SRCALPHA)
    s.fill((0, 0, 0, 200))
    ventana.blit(s, (0, ALTO - 250))


def escribir_texto(ventana, ctx, texto, velocidad=35):
    rect_texto(ventana)

    x = 100
    y = ALTO - 200

    acumulado = ""
    reloj = pygame.time.Clock()

    for letra in texto:
        acumulado += letra

        ventana.blit(ctx["fondo_actual"], (0, 0))

        if ctx["sprite_miel"]:
            ventana.blit(ctx["sprite_miel"], ctx["pos_miel"])

        rect_texto(ventana)

        render = fuente_texto.render(acumulado, True, BLANCO)
        ventana.blit(render, (x, y))

        mostrar_indicador(ventana)
        pygame.display.update()
        reloj.tick(velocidad)

    esperar_espacio(ventana, ctx)


def mostrar_indicador(ventana):
    texto = fuente_texto.render("Presiona ESPACIO para continuar", True, BLANCO)
    t = pygame.time.get_ticks() / 300
    alpha = int((1 + math.sin(t)) * 127)

    surf = texto.copy()
    surf.set_alpha(alpha)
    ventana.blit(surf, (ANCHO - surf.get_width() - 60, ALTO - 60))


def esperar_espacio(ventana, ctx):
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return

        ventana.blit(ctx["fondo_actual"], (0, 0))

        if ctx["sprite_miel"]:
            ventana.blit(ctx["sprite_miel"], ctx["pos_miel"])

        rect_texto(ventana)
        mostrar_indicador(ventana)

        pygame.display.update()
        reloj.tick(60)


def cargar_sprite_proporcional(ruta, alto_deseado=700):
    img = pygame.image.load(ruta).convert_alpha()
    w, h = img.get_size()
    factor = alto_deseado / h
    return pygame.transform.scale(img, (int(w * factor), int(h * factor)))


def intro_del_juego(ventana, ctx):
    """ctx = { fondo_actual, sprite_miel, pos_miel }"""

    ventana.blit(ctx["fondo_actual"], (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)

    escribir_texto(
        ventana, ctx, "Tras meses de trabajo lo logré... pude instalar mi propia cafetería, aunque no fue nada fácil.", velocidad=25)

    try:
        miel_sorp = cargar_sprite_proporcional("imagenes/miel_sorprendida.png")
        miel_habla = cargar_sprite_proporcional("imagenes/miel_hablando.png")
    except:
        miel_sorp = miel_habla = None

    escribir_texto(
        ventana, ctx, "¡Ah pero qué agotamiento!", velocidad=25)

    ctx["sprite_miel"] = miel_sorp
    escribir_texto(
        ventana, ctx, "¿Ah, y esto? ¿Por fin abrirán el local?", velocidad=25)
    
    ctx["sprite_miel"] = miel_habla
    escribir_texto(
        ventana, ctx, "¿Eres tú el dueño de este local?", velocidad=25)

    opcion = elegir_si_no(ventana, ctx)

    if opcion == 0:
        escribir_texto(ventana, ctx, "Sí, este es mi local.", velocidad=25)
    else:
        escribir_texto(ventana, ctx, "No... ni siquiera sabía que se iba a instalar.", velocidad=25)

    bucle_juego(ventana)


def elegir_si_no(ventana, ctx):
    opciones = ["Sí", "No"]
    seleccion = 0
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % 2
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % 2
                if evento.key == pygame.K_RETURN:
                    return seleccion

        ventana.blit(ctx["fondo_actual"], (0, 0))

        if ctx["sprite_miel"]:
            ventana.blit(ctx["sprite_miel"], ctx["pos_miel"])

        rect_texto(ventana)
        mostrar_indicador(ventana)

        for i, op in enumerate(opciones):
            color = (200, 200, 255) if i == seleccion else BLANCO
            render = fuente_texto.render(op, True, color)
            ventana.blit(render, (120, ALTO - 250 + i * 60))

        pygame.display.update()
        reloj.tick(60)