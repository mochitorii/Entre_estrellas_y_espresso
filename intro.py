import pygame
import sys
import time
from juego import bucle_juego

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

try:
    fuente_texto = pygame.font.Font("fuentes/Fredoka-VariableFont.ttf", 32)
except:
    fuente_texto = pygame.font.Font(None, 32)

def intro_del_juego(ventana, fondo=None):
    ANCHO, ALTO = ventana.get_size()

    if fondo is None:
        fondo = pygame.Surface((ANCHO, ALTO))
        fondo.fill((50, 50, 80))

    try:
        miel_img_normal = pygame.image.load("imagenes/miel_normal.png").convert_alpha()
        miel_img_sorprendida = pygame.image.load("imagenes/miel_sorprendida.png").convert_alpha()
    except:
        miel_img_normal = pygame.Surface((150,300))
        miel_img_normal.fill((200,200,255))
        miel_img_sorprendida = miel_img_normal.copy()

    ventana.blit(fondo, (0,0))
    pygame.display.flip()
    pygame.time.delay(5000)

    mostrar_texto_letra_por_letra(ventana, fondo, 
        "Tras meses de trabajo lo logré, pude instalar mi propia cafetería, aunque no fue nada fácil.", 
        (ANCHO//2, int(ALTO*0.8)), centrado=True)

    pygame.time.delay(3000)
    indicador_espacio(ventana, fondo)
    esperar_espacio()

    mostrar_texto_letra_por_letra(ventana, fondo, 
        "¡Ah, pero que agotamiento!", 
        (ANCHO//2, int(ALTO*0.8)), centrado=True)
    pygame.time.delay(500)

    ventana.blit(fondo, (0,0))
    ventana.blit(miel_img_sorprendida, (ANCHO-400, ALTO-400))
    pygame.display.flip()
    pygame.time.delay(500)

    mostrar_texto_letra_por_letra(ventana, fondo, 
        "Ah, ¿y esto? Por fin abrirán el local?", 
        (ANCHO//2, int(ALTO*0.8)), centrado=True)
    mostrar_texto_letra_por_letra(ventana, fondo, 
        "¿Eres tú el dueño de este local?", 
        (ANCHO//2, int(ALTO*0.85)), centrado=True)
    
    opciones = ["Sí, este es mi local", "No, ni siquiera sabía que se iba a instalar"]
    seleccion = 0
    reloj = pygame.time.Clock()
    elegir = True

    while elegir:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    ventana.blit(fondo, (0,0))
                    ventana.blit(miel_img_sorprendida, (ANCHO-400, ALTO-400))
                    mostrar_texto_letra_por_letra(ventana, fondo, opciones[seleccion], (ANCHO//2, int(ALTO*0.8)), centrado=True)
                    pygame.time.delay(1000)
                    elegir = False
                    break

        ventana.blit(fondo, (0,0))
        ventana.blit(miel_img_sorprendida, (ANCHO-400, ALTO-400))

        for i, opcion in enumerate(opciones):
            color = (200,200,255) if i == seleccion else BLANCO
            render = fuente_texto.render(opcion, True, color)
            ventana.blit(render, (ANCHO//2 - render.get_width()//2, int(ALTO*0.7)+i*40))

        pygame.display.flip()
        reloj.tick(60)

    bucle_juego(ventana)

def mostrar_texto_letra_por_letra(ventana, fondo, texto, pos, centrado=False, velocidad=30):
    render = fuente_texto.render("", True, BLANCO)
    texto_actual = ""
    reloj = pygame.time.Clock()
    for letra in texto:
        texto_actual += letra
        ventana.blit(fondo, (0,0))
        render = fuente_texto.render(texto_actual, True, BLANCO)
        x, y = pos
        if centrado:
            x = x - render.get_width()//2
        ventana.blit(render, (x,y))
        pygame.display.flip()
        reloj.tick(velocidad)

def indicador_espacio(ventana, fondo):
    ANCHO, ALTO = ventana.get_size()
    render = fuente_texto.render("Presiona ESPACIO para continuar", True, BLANCO)
    ventana.blit(fondo, (0,0))
    ventana.blit(render, (ANCHO//2 - render.get_width()//2, int(ALTO*0.9)))
    pygame.display.flip()

def esperar_espacio():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False