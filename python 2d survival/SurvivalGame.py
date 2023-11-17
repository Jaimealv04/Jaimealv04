########################################################################
########################################################################
#   Final Practice 'VIDEOJUEGO ALIEN'
#   Module: POO
#   Author: JAM
#   Create date: 17-04-2023
#   Last modification: 08-04-2023
#   Version: 1.0
#   Modified by: Jorge Albert, Carolina Romano, Óscar Haotiang, Jaime
#                Álvarez, Xabier Fernández y Eduardo Salazar
#   Content: Software that contains game 'ALIEN'
########################################################################
########################################################################

import pygame
import botones
from pygame.locals import *
from pygame import mixer
import os
import sys
import random


# Starting library
pygame.init()

# Inicializar la biblioteca pygame.mixer
pygame.mixer.init()

# Cargar la música en una variable
soundtrack = pygame.mixer.Sound("soundtrack_interfaz.wav")

# Reproducir la música
soundtrack.play(loops=-1)
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 149, 0)
red = (232, 5, 5)
orange_light = (246, 209, 112)

# Window size
# (1333, 750) ----- (+587, +330)
size = (1920, 1080)
'''fuente_2 = pygame.font.Font("SFPRODISPLAYREGULAR.OTF", 65)'''

screen = pygame.display.set_mode(size)  # Screen apagada
screen2 = pygame.display.set_mode(size)
screen3 = pygame.display.set_mode(size)
screen4 = pygame.display.set_mode(size)
screen5 = pygame.display.set_mode(size)

# Set the pygame window name and image
pygame.display.set_caption('GALAXIA EN GUERRA')
portada = pygame.image.load('alien_logo.png')
pygame.display.set_icon(portada)

# LOAD IMAGE
# Credits display
bg_credits_image = pygame.image.load("fondo_creditos.png").convert_alpha()
# Front play display
front_page_image = pygame.image.load("portada_videojuego.png").convert_alpha()
# Button start
button_start_image = pygame.image.load("boton_start.png").convert_alpha()
# Button credits
button_credits_image = pygame.image.load("boton_creditos.png").convert_alpha()
# Botón pistola
boton_pistola_imagen = pygame.image.load("boton_pistola.png").convert_alpha()
# Botón volver
boton_volver_imagen = pygame.image.load("boton_volver.png").convert_alpha()


front_page_image2 = pygame.image.load("pantalla_seleccion.png").convert_alpha()

boton_granada_imagen = pygame.image.load("boton_granada.png").convert_alpha()

boton_metralleta_imagen = pygame.image.load("boton_metralleta.png").convert_alpha()

boton_escopeta_imagen = pygame.image.load("boton_escopeta.png").convert_alpha()

boton_cuchillo_imagen = pygame.image.load("boton_cuchillo.png").convert_alpha()

personaje_imagen = pygame.image.load("personaje_principal.png").convert_alpha()

personaje_metralleta_imagen = pygame.image.load("personajeconmetralleta.png").convert_alpha()

caracteristicas_metralleta_imagen = pygame.image.load("caracteristicas_metralleta.png").convert_alpha()

personaje_pistola_imagen = pygame.image.load("personajeconpistola.png").convert_alpha()

caracteristicas_pistola_imagen = pygame.image.load("caracteristicas_pistola.png").convert_alpha()

personaje_escopeta_imagen = pygame.image.load("personajeconescopeta.png").convert_alpha()

caracteristicas_escopeta_imagen = pygame.image.load("caracteristicas_escopeta.png").convert_alpha()

personaje_cuchillo_imagen = pygame.image.load("personajeconcuchillo.png").convert_alpha()

caracteristicas_cuchillo_imagen = pygame.image.load("caracteristicas_cuchillo.png").convert_alpha()

personaje_granada_imagen = pygame.image.load("personajecongranada.png").convert_alpha()

caracteristicas_granada_imagen = pygame.image.load("caracteristicas_granada.png").convert_alpha()

boton_seleccionar_imagen = pygame.image.load("boton_seleccionar.png").convert_alpha()

boton_menu_imagen = pygame.image.load("boton_menu.png").convert_alpha()

def first_window():
    # armas
    metralleta_arm = False
    cuchillo_arm = False
    pistola_arm = False
    granada_arm = False
    escopeta_arm = False
    contador = 0

    # Import button image
    # Button start
    button_start = botones.boton(1000, 100, button_start_image, 0.8)
    # Button credits
    button_credits = botones.boton(0, 750, button_credits_image, 0.3)

    # Bucle principal del programa
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.blit(front_page_image,[0, 0])  # Image on background

            if button_start.draw(screen):
                start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)
            if button_credits.draw(screen):
                credits()

            pygame.display.update()  # Update window

def start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador):

    screen2.fill(white)
    screen2.blit(front_page_image2, [0, 0])  # Image on background
    boton_pistola = botones.boton(30, 240, boton_pistola_imagen, 0.28)
    boton_granada = botones.boton(360, 240, boton_granada_imagen, 0.28)
    boton_metralleta = botones.boton(30, 515, boton_metralleta_imagen, 0.28)
    boton_escopeta = botones.boton(360, 515, boton_escopeta_imagen, 0.28)
    boton_cuchillo = botones.boton(195, 790, boton_cuchillo_imagen, 0.28)


    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen2.blit(front_page_image2, [0, 0])  # Image on background

            if contador == 2:
                pantalla_niveles(pistola_arm, escopeta_arm, metralleta_arm, granada_arm, cuchillo_arm)

            if boton_pistola.draw(screen2):
                pistola(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_granada.draw(screen2):
                granada(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_metralleta.draw(screen2):
                metralleta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_escopeta.draw(screen2):
                escopeta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_cuchillo.draw(screen2):
                cuchillo(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            screen2.blit(personaje_imagen, (850, 200))


def credits():

    screen3.fill(white)
    screen3.blit(bg_credits_image, [0, 0])  # Image on background

    # Button credits
    boton_volver = botones.boton(1350, 750, boton_volver_imagen, 0.3)

    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen3.blit(bg_credits_image, [0, 0])  # Image on background

            if boton_volver.draw(screen):
                first_window()

def pistola(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador):

    screen4.fill(white)
    screen4.blit(front_page_image2, [0, 0])  # Image on background
    boton_pistola = botones.boton(30, 240, boton_pistola_imagen, 0.28)
    boton_granada = botones.boton(360, 240, boton_granada_imagen, 0.28)
    boton_metralleta = botones.boton(30, 515, boton_metralleta_imagen, 0.28)
    boton_escopeta = botones.boton(360, 515, boton_escopeta_imagen, 0.28)
    boton_cuchillo = botones.boton(195, 790, boton_cuchillo_imagen, 0.28)
    boton_caracteristicas = botones.boton(1300,200, caracteristicas_pistola_imagen, 0.8)
    boton_seleccionar = botones.boton(1250,700, boton_seleccionar_imagen, 0.4)


    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen4.blit(front_page_image2, [0, 0])  # Image on background

            if boton_seleccionar.draw(screen4):
                pistola_arm = True
                contador += 1
                start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_pistola.draw(screen4):
                pass

            if boton_granada.draw(screen4):
                granada(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_metralleta.draw(screen4):
                metralleta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_escopeta.draw(screen4):
                escopeta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_cuchillo.draw(screen4):
                cuchillo(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_caracteristicas.draw(screen4):
                pass

            screen4.blit(personaje_pistola_imagen, (850, 200))

def granada(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador):
    screen4.fill(white)
    screen4.blit(front_page_image2, [0, 0])  # Image on background
    boton_pistola = botones.boton(30, 240, boton_pistola_imagen, 0.28)
    boton_granada = botones.boton(360, 240, boton_granada_imagen, 0.28)
    boton_metralleta = botones.boton(30, 515, boton_metralleta_imagen, 0.28)
    boton_escopeta = botones.boton(360, 515, boton_escopeta_imagen, 0.28)
    boton_cuchillo = botones.boton(195, 790, boton_cuchillo_imagen, 0.28)
    boton_caracteristicas = botones.boton(1300,200, caracteristicas_granada_imagen, 0.8)
    boton_seleccionar = botones.boton(1250, 700, boton_seleccionar_imagen, 0.4)

    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen4.blit(front_page_image2, [0, 0])  # Image on background

            if boton_seleccionar.draw(screen4):
                granada_arm = True
                contador += 1
                start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_pistola.draw(screen4):
                pistola(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_granada.draw(screen4):
                pass

            if boton_metralleta.draw(screen4):
                metralleta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_escopeta.draw(screen4):
                escopeta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_cuchillo.draw(screen4):
                cuchillo(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_caracteristicas.draw(screen4):
                pass

            screen4.blit(personaje_granada_imagen, (550, 200))

def metralleta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador):

    screen4.fill(white)
    screen4.blit(front_page_image2, [0, 0])  # Image on background
    boton_pistola = botones.boton(30, 240, boton_pistola_imagen, 0.28)
    boton_granada = botones.boton(360, 240, boton_granada_imagen, 0.28)
    boton_metralleta = botones.boton(30, 515, boton_metralleta_imagen, 0.28)
    boton_escopeta = botones.boton(360, 515, boton_escopeta_imagen, 0.28)
    boton_cuchillo = botones.boton(195, 790, boton_cuchillo_imagen, 0.28)
    boton_caracteristicas = botones.boton(1300,200, caracteristicas_metralleta_imagen, 0.8)
    boton_seleccionar = botones.boton(1250,700, boton_seleccionar_imagen, 0.4)


    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen4.blit(front_page_image2, [0, 0])  # Image on background

            if boton_seleccionar.draw(screen4):
                metralleta_arm = True
                contador += 1
                start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_pistola.draw(screen4):
                pistola(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_granada.draw(screen4):
                granada(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_metralleta.draw(screen4):
                pass

            if boton_escopeta.draw(screen4):
                escopeta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_cuchillo.draw(screen4):
                cuchillo(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_caracteristicas.draw(screen4):
                pass

            screen4.blit(personaje_metralleta_imagen, (750, 200))

def escopeta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador):

    screen4.fill(white)
    screen4.blit(front_page_image2, [0, 0])  # Image on background
    boton_pistola = botones.boton(30, 240, boton_pistola_imagen, 0.28)
    boton_granada = botones.boton(360, 240, boton_granada_imagen, 0.28)
    boton_metralleta = botones.boton(30, 515, boton_metralleta_imagen, 0.28)
    boton_escopeta = botones.boton(360, 515, boton_escopeta_imagen, 0.28)
    boton_cuchillo = botones.boton(195, 790, boton_cuchillo_imagen, 0.28)
    boton_caracteristicas = botones.boton(1300,200, caracteristicas_escopeta_imagen, 0.8)
    boton_seleccionar = botones.boton(1250,700, boton_seleccionar_imagen, 0.4)


    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen4.blit(front_page_image2, [0, 0])  # Image on background

            if boton_seleccionar.draw(screen4):
                escopeta_arm = True
                contador += 1
                start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_pistola.draw(screen4):
                pistola(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_granada.draw(screen4):
                granada(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_metralleta.draw(screen4):
                metralleta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_escopeta.draw(screen4):
                pass

            if boton_cuchillo.draw(screen4):
                cuchillo(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_caracteristicas.draw(screen4):
                pass

            screen4.blit(personaje_escopeta_imagen, (750, 200))

def cuchillo(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador):
    screen4.fill(white)
    screen4.blit(front_page_image2, [0, 0])  # Image on background
    boton_pistola = botones.boton(30, 240, boton_pistola_imagen, 0.28)
    boton_granada = botones.boton(360, 240, boton_granada_imagen, 0.28)
    boton_metralleta = botones.boton(30, 515, boton_metralleta_imagen, 0.28)
    boton_escopeta = botones.boton(360, 515, boton_escopeta_imagen, 0.28)
    boton_cuchillo = botones.boton(195, 790, boton_cuchillo_imagen, 0.28)
    boton_caracteristicas = botones.boton(1300, 200, caracteristicas_cuchillo_imagen, 0.8)
    boton_seleccionar = botones.boton(1250,700, boton_seleccionar_imagen, 0.4)

    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            screen4.blit(front_page_image2, [0, 0])  # Image on background

            if boton_seleccionar.draw(screen4):
                cuchillo_arm = True
                contador += 1
                start(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_pistola.draw(screen4):
                pistola(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_granada.draw(screen4):
                granada(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_metralleta.draw(screen4):
                metralleta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_escopeta.draw(screen4):
                escopeta(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm, contador)

            if boton_cuchillo.draw(screen4):
                pass

            if boton_caracteristicas.draw(screen4):
                pass

            screen4.blit(personaje_cuchillo_imagen, (650, 200))


def nivel2(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm):

    soundtrack.stop()

    color = (0, 0, 0)
    fps = 60
    color2 = (255, 255, 255)

    class Personaje(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.center = (100, SCREEN_HEIGHT // 2)  # donde queremos que se instancie en primer lugar el personaje
            self.energia = 10
            self.velocidad_x = 0
            self.velocidad_y = 0
            self.pistola = False
            self.escopeta = False
            self.granada = False
            self.metralleta = False
            self.cuchillo = False
            self.disparando = False
            self.balasPistola = 15
            self.balasEscopeta = 5
            self.balasMetralleta = 50
            self.cargador = 1
            self.cuchillos = 15
            self.granadas = 2
            self.aliensMuertos = 0

        def update(self):

            # Colisiones
            if pygame.sprite.groupcollide(aliens.aliens, sprites, 1, 0):
                self.energia -= 1

            if pygame.sprite.groupcollide(aliens.aliens, balas, 1, 1):
                self.aliensMuertos += 1

            if self.aliensMuertos == 10:
                victoria()

            self.vida()

            # calavera con contador de aliens
            self.calavera = pygame.image.load("calavera.png")
            self.calavera = pygame.transform.scale(self.calavera, (100, 100))
            screen.blit(self.calavera, (40, 250))
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(str(self.aliensMuertos), True, color2)
            textRect = text.get_rect()
            textRect.center = (160, 310)
            screen.blit(text, textRect)

            # Inventario
            if self.pistola:
                self.pistolaInv = pygame.image.load("Pistolainventario.png").convert()
                self.pistolaInv = pygame.transform.scale(self.pistolaInv, (200, 200))
                screen.blit(self.pistolaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasPistola), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.escopeta:
                self.escopetaInv = pygame.image.load("Escopetainventario.png").convert()
                self.escopetaInv = pygame.transform.scale(self.escopetaInv, (200, 200))
                screen.blit(self.escopetaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasEscopeta), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.cuchillo:
                self.cuchilloInv = pygame.image.load("Cuchilloinventario.png").convert()
                self.cuchilloInv = pygame.transform.scale(self.cuchilloInv, (200, 200))
                screen.blit(self.cuchilloInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.cuchillos), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.metralleta:
                self.metralletaInv = pygame.image.load("Metralletainventario.png").convert()
                self.metralletaInv = pygame.transform.scale(self.metralletaInv, (200, 200))
                screen.blit(self.metralletaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasMetralleta), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.granada:
                self.granadaInv = pygame.image.load("Granadainventario.png").convert()
                self.granadaInv = pygame.transform.scale(self.granadaInv, (200, 200))
                screen.blit(self.granadaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.granadas), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            # velocidad predeterminada
            self.velocidad_x = 0
            self.velocidad_y = 0

            # input de teclas
            teclas = pygame.key.get_pressed()

            # Movimiento
            if teclas[pygame.K_a]:
                self.velocidad_x = -10
            if teclas[pygame.K_d]:
                self.velocidad_x = 10
            if teclas[pygame.K_w]:
                self.velocidad_y = -10
            if teclas[pygame.K_s]:
                self.velocidad_y = 10

                # recargar armas
            if teclas[pygame.K_r] and self.pistola == True and self.cargador > 0:
                self.balasPistola += 7
                self.cargador -= 1

            if teclas[pygame.K_r] and self.metralleta == True and self.cargador > 0:
                self.balasMetralleta += 25
                self.cargador -= 1

            if teclas[pygame.K_r] and self.escopeta == True and self.cargador > 0:
                self.balasEscopeta += 3
                self.cargador -= 1

            if teclas[pygame.K_r] and self.cuchillo == True and self.cargador > 0:
                self.cuchillos += 7
                self.cargador -= 1

            if teclas[pygame.K_r] and self.granada == True and self.cargador > 0:
                self.granadas += 1
                self.cargador -= 1

                # Sacar Armas
            if teclas[pygame.K_1] and pistola_arm == True:
                self.pistola = True
                self.escopeta = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))

            if teclas[pygame.K_2] and escopeta_arm == True:
                self.escopeta = True
                self.pistola = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("MachineGun1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))

            if teclas[pygame.K_3] and metralleta_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = True
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("Metralleta1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            if teclas[pygame.K_4] and cuchillo_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = False
                self.cuchillo = True
                self.granada = False
                self.image = pygame.image.load("Cuchillo1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            if teclas[pygame.K_5] and granada_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = True
                self.image = pygame.image.load("Granada1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            # Actualiza la velocidad del personaje
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

            # Limites de movimiento izquierda derecha
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            # Limites de movimiento arriba, abajo
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0

            self.disparar()

        def disparar(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.pistola == True and self.balasPistola > 0:
                    sound_pistola.play()
                    self.image = pygame.image.load("Handgun2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.balasPistola -= 1
                    jugador.disparoPistola()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.pistola == True:
                    self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.escopeta == True and self.balasEscopeta > 0:
                    sound_escopeta.play()
                    self.image = pygame.image.load("MachineGun2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.balasEscopeta -= 1
                    jugador.disparoEscopeta()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.escopeta == True:
                    self.image = pygame.image.load("MachineGun1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.metralleta == True and self.balasMetralleta > 0:
                    self.image = pygame.image.load("Metralleta2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.balasMetralleta -= 5
                    jugador.disparoMetralleta()
                    sound_metralleta.play()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.metralleta == True:
                    self.image = pygame.image.load("Metralleta1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.cuchillo == True and self.cuchillos > 0:
                    self.image = pygame.image.load("Cuchillo2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.cuchillos -= 1
                    jugador.disparoCuchillo()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.cuchillo == True:
                    self.image = pygame.image.load("Cuchillo1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.granada == True and self.granadas > 0:
                    self.image = pygame.image.load("Granada2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.granadas -= 1
                    jugador.disparoGranada()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.granada == True:
                    self.image = pygame.image.load("Granada1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

        def disparoPistola(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def disparoEscopeta(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

            bala2 = Disparos2(self.rect.centerx, self.rect.right)
            balas.add(bala2)

            bala3 = Disparos3(self.rect.centerx, self.rect.right)
            balas.add(bala3)

        def disparoMetralleta(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

            bala2 = Disparos2(self.rect.centerx, self.rect.right)
            balas.add(bala2)

            bala3 = Disparos3(self.rect.centerx, self.rect.right)
            balas.add(bala3)

            bala4 = Disparos4(self.rect.centerx, self.rect.right)
            balas.add(bala4)

            bala5 = Disparos5(self.rect.centerx, self.rect.right)
            balas.add(bala5)

        def disparoCuchillo(self):
            bala = Disparos6(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def disparoGranada(self):
            bala = Disparos7(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def vida(self):
            # vida
            if self.energia == 10:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 9:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 8:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 7:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 6:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 5:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 4:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 3:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 2:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 1:
                self.corazon1 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 0:
                game_over()


    # disparo escopeta y pistola
    class Disparos1(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 75

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    # disparos metralleta + anterior
    class Disparos2(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 130

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos3(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 35

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos4(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y - 15

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos5(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 190

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    # disparo cuchillo
    class Disparos6(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("ataquecuchillo.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 60
            self.rect.y = jugador.rect.y - 30

        def update(self):
            self.rect.x += 15
            if self.rect.bottom < 0:
                self.kill()

    # disparo granada
    class Disparos7(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("granadaDisp.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 100
            self.rect.y = jugador.rect.y + 60

        def update(self):
            self.rect.x += 15
            if self.rect.bottom < 0:
                self.kill()

    # Clases oscar

    def load_image(nombre, alpha=False):
        ruta = os.path.join(nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print("Error, no se puede cargar la imagen: " + ruta)
            sys.exit(1)

        if alpha is True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    class generar_Aliens:
        def __init__(self):
            self.aliens = pygame.sprite.Group()
            self.siguiente_alien = pygame.time.get_ticks() + random.randint(2000, 3000)
            self.contador_aliens = 0

        def quitar_aliens(self):
            self.contador_aliens -= 1

        def update(self):
            if self.quitar_aliens():
                self.contador_aliens -= 1
            if self.contador_aliens < 15:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual >= self.siguiente_alien:
                    n = random.randint(2, 5)
                    for i in range(n):
                        self.generar_alien()
                    self.siguiente_alien = pygame.time.get_ticks() + random.randint(2000, 3000)

            self.aliens.update()

        def draw(self, screen):
            self.aliens.draw(screen)

        def generar_alien(self):
            tipo_alien = random.randint(1, 3)
            if tipo_alien == 1:
                alien = Aliens1_image()
            elif tipo_alien == 2:
                alien = Aliens2_image()
            elif tipo_alien == 3:
                alien = Aliens3_image()

            alien.rect.centerx = SCREEN_WIDTH - 70
            alien.rect.centery = random.randint(50, 1000)
            self.contador_aliens += 1
            self.aliens.add(alien)

    class Aliens1_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien1.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 40

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -2

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

            if self.rect.x <= 1700:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1600:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1500:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1400:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1300:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1200:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1100:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1000:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 900:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 800:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 700:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 600:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 500:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 400:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 300:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 250:
                self.image = load_image("alien1.png", alpha=True)

    class Aliens2_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien2.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 20

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -1

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

    class Aliens3_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien3_1.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 30

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -2.5

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

            if self.rect.x <= 1700:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 1500:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 1300:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 1100:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 900:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 700:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 500:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 300:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 200:
                self.image = load_image("alien3_2.png", alpha=True)

    # Inicio pygame
    pygame.init()

    # sonidos
    sound_escopeta = mixer.Sound("escopeta.wav")
    sound_pistola = mixer.Sound('pistola.wav')
    sound_metralleta = mixer.Sound('metralleta.wav')
    sound_cuchillo = mixer.Sound('cuchillo.wav')
    Clock = pygame.time.Clock()

    # parametros de la pantalla
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    bg = pygame.image.load("fondogame.png").convert()

    # Instanciar
    # Creamos un grupo de sprites, instanciamos objeto(jugador) y lo anadimos a la lista
    sprites = pygame.sprite.Group()
    jugador = Personaje()
    sprites.add(jugador)

    # Creamos un grupo de sprites de balas
    balas = pygame.sprite.Group()

    # Creamos un grupo de sprites para los aliens
    aliens = generar_Aliens()

    while running:

        # Para que la pantalla guarde los cambios
        screen.blit(bg, (0, 0))

        sprites.draw(screen)
        sprites.update()
        balas.draw(screen)
        balas.update()
        aliens.draw(screen)
        aliens.update()
        # Colisiones

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    sys.exit(0)

        pygame.display.update()
        Clock.tick(fps)

    pygame.quit()
def nivel3(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm):

    soundtrack.stop()

    color = (0, 0, 0)
    fps = 60
    color2 = (255, 255, 255)

    class Personaje(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.center = (100, SCREEN_HEIGHT // 2)  # donde queremos que se instancie en primer lugar el personaje
            self.energia = 10
            self.velocidad_x = 0
            self.velocidad_y = 0
            self.pistola = False
            self.escopeta = False
            self.granada = False
            self.metralleta = False
            self.cuchillo = False
            self.disparando = False
            self.balasPistola = 15
            self.balasEscopeta = 5
            self.balasMetralleta = 50
            self.cargador = 1
            self.cuchillos = 15
            self.granadas = 2
            self.aliensMuertos = 0

        def update(self):

            # Colisiones
            if pygame.sprite.groupcollide(aliens.aliens, sprites, 1, 0):
                self.energia -= 1

            if pygame.sprite.groupcollide(aliens.aliens, balas, 1, 1):
                self.aliensMuertos += 1

            if self.aliensMuertos == 15:
                victoria()

            self.vida()

            # calavera con contador de aliens
            self.calavera = pygame.image.load("calavera.png")
            self.calavera = pygame.transform.scale(self.calavera, (100, 100))
            screen.blit(self.calavera, (40, 250))
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(str(self.aliensMuertos), True, color2)
            textRect = text.get_rect()
            textRect.center = (160, 310)
            screen.blit(text, textRect)

            # Inventario
            if self.pistola:
                self.pistolaInv = pygame.image.load("Pistolainventario.png").convert()
                self.pistolaInv = pygame.transform.scale(self.pistolaInv, (200, 200))
                screen.blit(self.pistolaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasPistola), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.escopeta:
                self.escopetaInv = pygame.image.load("Escopetainventario.png").convert()
                self.escopetaInv = pygame.transform.scale(self.escopetaInv, (200, 200))
                screen.blit(self.escopetaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasEscopeta), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.cuchillo:
                self.cuchilloInv = pygame.image.load("Cuchilloinventario.png").convert()
                self.cuchilloInv = pygame.transform.scale(self.cuchilloInv, (200, 200))
                screen.blit(self.cuchilloInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.cuchillos), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.metralleta:
                self.metralletaInv = pygame.image.load("Metralletainventario.png").convert()
                self.metralletaInv = pygame.transform.scale(self.metralletaInv, (200, 200))
                screen.blit(self.metralletaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasMetralleta), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.granada:
                self.granadaInv = pygame.image.load("Granadainventario.png").convert()
                self.granadaInv = pygame.transform.scale(self.granadaInv, (200, 200))
                screen.blit(self.granadaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.granadas), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            # velocidad predeterminada
            self.velocidad_x = 0
            self.velocidad_y = 0

            # input de teclas
            teclas = pygame.key.get_pressed()

            # Movimiento
            if teclas[pygame.K_a]:
                self.velocidad_x = -10
            if teclas[pygame.K_d]:
                self.velocidad_x = 10
            if teclas[pygame.K_w]:
                self.velocidad_y = -10
            if teclas[pygame.K_s]:
                self.velocidad_y = 10

                # recargar armas
            if teclas[pygame.K_r] and self.pistola == True and self.cargador > 0:
                self.balasPistola += 7
                self.cargador -= 1

            if teclas[pygame.K_r] and self.metralleta == True and self.cargador > 0:
                self.balasMetralleta += 25
                self.cargador -= 1

            if teclas[pygame.K_r] and self.escopeta == True and self.cargador > 0:
                self.balasEscopeta += 3
                self.cargador -= 1

            if teclas[pygame.K_r] and self.cuchillo == True and self.cargador > 0:
                self.cuchillos += 7
                self.cargador -= 1

            if teclas[pygame.K_r] and self.granada == True and self.cargador > 0:
                self.granadas += 1
                self.cargador -= 1

                # Sacar Armas
            if teclas[pygame.K_1] and pistola_arm == True:
                self.pistola = True
                self.escopeta = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))

            if teclas[pygame.K_2] and escopeta_arm == True:
                self.escopeta = True
                self.pistola = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("MachineGun1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))

            if teclas[pygame.K_3] and metralleta_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = True
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("Metralleta1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            if teclas[pygame.K_4] and cuchillo_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = False
                self.cuchillo = True
                self.granada = False
                self.image = pygame.image.load("Cuchillo1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            if teclas[pygame.K_5] and granada_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = True
                self.image = pygame.image.load("Granada1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            # Actualiza la velocidad del personaje
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

            # Limites de movimiento izquierda derecha
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            # Limites de movimiento arriba, abajo
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0

            self.disparar()

        def disparar(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.pistola == True and self.balasPistola > 0:
                    sound_pistola.play()
                    self.image = pygame.image.load("Handgun2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.balasPistola -= 1
                    jugador.disparoPistola()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.pistola == True:
                    self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.escopeta == True and self.balasEscopeta > 0:
                    sound_escopeta.play()
                    self.image = pygame.image.load("MachineGun2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.balasEscopeta -= 1
                    jugador.disparoEscopeta()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.escopeta == True:
                    self.image = pygame.image.load("MachineGun1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.metralleta == True and self.balasMetralleta > 0:
                    self.image = pygame.image.load("Metralleta2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.balasMetralleta -= 5
                    jugador.disparoMetralleta()
                    sound_metralleta.play()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.metralleta == True:
                    self.image = pygame.image.load("Metralleta1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.cuchillo == True and self.cuchillos > 0:
                    self.image = pygame.image.load("Cuchillo2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.cuchillos -= 1
                    jugador.disparoCuchillo()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.cuchillo == True:
                    self.image = pygame.image.load("Cuchillo1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.granada == True and self.granadas > 0:
                    self.image = pygame.image.load("Granada2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.granadas -= 1
                    jugador.disparoGranada()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.granada == True:
                    self.image = pygame.image.load("Granada1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

        def disparoPistola(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def disparoEscopeta(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

            bala2 = Disparos2(self.rect.centerx, self.rect.right)
            balas.add(bala2)

            bala3 = Disparos3(self.rect.centerx, self.rect.right)
            balas.add(bala3)

        def disparoMetralleta(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

            bala2 = Disparos2(self.rect.centerx, self.rect.right)
            balas.add(bala2)

            bala3 = Disparos3(self.rect.centerx, self.rect.right)
            balas.add(bala3)

            bala4 = Disparos4(self.rect.centerx, self.rect.right)
            balas.add(bala4)

            bala5 = Disparos5(self.rect.centerx, self.rect.right)
            balas.add(bala5)

        def disparoCuchillo(self):
            bala = Disparos6(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def disparoGranada(self):
            bala = Disparos7(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def vida(self):
            # vida
            if self.energia == 10:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 9:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 8:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 7:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 6:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 5:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 4:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 3:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 2:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 1:
                self.corazon1 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 0:
                game_over()


    # disparo escopeta y pistola
    class Disparos1(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 75

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    # disparos metralleta + anterior
    class Disparos2(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 130

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos3(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 35

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos4(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y - 15

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos5(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 190

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    # disparo cuchillo
    class Disparos6(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("ataquecuchillo.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 60
            self.rect.y = jugador.rect.y - 30

        def update(self):
            self.rect.x += 15
            if self.rect.bottom < 0:
                self.kill()

    # disparo granada
    class Disparos7(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("granadaDisp.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 100
            self.rect.y = jugador.rect.y + 60

        def update(self):
            self.rect.x += 15
            if self.rect.bottom < 0:
                self.kill()

    # Clases oscar

    def load_image(nombre, alpha=False):
        ruta = os.path.join(nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print("Error, no se puede cargar la imagen: " + ruta)
            sys.exit(1)

        if alpha is True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    class generar_Aliens:
        def __init__(self):
            self.aliens = pygame.sprite.Group()
            self.siguiente_alien = pygame.time.get_ticks() + random.randint(2000, 3000)
            self.contador_aliens = 0

        def quitar_aliens(self):
            self.contador_aliens -= 1

        def update(self):
            if self.quitar_aliens():
                self.contador_aliens -= 1
            if self.contador_aliens < 15:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual >= self.siguiente_alien:
                    n = random.randint(2, 6)
                    for i in range(n):
                        self.generar_alien()
                    self.siguiente_alien = pygame.time.get_ticks() + random.randint(2000, 3000)

            self.aliens.update()

        def draw(self, screen):
            self.aliens.draw(screen)

        def generar_alien(self):
            tipo_alien = random.randint(1, 3)
            if tipo_alien == 1:
                alien = Aliens1_image()
            elif tipo_alien == 2:
                alien = Aliens2_image()
            elif tipo_alien == 3:
                alien = Aliens3_image()

            alien.rect.centerx = SCREEN_WIDTH - 70
            alien.rect.centery = random.randint(50, 1000)
            self.contador_aliens += 1
            self.aliens.add(alien)

    class Aliens1_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien1.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 40

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -2

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

            if self.rect.x <= 1700:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1600:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1500:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1400:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1300:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1200:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1100:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1000:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 900:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 800:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 700:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 600:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 500:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 400:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 300:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 250:
                self.image = load_image("alien1.png", alpha=True)

    class Aliens2_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien2.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 20

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -1

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

    class Aliens3_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien3_1.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 30

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -2.5

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

            if self.rect.x <= 1700:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 1500:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 1300:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 1100:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 900:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 700:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 500:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 300:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 200:
                self.image = load_image("alien3_2.png", alpha=True)


    # Inicio pygame
    pygame.init()

    # sonidos
    sound_escopeta = mixer.Sound("escopeta.wav")
    sound_pistola = mixer.Sound('pistola.wav')
    sound_metralleta = mixer.Sound('metralleta.wav')
    sound_cuchillo = mixer.Sound('cuchillo.wav')
    Clock = pygame.time.Clock()

    # parametros de la pantalla
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    bg = pygame.image.load("fondogame.png").convert()

    # Instanciar
    # Creamos un grupo de sprites, instanciamos objeto(jugador) y lo anadimos a la lista
    sprites = pygame.sprite.Group()
    jugador = Personaje()
    sprites.add(jugador)

    # Creamos un grupo de sprites de balas
    balas = pygame.sprite.Group()

    # Creamos un grupo de sprites para los aliens
    aliens = generar_Aliens()

    while running:

        # Para que la pantalla guarde los cambios
        screen.blit(bg, (0, 0))

        sprites.draw(screen)
        sprites.update()
        balas.draw(screen)
        balas.update()
        aliens.draw(screen)
        aliens.update()
        # Colisiones

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    sys.exit(0)

        pygame.display.update()
        Clock.tick(fps)

    pygame.quit()

def nivel1(pistola_arm, granada_arm, metralleta_arm, escopeta_arm, cuchillo_arm):

    soundtrack.stop()

    color = (0, 0, 0)
    fps = 60
    color2 = (255, 255, 255)

    class Personaje(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.center = (100, SCREEN_HEIGHT // 2)  # donde queremos que se instancie en primer lugar el personaje
            self.energia = 10
            self.velocidad_x = 0
            self.velocidad_y = 0
            self.pistola = False
            self.escopeta = False
            self.granada = False
            self.metralleta = False
            self.cuchillo = False
            self.disparando = False
            self.balasPistola = 15
            self.balasEscopeta = 5
            self.balasMetralleta = 50
            self.cargador = 1
            self.cuchillos = 15
            self.granadas = 2
            self.aliensMuertos = 0

        def update(self):

            # Colisiones
            if pygame.sprite.groupcollide(aliens.aliens, sprites, 1, 0):
                self.energia -= 1

            if pygame.sprite.groupcollide(aliens.aliens, balas, 1, 1):
                self.aliensMuertos += 1

            if self.aliensMuertos == 5:
                victoria()

            self.vida()

            # calavera con contador de aliens
            self.calavera = pygame.image.load("calavera.png")
            self.calavera = pygame.transform.scale(self.calavera, (100, 100))
            screen.blit(self.calavera, (40, 250))
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render(str(self.aliensMuertos), True, color2)
            textRect = text.get_rect()
            textRect.center = (160, 310)
            screen.blit(text, textRect)

            # Inventario
            if self.pistola:
                self.pistolaInv = pygame.image.load("Pistolainventario.png").convert()
                self.pistolaInv = pygame.transform.scale(self.pistolaInv, (200, 200))
                screen.blit(self.pistolaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasPistola), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.escopeta:
                self.escopetaInv = pygame.image.load("Escopetainventario.png").convert()
                self.escopetaInv = pygame.transform.scale(self.escopetaInv, (200, 200))
                screen.blit(self.escopetaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasEscopeta), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.cuchillo:
                self.cuchilloInv = pygame.image.load("Cuchilloinventario.png").convert()
                self.cuchilloInv = pygame.transform.scale(self.cuchilloInv, (200, 200))
                screen.blit(self.cuchilloInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.cuchillos), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.metralleta:
                self.metralletaInv = pygame.image.load("Metralletainventario.png").convert()
                self.metralletaInv = pygame.transform.scale(self.metralletaInv, (200, 200))
                screen.blit(self.metralletaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.balasMetralleta), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            if self.granada:
                self.granadaInv = pygame.image.load("Granadainventario.png").convert()
                self.granadaInv = pygame.transform.scale(self.granadaInv, (200, 200))
                screen.blit(self.granadaInv, (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(self.granadas), True, color2)
                textRect = text.get_rect()
                textRect.center = (150, 150)
                screen.blit(text, textRect)

            # velocidad predeterminada
            self.velocidad_x = 0
            self.velocidad_y = 0

            # input de teclas
            teclas = pygame.key.get_pressed()

            # Movimiento
            if teclas[pygame.K_a]:
                self.velocidad_x = -10
            if teclas[pygame.K_d]:
                self.velocidad_x = 10
            if teclas[pygame.K_w]:
                self.velocidad_y = -10
            if teclas[pygame.K_s]:
                self.velocidad_y = 10

                # recargar armas
            if teclas[pygame.K_r] and self.pistola == True and self.cargador > 0:
                self.balasPistola += 7
                self.cargador -= 1

            if teclas[pygame.K_r] and self.metralleta == True and self.cargador > 0:
                self.balasMetralleta += 25
                self.cargador -= 1

            if teclas[pygame.K_r] and self.escopeta == True and self.cargador > 0:
                self.balasEscopeta += 3
                self.cargador -= 1

            if teclas[pygame.K_r] and self.cuchillo == True and self.cargador > 0:
                self.cuchillos += 7
                self.cargador -= 1

            if teclas[pygame.K_r] and self.granada == True and self.cargador > 0:
                self.granadas += 1
                self.cargador -= 1

                # Sacar Armas
            if teclas[pygame.K_1] and pistola_arm == True:
                self.pistola = True
                self.escopeta = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))

            if teclas[pygame.K_2] and escopeta_arm == True:
                self.escopeta = True
                self.pistola = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("MachineGun1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))

            if teclas[pygame.K_3] and metralleta_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = True
                self.cuchillo = False
                self.granada = False
                self.image = pygame.image.load("Metralleta1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            if teclas[pygame.K_4] and cuchillo_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = False
                self.cuchillo = True
                self.granada = False
                self.image = pygame.image.load("Cuchillo1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            if teclas[pygame.K_5] and granada_arm == True:
                self.escopeta = False
                self.pistola = False
                self.metralleta = False
                self.cuchillo = False
                self.granada = True
                self.image = pygame.image.load("Granada1.png").convert()  # Agregamos la imagen
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_colorkey(color)

            # Actualiza la velocidad del personaje
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

            # Limites de movimiento izquierda derecha
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            # Limites de movimiento arriba, abajo
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
            if self.rect.top < 0:
                self.rect.top = 0

            self.disparar()

        def disparar(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.pistola == True and self.balasPistola > 0:
                    sound_pistola.play()
                    self.image = pygame.image.load("Handgun2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.balasPistola -= 1
                    jugador.disparoPistola()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.pistola == True:
                    self.image = pygame.image.load("Handgun1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.escopeta == True and self.balasEscopeta > 0:
                    sound_escopeta.play()
                    self.image = pygame.image.load("MachineGun2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.balasEscopeta -= 1
                    jugador.disparoEscopeta()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.escopeta == True:
                    self.image = pygame.image.load("MachineGun1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.metralleta == True and self.balasMetralleta > 0:
                    self.image = pygame.image.load("Metralleta2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.balasMetralleta -= 5
                    jugador.disparoMetralleta()
                    sound_metralleta.play()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.metralleta == True:
                    self.image = pygame.image.load("Metralleta1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.cuchillo == True and self.cuchillos > 0:
                    self.image = pygame.image.load("Cuchillo2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.cuchillos -= 1
                    jugador.disparoCuchillo()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.cuchillo == True:
                    self.image = pygame.image.load("Cuchillo1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.granada == True and self.granadas > 0:
                    self.image = pygame.image.load("Granada2.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)
                    self.granadas -= 1
                    jugador.disparoGranada()

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.granada == True:
                    self.image = pygame.image.load("Granada1.png").convert()  # Agregamos la imagen
                    self.image = pygame.transform.scale(self.image, (200, 200))
                    self.image.set_colorkey(color)

        def disparoPistola(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def disparoEscopeta(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

            bala2 = Disparos2(self.rect.centerx, self.rect.right)
            balas.add(bala2)

            bala3 = Disparos3(self.rect.centerx, self.rect.right)
            balas.add(bala3)

        def disparoMetralleta(self):
            bala = Disparos1(self.rect.centerx, self.rect.right)
            balas.add(bala)

            bala2 = Disparos2(self.rect.centerx, self.rect.right)
            balas.add(bala2)

            bala3 = Disparos3(self.rect.centerx, self.rect.right)
            balas.add(bala3)

            bala4 = Disparos4(self.rect.centerx, self.rect.right)
            balas.add(bala4)

            bala5 = Disparos5(self.rect.centerx, self.rect.right)
            balas.add(bala5)

        def disparoCuchillo(self):
            bala = Disparos6(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def disparoGranada(self):
            bala = Disparos7(self.rect.centerx, self.rect.right)
            balas.add(bala)

        def vida(self):
            # vida
            if self.energia == 10:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 9:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 8:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 7:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 6:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 5:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 4:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 3:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 2:
                self.corazon1 = pygame.image.load("Health1.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 1:
                self.corazon1 = pygame.image.load("Health1Half.png").convert()  # Agregamos la imagen
                self.corazon1 = pygame.transform.scale(self.corazon1, (150, 150))
                self.corazon1.set_colorkey(color)
                screen.blit(self.corazon1, (225, 30))

                self.corazon2 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon2 = pygame.transform.scale(self.corazon2, (150, 150))
                self.corazon2.set_colorkey(color)
                screen.blit(self.corazon2, (400, 30))

                self.corazon3 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon3 = pygame.transform.scale(self.corazon3, (150, 150))
                self.corazon3.set_colorkey(color)
                screen.blit(self.corazon3, (575, 30))

                self.corazon4 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon4 = pygame.transform.scale(self.corazon4, (150, 150))
                self.corazon4.set_colorkey(color)
                screen.blit(self.corazon4, (750, 30))

                self.corazon5 = pygame.image.load("HealthEmpty.png").convert()  # Agregamos la imagen
                self.corazon5 = pygame.transform.scale(self.corazon5, (150, 150))
                self.corazon5.set_colorkey(color)
                screen.blit(self.corazon5, (925, 30))

            if self.energia == 0:
                game_over()


    # disparo escopeta y pistola
    class Disparos1(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 75

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    # disparos metralleta + anterior
    class Disparos2(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 130

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos3(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 35

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos4(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y - 15

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    class Disparos5(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()

            self.image = pygame.image.load("BulletProjectile.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 200
            self.rect.y = jugador.rect.y + 190

        def update(self):
            self.rect.x += 25
            if self.rect.bottom < 0:
                self.kill()

    # disparo cuchillo
    class Disparos6(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("ataquecuchillo.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 60
            self.rect.y = jugador.rect.y - 30

        def update(self):
            self.rect.x += 15
            if self.rect.bottom < 0:
                self.kill()

    # disparo granada
    class Disparos7(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("granadaDisp.png").convert()  # Agregamos la imagen
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image.set_colorkey(color)
            self.rect = self.image.get_rect()  # obtenemos un rectangulo formado por la imagen
            self.rect.bottom = y
            self.rect.centerx = x
            self.rect.x = jugador.rect.x + 100
            self.rect.y = jugador.rect.y + 60

        def update(self):
            self.rect.x += 15
            if self.rect.bottom < 0:
                self.kill()

    # Clases oscar

    def load_image(nombre, alpha=False):
        ruta = os.path.join(nombre)
        try:
            image = pygame.image.load(ruta)
        except:
            print("Error, no se puede cargar la imagen: " + ruta)
            sys.exit(1)

        if alpha is True:
            image = image.convert_alpha()
        else:
            image = image.convert()
        return image

    class generar_Aliens:
        def __init__(self):
            self.aliens = pygame.sprite.Group()
            self.siguiente_alien = pygame.time.get_ticks() + random.randint(2000, 3000)
            self.contador_aliens = 0

        def quitar_aliens(self):
            self.contador_aliens -= 1

        def update(self):
            if self.quitar_aliens():
                self.contador_aliens -= 1
            if self.contador_aliens < 15:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual >= self.siguiente_alien:
                    n = random.randint(2, 4)
                    for i in range(n):
                        self.generar_alien()
                    self.siguiente_alien = pygame.time.get_ticks() + random.randint(2000, 3000)

            self.aliens.update()

        def draw(self, screen):
            self.aliens.draw(screen)

        def generar_alien(self):
            tipo_alien = random.randint(1, 3)
            if tipo_alien == 1:
                alien = Aliens1_image()
            elif tipo_alien == 2:
                alien = Aliens2_image()
            elif tipo_alien == 3:
                alien = Aliens3_image()

            alien.rect.centerx = SCREEN_WIDTH - 70
            alien.rect.centery = random.randint(50, 1000)
            self.contador_aliens += 1
            self.aliens.add(alien)

    class Aliens1_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien1.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 40

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -2

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

            if self.rect.x <= 1700:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1600:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1500:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1400:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1300:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1200:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 1100:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 1000:
                self.image = load_image("alien1_1.png", alpha=True)

            if self.rect.x <= 900:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 800:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 700:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 600:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 500:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 400:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 300:
                self.image = load_image("alien1_2.png", alpha=True)

            if self.rect.x <= 250:
                self.image = load_image("alien1.png", alpha=True)

    class Aliens2_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien2.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 20

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -1

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

    class Aliens3_image(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = load_image("alien3_1.png", alpha=True)
            self.rect = self.image.get_rect()
            self.velocidad_x = 0
            self.vida = 30

        def update(self):
            self.velocidad_x = 0

            self.velocidad_x = -2.5

            if self.rect.x < jugador.rect.x:
                self.rect.x -= self.velocidad_x
            elif self.rect.x > jugador.rect.x:
                self.rect.x += self.velocidad_x

            if self.rect.y < jugador.rect.y:
                self.rect.y -= self.velocidad_x
            elif self.rect.y > jugador.rect.y:
                self.rect.y += self.velocidad_x
            elif self.rect.y == jugador.rect.y:
                self.rect.y += 0

            if self.rect.y <= 50:
                self.rect.y = 50
            elif self.rect.y >= 1000:
                self.rect.y = 1000

            if self.rect.x <= 1700:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 1500:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 1300:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 1100:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 900:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 700:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 500:
                self.image = load_image("alien3_2.png", alpha=True)

            if self.rect.x <= 300:
                self.image = load_image("alien3_1.png", alpha=True)

            if self.rect.x <= 200:
                self.image = load_image("alien3_2.png", alpha=True)


    # Inicio pygame
    pygame.init()

    # sonidos
    sound_escopeta = mixer.Sound("escopeta.wav")
    sound_pistola = mixer.Sound('pistola.wav')
    sound_metralleta = mixer.Sound('metralleta.wav')
    sound_cuchillo = mixer.Sound('cuchillo.wav')
    Clock = pygame.time.Clock()

    # parametros de la pantalla
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    bg = pygame.image.load("fondogame.png").convert()

    # Instanciar
    # Creamos un grupo de sprites, instanciamos objeto(jugador) y lo anadimos a la lista
    sprites = pygame.sprite.Group()
    jugador = Personaje()
    sprites.add(jugador)

    # Creamos un grupo de sprites de balas
    balas = pygame.sprite.Group()

    # Creamos un grupo de sprites para los aliens
    aliens = generar_Aliens()

    while running:

        # Para que la pantalla guarde los cambios
        screen.blit(bg, (0, 0))

        sprites.draw(screen)
        sprites.update()
        balas.draw(screen)
        balas.update()
        aliens.draw(screen)
        aliens.update()
        # Colisiones

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    sys.exit(0)

        pygame.display.update()
        Clock.tick(fps)

    pygame.quit()


def game_over():
    screen5.fill(white)
    gameover = pygame.image.load("game over.png")  # Agregamos la imagen
    screen5.blit(gameover, [0, 0])
    boton_menu = botones.boton(650, 600, boton_menu_imagen, 0.8)

    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        if boton_menu.draw(screen5):
            first_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()



def victoria():
    screen5.fill(white)
    victoria = pygame.image.load("victoria.png")  # Agregamos la imagen
    screen5.blit(victoria, [0, 0])
    boton_menu = botones.boton(650, 600, boton_menu_imagen, 0.8)

    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window

        if boton_menu.draw(screen5):
            first_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()


def pantalla_niveles(pistola_arm, escopeta_arm, metralleta_arm, granada_arm, cuchillo_arm):
    
    screen5.fill(white)
    niveles = pygame.image.load("pantalla_niveles.png")  # Agregamos la imagen
    screen5.blit(niveles, [0, 0])
    nivel3_boton = pygame.image.load("nivel3.png")
    boton_nivel3 = botones.boton(1100, 400, nivel3_boton, 0.4)
    nivel2_boton = pygame.image.load("nivel2.png")
    boton_nivel2 = botones.boton(550, 400, nivel2_boton, 0.4)
    nivel1_boton = pygame.image.load("nivel1.png")
    boton_nivel1 = botones.boton(0, 400, nivel1_boton, 0.4)

    done = False
    while not done:
        pygame.display.update()  # Update window
        # Bucle for that register all things happend on this window
        if boton_nivel3.draw(screen5):

            nivel3(pistola_arm, escopeta_arm, metralleta_arm, granada_arm, cuchillo_arm)

        if boton_nivel2.draw(screen5):

            nivel2(pistola_arm, escopeta_arm, metralleta_arm, granada_arm, cuchillo_arm)

        if boton_nivel1.draw(screen5):

            nivel1(pistola_arm, escopeta_arm, metralleta_arm, granada_arm, cuchillo_arm)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()


first_window()