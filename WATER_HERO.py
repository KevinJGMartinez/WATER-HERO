import pygame
import sys
import os
import pyganim
import time
import string
import random
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
ANCHO = 1024
ALTO = 600
FPS = 130
black = (0,0,0)
white = (255,255,255)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('WATER HERO')
rojo=200,0,0
negro = 0,0,0
lose = False
win = False

reloj = pygame.time.Clock()
pause = False
# Variable para el cambio de idioma
lenguaje = 0
# Variable para activa/desactivar la música
musi = 0
# Insertar imagenes de personajes y fondos
IDLEDER = pygame.image.load('sprites/monito/IDLE00.png')
IDLEIZQ = pygame.image.load('sprites/monito/IDLE0.png')
WALKIZQ = [pygame.image.load('sprites/monito/WALK0.png'), pygame.image.load('sprites/monito/WALK1.png'), pygame.image.load('sprites/monito/WALK2.png'), pygame.image.load('sprites/monito/WALK3.png'), pygame.image.load('sprites/monito/WALK4.png')]
WALKDER = [pygame.image.load('sprites/monito/WALK00.png'), pygame.image.load('sprites/monito/WALK11.png'), pygame.image.load('sprites/monito/WALK22.png'), pygame.image.load('sprites/monito/WALK33.png'),pygame.image.load('sprites/monito/WALK44.png')]
JUMPIZQ = [pygame.image.load('sprites/monito/JUMP0.png'),pygame.image.load('sprites/monito/JUMP1.png'),pygame.image.load('sprites/monito/JUMP2.png'),pygame.image.load('sprites/monito/JUMP3.png')]
JUMPDER = [pygame.image.load('sprites/monito/JUMP00.png'),pygame.image.load('sprites/monito/JUMP11.png'),pygame.image.load('sprites/monito/JUMP22.png'),pygame.image.load('sprites/monito/JUMP33.png')]
VIDA = pygame.image.load('sprites/monito/VIDA.png')
FONDO_MENU = pygame.image.load('sprites/FONDO_MENU.jpg')
ATTI = pygame.image.load('sprites/monito/ATT1.png')
ATTD = pygame.image.load('sprites/monito/ATT11.png')
TRONC = pygame.image.load('sprites/TRONCOS.png')
ICON = pygame.image.load('sprites/monito/ICON.png')
DANY = pygame.image.load('sprites/integrantes/DANIEL.png')
KEVS = pygame.image.load('sprites/integrantes/KEVIN.png')
ROBE = pygame.image.load('sprites/integrantes/ROBERTO.jpg')
LUIS = pygame.image.load('sprites/integrantes/LUIS.jpg')
DIEGO = pygame.image.load('sprites/integrantes/DIEGO.jpg')
Maestro = pygame.image.load('sprites/integrantes/efrain1.png')
BOTON = [pygame.image.load('sprites/BOTON0.png'),pygame.image.load('sprites/BOTON1.png')]
HURT = pygame.image.load('sprites/monito/HURT0.png')
HURTI = pygame.image.load('sprites/monito/HURT00.png')
BALA = pygame.image.load('sprites/jefes/Gastly/BALA.png')
BALA1 = pygame.image.load('sprites/jefes/Muk/BALA1.png')
BALA2 = pygame.image.load('sprites/jefes/Rubish/BALA2.png')
PILAR = pygame.image.load('sprites/PILAR.png')
VIDAS_ENEM=[pygame.image.load('sprites/jefes/Muk/VQ.png'),pygame.image.load('sprites/jefes/Gastly/VP.png'),pygame.image.load('sprites/jefes/Rubish/VB.png')]
PET_VENCIDO = pygame.image.load('sprites/jefes/Gastly/PET_ELIMINADO.png')
QUIMICO_VENCIDO = pygame.image.load('sprites/jefes/Muk/QUIMICO_ELIMINADO.png')
BASURA_VENCIDO = pygame.image.load('sprites/jefes/Rubish/BASURA_ELIMINADO.png')
INSTRUCTIONS = pygame.image.load('sprites/INSTRUCTIONS.png')
INSTRUCCIONES = pygame.image.load('sprites/INSTRUCCIONES.png')


"""FONDOGAST = pyganim.PygAnimation([('sprites/imagenes_extra_P/Gastly/Move00.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move01.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move02.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move03.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move04.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move05.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move06.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move07.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move08.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move09.png',0.4),
					('sprites/imagenes_extraP/Gastly/Move10.png',0.4)])"""

"""FONDORUB = pyganim.PygAnimation([('sprites/imagenes_extra_P/Rubish/MOVE00.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE01.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE02.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE03.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE04.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE05.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE06.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE07.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE08.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE09.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE10.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE11.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE12.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE13.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE14.png',0.4),
					('sprites/imagenes_extraP/Rubish/MOVE15.png',0.4)])"""

"""FONDOMUK = pyganim.PygAnimation([('sprites/imagenes_extra/Gastly/MOVE00.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE01.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE02.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE03.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE04.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE05.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE06.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE07.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE08.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE09.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE10.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE11.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE12.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE13.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE14.png',0.4),
				('sprites/imagenes_extra/Gastly/MOVE15.png',0.4),])"""
#Icono de la ventana de juego
pygame.display.set_icon(ICON)

# Animaciones con PYGANIM
FONDO = pyganim.PygAnimation([('sprites/fondo_petroleo/FONDO0.png',1.19),
				('sprites/fondo_petroleo/FONDO1.png',1.19),
				('sprites/fondo_petroleo/FONDO2.png',1.19),
				('sprites/fondo_petroleo/FONDO3.png',1.19),
				('sprites/fondo_petroleo/Move00.png',1.19),
				('sprites/fondo_petroleo/Move01.png',1.19),
				('sprites/fondo_petroleo/Move02.png',1.19),
				('sprites/fondo_petroleo/Move03.png',1.19),
				('sprites/fondo_petroleo/Move04.png',1.19),
				('sprites/fondo_petroleo/Move05.png',1.19),
				('sprites/fondo_petroleo/Move06.png',1.19),
				('sprites/fondo_petroleo/Move07.png',1.19),
				('sprites/fondo_petroleo/Move08.png',1.19),
				('sprites/fondo_petroleo/Move09.png',1.19),
				('sprites/fondo_petroleo/Move10.png',1.19)])

PETROLEO = pyganim.PygAnimation([('sprites/jefes/Gastly/ENEM0.png',0.4),
				 ('sprites/jefes/Gastly/ENEM1.png',0.4),
				 ('sprites/jefes/Gastly/ENEMATT.png',0.4)])

QUIM = pyganim.PygAnimation([('sprites/jefes/Muk/ENEMQUIM0.png',0.4),
				  ('sprites/jefes/Muk/ENEMQUIM1.png',0.4),
				  ('sprites/jefes/Muk/ENEMQUIMATT.png',0.4)])

BASURA = pyganim.PygAnimation([('sprites/jefes/Rubish/ENEMBAS0.png',0.4),
				  ('sprites/jefes/Rubish/ENEMBAS1.png',0.4),
				  ('sprites/jefes/Rubish/ENEMBASATT.png',0.4)])

PETR = pyganim.PygAnimation([('sprites/jefes/Gastly/PET0.png',0.4),
				 ('sprites/jefes/Gastly/PET1.png',0.4)])

QUIMQ = pyganim.PygAnimation([('sprites/jefes/Muk/QUIM0.png',0.4),
				  ('sprites/jefes/Muk/QUIM1.png',0.4)])

BASUR = pyganim.PygAnimation([('sprites/jefes/Rubish/BAS0.png',0.4),
				  ('sprites/jefes/Rubish/BAS1.png',0.4)])

BACK = pyganim.PygAnimation( [('sprites/back1.png',0.4),
				('sprites/back2.png',0.4)])
FONDOBAS = pyganim.PygAnimation([('sprites/fondo_basura/sprite_14.png',0.4),
				('sprites/fondo_basura/sprite_13.png',0.4),
				('sprites/fondo_basura/sprite_12.png',0.4),
				('sprites/fondo_basura/sprite_11.png',0.4),
				('sprites/fondo_basura/sprite_10.png',0.4),
				('sprites/fondo_basura/sprite_09.png',0.4),
				('sprites/fondo_basura/sprite_08.png',0.4),
				('sprites/fondo_basura/sprite_07.png',0.4),
				('sprites/fondo_basura/sprite_06.png',0.4),
				('sprites/fondo_basura/sprite_05.png',0.4),
				('sprites/fondo_basura/sprite_04.png',0.4),
				('sprites/fondo_basura/sprite_03.png',0.4),
				('sprites/fondo_basura/sprite_02.png',0.4),
				('sprites/fondo_basura/sprite_01.png',0.4),
				('sprites/fondo_basura/sprite_00.png',0.4),
				('sprites/fondo_basura/MOVE00.png',0.4),
				('sprites/fondo_basura/MOVE01.png',0.4),
				('sprites/fondo_basura/MOVE02.png',0.4),
				('sprites/fondo_basura/MOVE03.png',0.4),
				('sprites/fondo_basura/MOVE04.png',0.4),
				('sprites/fondo_basura/MOVE05.png',0.4),
				('sprites/fondo_basura/MOVE06.png',0.4),
				('sprites/fondo_basura/MOVE07.png',0.4),
				('sprites/fondo_basura/MOVE08.png',0.4),
				('sprites/fondo_basura/MOVE09.png',0.4),
				('sprites/fondo_basura/MOVE10.png',0.4),
				('sprites/fondo_basura/MOVE11.png',0.4),
				('sprites/fondo_basura/MOVE12.png',0.4),
				('sprites/fondo_basura/MOVE13.png',0.4),
				('sprites/fondo_basura/MOVE14.png',0.4),
				('sprites/fondo_basura/MOVE15.png',0.4)])

FONDOQUIMI = pyganim.PygAnimation([('sprites/fondo_quimico/sprite_28.png',0.4),
				('sprites/fondo_quimico/sprite_27.png',0.4),
				('sprites/fondo_quimico/sprite_26.png',0.4),
				('sprites/fondo_quimico/sprite_25.png',0.4),
				('sprites/fondo_quimico/sprite_24.png',0.4),
				('sprites/fondo_quimico/sprite_23.png',0.4),
				('sprites/fondo_quimico/sprite_22.png',0.4),
				('sprites/fondo_quimico/sprite_21.png',0.4),
				('sprites/fondo_quimico/sprite_20.png',0.4),
				('sprites/fondo_quimico/sprite_19.png',0.4),
				('sprites/fondo_quimico/sprite_18.png',0.4),
				('sprites/fondo_quimico/sprite_17.png',0.4),
				('sprites/fondo_quimico/sprite_16.png',0.4),
				('sprites/fondo_quimico/sprite_15.png',0.4),
				('sprites/fondo_quimico/sprite_14.png',0.4),
				('sprites/fondo_quimico/sprite_13.png',0.4),
				('sprites/fondo_quimico/sprite_12.png',0.4),
				('sprites/fondo_quimico/sprite_11.png',0.4),
				('sprites/fondo_quimico/sprite_10.png',0.4),
				('sprites/fondo_quimico/sprite_09.png',0.4),
				('sprites/fondo_quimico/sprite_08.png',0.4),
				('sprites/fondo_quimico/sprite_07.png',0.4),
				('sprites/fondo_quimico/sprite_06.png',0.4),
				('sprites/fondo_quimico/sprite_05.png',0.4),
				('sprites/fondo_quimico/sprite_04.png',0.4),
				('sprites/fondo_quimico/sprite_03.png',0.4),
				('sprites/fondo_quimico/sprite_02.png',0.4),
				('sprites/fondo_quimico/sprite_01.png',0.4),
				('sprites/fondo_quimico/sprite_00.png',0.4),
				('sprites/fondo_quimico/MOVE00.png',0.4),
				('sprites/fondo_quimico/MOVE01.png',0.4),
				('sprites/fondo_quimico/MOVE03.png',0.4),
				('sprites/fondo_quimico/MOVE04.png',0.4),
				('sprites/fondo_quimico/MOVE05.png',0.4),
				('sprites/fondo_quimico/MOVE06.png',0.4),
				('sprites/fondo_quimico/MOVE07.png',0.4),
				('sprites/fondo_quimico/MOVE08.png',0.4),
				('sprites/fondo_quimico/MOVE09.png',0.4),
				('sprites/fondo_quimico/MOVE10.png',0.4),
				('sprites/fondo_quimico/MOVE11.png',0.4),
				('sprites/fondo_quimico/MOVE12.png',0.4),
				('sprites/fondo_quimico/MOVE13.png',0.4),
				('sprites/fondo_quimico/MOVE14.png',0.4),
				('sprites/fondo_quimico/MOVE15.png',0.4),
				('sprites/fondo_quimico/MOVE16.png',0.4),
				('sprites/fondo_quimico/MOVE17.png',0.4),
				('sprites/fondo_quimico/MOVE18.png',0.4),
				('sprites/fondo_quimico/MOVE19.png',0.4),
				('sprites/fondo_quimico/MOVE20.png',0.4),
				('sprites/fondo_quimico/MOVE21.png',0.4),
				('sprites/fondo_quimico/MOVE22.png',0.4),
				('sprites/fondo_quimico/MOVE23.png',0.4),
				('sprites/fondo_quimico/MOVE24.png',0.4),
				('sprites/fondo_quimico/MOVE25.png',0.4),
				('sprites/fondo_quimico/MOVE26.png',0.4),
				('sprites/fondo_quimico/MOVE27.png',0.4),
				('sprites/fondo_quimico/MOVE28.png',0.4)])

GANAR = pyganim.PygAnimation([('sprites/monito/JUMP0.png',0.4),
				('sprites/monito/JUMP1.png',0.4),
				('sprites/monito/JUMP00.png',0.4),
				('sprites/monito/JUMP11.png',0.4)])

PERDER = pyganim.PygAnimation([('sprites/monito/LOSE1.png',0.4),
				('sprites/monito/LOSE2.png',0.4),
				('sprites/monito/LOSE3.png',0.4)])
# Cargan sonidos y musica
boop = pygame.mixer.Sound("efectos/select.wav")
uf = pygame.mixer.Sound("efectos/punch.wav")
musica = pygame.mixer.music.load("efectos/musicaa.mp3")
musica_pet = "efectos/musica_pet.mp3"
musica_quim = "efectos/musica_quim.mp3"
musica_basura = "efectos/musica_basura.mp3"
victoria = "efectos/victoria.mp3"
perderz = 'efectos/lose.mp3'
contador =+ 1

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
def boton(msg,x,y,ancho,alto,accion=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+ancho > mouse[0] > x and y+alto > mouse[1] > y:
		pantalla.blit(BOTON[0],(x,y))
		if click[0] == 1 and accion != None:
			accion()
		for evento in pygame.event.get():
			if evento.type == pygame.MOUSEBUTTONDOWN:
				click = pygame.mouse.get_pressed()
				boop.play(0)
		reloj.tick(60)
	else:
		pantalla.blit(BOTON[1], (x,y))
	smallText = pygame.font.SysFont("comicsansms",19)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ((x+58), (y+21))
	pantalla.blit(textSurf, textRect)
def botonimg(img,x,y,ancho,alto,accion=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+ancho > mouse[0] > x and y+alto > mouse[1] > y:
		accion()
	pantalla.blit(img,(x,y))
def botonimgclick(img,x,y,ancho,alto,accion1=None,accion2=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+ancho > mouse[0] > x and y+alto > mouse[1] > y:
		accion1()
		if click[0] == 1 and accion2 != None:
			accion2()
		for evento in pygame.event.get():
			if evento.type == pygame.MOUSEBUTTONDOWN:
				click = pygame.mouse.get_pressed()
				boop.play(0)
		reloj.tick(60)
	img.blit(pantalla,(x,y))
	img.play()
def Daniel():
	largeText = pygame.font.SysFont("comicsansms",60)
	TextSurf, TextRect = text_objects("Daniel Montes de Oca", largeText)
	TextRect.center = ((ANCHO/2),100)
	pantalla.blit(TextSurf, TextRect)
	smallText = pygame.font.SysFont("comicsansms",40)
	if lenguaje == 0:
		textSurf, textRect = text_objects("Software Engineering student", smallText)
	else:
		textSurf, textRect = text_objects("Estudiante de Ingeniería de Software", smallText)
	textRect.center = ((ANCHO/2), 190)
	pantalla.blit(textSurf, textRect)
	if lenguaje == 0:
		textSurf1, textRect1 = text_objects("Programming Leader", smallText)
	else:
		textSurf1, textRect1 = text_objects("Líder de programación", smallText)
	textRect1.center = ((ANCHO/2), 250)
	pantalla.blit(textSurf1, textRect1)
	if lenguaje == 0:
		textSurf2, textRect2 = text_objects("18 years old", smallText)
	else:
		textSurf2, textRect2 = text_objects("18 años", smallText)
	textRect2.center = ((ANCHO/2), 300)
	pantalla.blit(textSurf2, textRect2)
def Kevin():
	largeText = pygame.font.SysFont("comicsansms",60)
	TextSurf, TextRect = text_objects("Kevin Jesús González", largeText)
	TextRect.center = ((ANCHO/2),100)
	pantalla.blit(TextSurf, TextRect)
	smallText = pygame.font.SysFont("comicsansms",40)
	if lenguaje == 0:
		textSurf, textRect = text_objects("Software Engineering student", smallText)
	else:
		textSurf, textRect = text_objects("Estudiante de Ingeniería de Software", smallText)
	textRect.center = ((ANCHO/2), 190)
	pantalla.blit(textSurf, textRect)
	if lenguaje == 0:
		textSurf1, textRect1 = text_objects("Team Leader", smallText)
	else:
		textSurf1, textRect1 = text_objects("Líder de equipo", smallText)
	textRect1.center = ((ANCHO/2), 250)
	pantalla.blit(textSurf1, textRect1)
	if lenguaje == 0:
		textSurf2, textRect2 = text_objects("21 years old", smallText)
	else:
		textSurf2, textRect2 = text_objects("21 años", smallText)
	textRect2.center = ((ANCHO/2), 300)
	pantalla.blit(textSurf2, textRect2)
def Roberto():
	largeText = pygame.font.SysFont("comicsansms",60)
	TextSurf, TextRect = text_objects("Roberto Girón Castell", largeText)
	TextRect.center = ((ANCHO/2),100)
	pantalla.blit(TextSurf, TextRect)
	smallText = pygame.font.SysFont("comicsansms",40)
	if lenguaje == 0:
		textSurf, textRect = text_objects("Software Engineering student", smallText)
	else:
		textSurf, textRect = text_objects("Estudiante de Ingeniería de Software", smallText)
	textRect.center = ((ANCHO/2), 190)
	pantalla.blit(textSurf, textRect)
	if lenguaje == 0:
		textSurf1, textRect1 = text_objects("Documentation Leader", smallText)
	else:
		textSurf1, textRect1 = text_objects("Líder de documentación", smallText)
	textRect1.center = ((ANCHO/2), 250)
	pantalla.blit(textSurf1, textRect1)
	if lenguaje == 0:
		textSurf2, textRect2 = text_objects("18 years old", smallText)
	else:
		textSurf2, textRect2 = text_objects("18 años", smallText)
	textRect2.center = ((ANCHO/2), 300)
	pantalla.blit(textSurf2, textRect2)
def Diego():
	largeText = pygame.font.SysFont("comicsansms",60)
	TextSurf, TextRect = text_objects("Diego Salas Santoyo", largeText)
	TextRect.center = ((ANCHO/2),100)
	pantalla.blit(TextSurf, TextRect)
	smallText = pygame.font.SysFont("comicsansms",40)
	if lenguaje == 0:
		textSurf, textRect = text_objects("Software Engineering student", smallText)
	else:
		textSurf, textRect = text_objects("Estudiante de Ingeniería de Software", smallText)
	textRect.center = ((ANCHO/2), 190)
	pantalla.blit(textSurf, textRect)
	if lenguaje == 0:
		textSurf1, textRect1 = text_objects("Design Leader", smallText)
	else:
		textSurf1, textRect1 = text_objects("Líder de diseño", smallText)
	textRect1.center = ((ANCHO/2), 250)
	pantalla.blit(textSurf1, textRect1)
	if lenguaje == 0:
		textSurf2, textRect2 = text_objects("18 years old", smallText)
	else:
		textSurf2, textRect2 = text_objects("18 años", smallText)
	textRect2.center = ((ANCHO/2), 300)
	pantalla.blit(textSurf2, textRect2)
def Luis():
	largeText = pygame.font.SysFont("comicsansms",60)
	TextSurf, TextRect = text_objects("Luis F. Pérez Valdovinos", largeText)
	TextRect.center = ((ANCHO/2),100)
	pantalla.blit(TextSurf, TextRect)
	smallText = pygame.font.SysFont("comicsansms",40)
	if lenguaje == 0:
		textSurf, textRect = text_objects("Software Engineering student", smallText)
	else:
		textSurf, textRect = text_objects("Estudiante de Ingeniería de Software", smallText)
	textRect.center = ((ANCHO/2), 190)
	pantalla.blit(textSurf, textRect)
	if lenguaje == 0:
		textSurf1, textRect1 = text_objects("Testing Leader", smallText)
	else:
		textSurf1, textRect1 = text_objects("Líder de pruebas", smallText)
	textRect1.center = ((ANCHO/2), 250)
	pantalla.blit(textSurf1, textRect1)
	if lenguaje == 0:
		textSurf2, textRect2 = text_objects("18 years old", smallText)
	else:
		textSurf2, textRect2 = text_objects("18 años", smallText)
	textRect2.center = ((ANCHO/2), 300)
	pantalla.blit(textSurf2, textRect2)
def Profe():
	largeText = pygame.font.SysFont("comicsansms",60)
	TextSurf, TextRect = text_objects("Prof. Efraín Hernandez", largeText)
	TextRect.center = ((ANCHO/2),100)
	pantalla.blit(TextSurf, TextRect)
	smallText = pygame.font.SysFont("comicsansms",40)
	if lenguaje == 0:
		textSurf, textRect = text_objects("Teacher", smallText)
	else:
		textSurf, textRect = text_objects("Maestro", smallText)
	textRect.center = ((ANCHO/2), 190)
	pantalla.blit(textSurf, textRect)
	if lenguaje == 0:
		textSurf1, textRect1 = text_objects("Team tutor", smallText)
	else:
		textSurf1, textRect1 = text_objects("Tutor de equipo", smallText)
	textRect1.center = ((ANCHO/2), 250)
	pantalla.blit(textSurf1, textRect1)
def quitgame():
	pygame.quit()
	quit()
def unpause():
	global pause
	pause = False
def paused():
	global pause
	if (lenguaje==0):
		largeText = pygame.font.SysFont("comicsansms",115)
		TextSurf, TextRect = text_objects("PAUSE", largeText)
		TextRect.center = ((ANCHO/2),(ALTO/2))
		pantalla.blit(TextSurf, TextRect)
	else:
		largeText = pygame.font.SysFont("comicsansms",115)
		TextSurf, TextRect = text_objects("PAUSA", largeText)
		TextRect.center = ((ANCHO/2),(ALTO/2))
		pantalla.blit(TextSurf, TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause = False
					unpause()
		if (lenguaje==0):
			boton("CONTINUE",250,500,116,42,unpause)
			boton("BACK",400,500,116,42,game_intro)
			boton("LEVELS",550,500,116,42,seleccionar_niveles)
			boton("QUIT",700,500,116,42,quitgame)
		else:
			boton("CONTINUAR",250,500,116,42,unpause)
			boton("VOLVER",400,500,116,42,game_intro)
			boton("NIVELES",550,500,116,42,seleccionar_niveles)
			boton("SALIR",700,500,116,42,quitgame)
		pygame.display.update()
		reloj.tick(15)
def musica_on():
	global musi
	musi = 0
	game_intro()
def musica_off():
	global musi
	musi = 1
	game_intro()
def ingles():
	global lenguaje
	lenguaje = 0
def espanol():
	global lenguaje
	lenguaje = 1
def opciones():
	opc = True

	while opc:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pantalla.fill(white)
		if (lenguaje == 1):
			largeText = pygame.font.SysFont("comicsansms",115)
			TextSurf, TextRect = text_objects("OPCIONES", largeText)
			TextRect.center = ((ANCHO/2),100)
			pantalla.blit(TextSurf, TextRect)
			
			boton("VOLVER",800,300,116,42,game_intro)
			smallText = pygame.font.SysFont("comicsansms",25)
			txt, txtr = text_objects("MUSICA",smallText)
			txtr.center = (270,280)
			pantalla.blit(txt,txtr)
			boton("SI",150,300,116,42,musica_on)
			boton("NO",290,300,116,42,musica_off)
			txt0, txtr0 = text_objects("IDIOMA",smallText)
			txtr0.center = (570,280)
			pantalla.blit(txt0,txtr0)
			boton("INGLÉS",450,300,116,42,ingles)
			boton("ESPAÑOL",590,300,116,42,espanol)
		else:
			largeText = pygame.font.SysFont("comicsansms",115)
			TextSurf, TextRect = text_objects("OPTIONS", largeText)
			TextRect.center = ((ANCHO/2),100)
			pantalla.blit(TextSurf, TextRect)
			
			boton("BACK",800,300,116,42,game_intro)
			smallText = pygame.font.SysFont("comicsansms",25)
			txt, txtr = text_objects("MUSIC",smallText)
			txtr.center = (270,280)
			pantalla.blit(txt,txtr)
			boton("ON",150,300,116,42,musica_on)
			boton("OFF",290,300,116,42,musica_off)
			txt0, txtr0 = text_objects("LANGUAGE",smallText)
			txtr0.center = (570,280)
			pantalla.blit(txt0,txtr0)
			boton("ENGLISH",450,300,116,42,ingles)
			boton("SPANISH",590,300,116,42,espanol)

		pygame.display.update()
		reloj.tick(15)
def creditos():
	opc = True

	while opc:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pantalla.fill(white)
		largeText = pygame.font.SysFont("comicsansms",70)
		if (lenguaje==0):
			TextSurf, TextRect = text_objects("CREDITS", largeText)
		else:
			TextSurf, TextRect = text_objects("CREDITOS", largeText)
		TextRect.center = ((ANCHO/2),40)
		pantalla.blit(TextSurf, TextRect)

		botonimg(DANY,40,100,100,100,Daniel)
		botonimg(KEVS,40,210,100,100,Kevin)
		botonimg(ROBE,40,320,100,100,Roberto)
		botonimg(DIEGO,884,100,100,100,Diego)
		botonimg(LUIS,884,210,100,100,Luis)
		botonimg(Maestro,884,320,100,100,Profe)
		if (lenguaje==0):
			boton("BACK",(ANCHO/2-(100)),500,116,42,game_intro)
		else:
			boton("VOLVER",(ANCHO/2-(100)),500,116,42,game_intro)

		pygame.display.update()
		reloj.tick(15)
def FONDOBLIT():
	FONDO.blit(pantalla,(0,0))
	FONDO.play()
def FONDOBASBLIT():
	FONDOBAS.blit(pantalla,(0,0))
	FONDOBAS.play()
def FONDOQUIMBLIT():
	FONDOQUIMI.blit(pantalla,(0,0))
	FONDOQUIMI.play()
def game_intro():

	intro = True
	if musi == 0:
		if pygame.mixer.music.get_busy() == False:
			pygame.mixer.music.play()
	else:
		pygame.mixer.music.stop()
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		pantalla.blit(FONDO_MENU, (0,0))
		if (lenguaje==0):
			boton("PLAY",150,450,100,50,intro_anim)
			boton("QUIT",750,450,100,50,quitgame)
			boton("OPTIONS",350,450,100,50,opciones)
			boton("CREDITS",550,450,100,50,creditos)
		else:
			boton("JUGAR",150,450,100,50,intro_anim)
			boton("SALIR",750,450,100,50,quitgame)
			boton("OPCIONES",350,450,100,50,opciones)
			boton("CREDITOS",550,450,100,50,creditos)
		pygame.display.update()
		reloj.tick(15)
def seleccionar_niveles():

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		pantalla.blit(FONDO_MENU, (0,0))
		largeText = pygame.font.SysFont("comicsansms",100)
		if lenguaje == 0:
			TextSurf, TextRect = text_objects("SELECT LEVEL", largeText)
		else:
			TextSurf, TextRect = text_objects("SELECCIONAR NIVEL", largeText)
		TextRect.center = ((ANCHO/2),500)
		pantalla.blit(TextSurf, TextRect)
		botonimgclick(PETR,62,100,200,200,FONDOBLIT,pet)
		botonimgclick(QUIMQ,322,150,200,200,FONDOQUIMBLIT,quimico)
		botonimgclick(BASUR,662,100,200,200,FONDOBASBLIT,basura)
		botonimgclick(BACK,10,10,100,50,FONDOBLIT,game_intro)
		pygame.display.update()
		reloj.tick(15)

def intro_anim():
	anim = True
	while anim:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					anim = False
		pantalla.fill(white)
		minitext1 = pygame.font.SysFont("comicsansms",30)
		if lenguaje==0:
			ii,jj = text_objects("Press ENTER to continue", minitext1)
			pantalla.blit(INSTRUCTIONS,(112,0))
		else:
			ii,jj = text_objects("Presiona ENTER para continuar", minitext1)
			pantalla.blit(INSTRUCCIONES,(112,0))
		jj.center = ((ANCHO/2),(550))
		pantalla.blit(ii,jj)
		pygame.display.update()
		reloj.tick(15)
	seleccionar_niveles()
class Recs(object):
	def __init__(self,numeroinicial,x1,y1):
		self.lista=[]
		for x in range(numeroinicial):
			leftrandom=random.randrange(0,790)
			toprandom=random.randrange(-600,0) #<----------Linea donde se destruiran las entidades
			width=x1
			height=y1
			self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))
		
	def reagregar(self,x1,y1):
		for x in range(len(self.lista)):
			if self.lista[x].top > 600:
				leftrandom=random.randrange(0,790)
				toprandom=random.randrange(-600,0)
				width=x1
				height=y1
				self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height)) 

	def reagregar2(self,x1,y1):
		for x in range(len(self.lista)):
			leftrandom=random.randrange(0,790)
			toprandom=random.randrange(-600,0)
			width=x1
			height=y1
			self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height))

	def mover(self,velocidad):
		for rectangulo in self.lista:
			rectangulo.move_ip(0,10)

	def pintar (self,superficie,img):
		for rectangulo in self.lista:
			pantalla.blit(img,(rectangulo))

def colision(monito,recs):
	for rec in recs.lista:
		if monito.rect.colliderect(rec):
			return True
	return False

"""def imagenes_extras():
	global contador
	for contador in FONDOGAST:
		if contador +1:
			FONDOGAST"""
			
	
def ganar(fondo,enemigo,pos):
	win = True
	if pygame.mixer.music.get_busy() == True:
		pygame.mixer.music.stop()
	if musi == 0:
		pygame.mixer.music.load(victoria)
		pygame.mixer.music.play()
	while win:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				elif event.key == pygame.K_RETURN:
					seleccionar_niveles()
		
		fondo.blit(pantalla, (0,0))
		fondo.play()
		pantalla.blit(enemigo,(pos))
		GANAR.blit(pantalla, (450,420))
		GANAR.play()
		largeText = pygame.font.SysFont("comicsansms",80)
		minitext = pygame.font.SysFont("comicsansms",40)
		minitext1 = pygame.font.SysFont("comicsansms",60)
		if lenguaje==0:
			TextSurf, TextRect = text_objects("CONGRATULATIONS!", largeText)
			x,y = text_objects("You saved the water!", minitext1)
			i,j = text_objects("Press ENTER to select another level", minitext)
			ii,jj = text_objects("Press ESCAPE to quit", minitext)
		else:
			TextSurf, TextRect = text_objects("¡FELICIDADES!", largeText)
			x,y = text_objects("¡Salvaste el agua!", minitext1)
			i,j = text_objects("Presiona ENTER para seleccionar otro nivel", minitext)
			ii,jj = text_objects("Presiona ESCAPE para salir", minitext)
		TextRect.center = ((ANCHO/2),(100))
		y.center = ((ANCHO/2),(200))
		j.center = ((ANCHO/2),(300))
		jj.center = ((ANCHO/2),(350))
		pantalla.blit(TextSurf, TextRect)
		pantalla.blit(x,y)
		pantalla.blit(i,j)
		pantalla.blit(ii,jj)
		pygame.display.update()
		reloj.tick(15)
def perder(fondo):
	lose = True
	if pygame.mixer.music.get_busy() == True:
		pygame.mixer.music.stop()
	if musi == 0:
		pygame.mixer.music.load(perderz)
		pygame.mixer.music.play()
	while lose:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				elif event.key == pygame.K_RETURN:
					seleccionar_niveles()
		fondo.blit(pantalla, (0,0))
		fondo.play()
		PERDER.blit(pantalla, (450,420))
		PERDER.play()
		largeText = pygame.font.SysFont("comicsansms",115)
		minitext = pygame.font.SysFont("comicsansms",40)
		if lenguaje==0:
			TextSurf, TextRect = text_objects("YOU LOST", largeText)
			i,j = text_objects("Press ENTER to select another level", minitext)
			ii,jj = text_objects("Press ESCAPE to quit", minitext)
		else:
			TextSurf, TextRect = text_objects("PERDISTE", largeText)
			i,j = text_objects("Presiona ENTER para seleccionar otro nivel", minitext)
			ii,jj = text_objects("Presiona ESCAPE para salir", minitext)
		TextRect.center = ((ANCHO/2),(100))
		j.center = ((ANCHO/2),(220))
		jj.center = ((ANCHO/2),(280))
		pantalla.blit(TextSurf, TextRect)
		pantalla.blit(i,j)
		pantalla.blit(ii,jj)
		pygame.display.update()
		reloj.tick(15)

def pantalla_espanol():#<----------Pantalla que arroja un mensaje
	a = (random.randrange(3))#<----------Se genera un numero al azar

	#SE CONTEMPLAN LAS POSIdBLES OPCCIONES DEL NUMERO AL AZAR Y SE IMPRIME UNA IMAGEN DISTINTA EN CADA UNO
	if a == 1:
	    pantalla_de_carga = pygame.image.load("sprites/CARGANDO1.png")
	elif a == 2:
	    pantalla_de_carga = pygame.image.load("sprites/CARGANDO2.png")
	else:
	    pantalla_de_carga = pygame.image.load("sprites/CARGANDO3.png")

	pantalla.blit(pantalla_de_carga,(0, 0))#<----------Se imprime la pantalla de carga en la pantalla
	pygame.display.update()#<----------Se actualiza la pantalla
	time.sleep(3)#<----------Se pausa la aplicacion por un segundo

def pantalla_ingles():#<----------Pantalla que arroja un mensaje
	a = (random.randrange(3))#<----------Se genera un numero al azar

	#SE CONTEMPLAN LAS POSIBLES OPCCIONES DEL NUMERO AL AZAR Y SE IMPRIME UNA IMAGEN DISTINTA EN CADA UNO
	if a == 1:
	    pantalla_de_carga = pygame.image.load("sprites/LOADING8.png")
	elif a == 2:
	    pantalla_de_carga = pygame.image.load("sprites/LOADING9.png")
	else:
	    pantalla_de_carga = pygame.image.load("sprites/LOADING10.png")

	pantalla.blit(pantalla_de_carga,(0, 0))#<----------Se imprime la pantalla de carga en la pantalla
	pygame.display.update()#<----------Se actualiza la pantalla
	time.sleep(3)#<----------Se pausa la aplicacion por un segundo
class monito(pygame.sprite.Sprite):
	def __init__(self,x,y,ancho,alto):
		self.x = 20
		self.y = 420
		self.yy = self.y
		self.alto = alto
		self.ancho = ancho
		self.vel = 20
		self.walkCount = 0
		self.isJump = False
		self.jumpCount = 10
		self.standing = True
		self.left = False
		self.right = True
		self.asd = 4
		self.ANIM_SALTAR = 1
		self.golpe = False	
		self.hurt = False
		self.rect = pygame.rect.Rect((self.x, self.y, self.ancho, self.alto))

		#self.hitbox = (self.x+8,self.y, 80,100)
	def dibujar_monito(self,pantalla):
		if self.walkCount + 1 >= 16:
			self.walkCount = 0
		if not (self.standing):
			if self.left:
				if self.y == self.yy:
					pantalla.blit(WALKIZQ[self.walkCount//self.asd], (self.x,self.y))
					self.walkCount += 1
				else:
					pantalla.blit(JUMPIZQ[self.ANIM_SALTAR], (self.x,self.y))
			elif self.right:
				if self.y == self.yy:
					pantalla.blit(WALKDER[self.walkCount//self.asd], (self.x,self.y))
					self.walkCount +=1
				else:
					pantalla.blit(JUMPDER[self.ANIM_SALTAR], (self.x,self.y))
		elif (self.standing):
			if (self.y < self.yy):
				if self.right:
					pantalla.blit(JUMPDER[self.ANIM_SALTAR], (self.x,self.y))
				elif self.left:
					pantalla.blit(JUMPIZQ[self.ANIM_SALTAR], (self.x,self.y))
			elif self.y == self.yy:
				if self.left:
					pantalla.blit(IDLEIZQ, (self.x,self.y))
				elif self.right:
					pantalla.blit(IDLEDER, (self.x,self.y))
		if self.golpe:
			if self.left:
				pantalla.blit(ATTI, (self.x,self.y))
				self.golpe = False
			elif self.right:
				pantalla.blit(ATTD, (self.x,self.y))
				self.golpe = False
		if self.hurt:
			if self.left:
				pantalla.blit(HURTI,(self.x,self.y))
				self.hurt = False
			elif self.right:
				pantalla.blit(HURT,(self.x,self.y))
				self.hurt = False
		self.rect = pygame.rect.Rect((self.x, self.y, self.ancho, self.alto))
		#pygame.draw.rect(pantalla, (0,0,0), self.rect,2)
class VIDAS1(object):
	def __init__(self, x,y):
		self.x= x
		self.y= y
	def dibujar_vidas(self,pantalla):
		if vida1 == 3:
			pantalla.blit(VIDA, (self.x,self.y))
			pantalla.blit(VIDA, (self.x+65,self.y))
			pantalla.blit(VIDA, (self.x+130,self.y))	
		elif vida1 == 2:
			pantalla.blit(VIDA, (self.x,self.y))
			pantalla.blit(VIDA, (self.x+65,self.y))
		elif vida1 == 1:
			pantalla.blit(VIDA, (self.x,self.y))
class VIDAS_ENEM1(object):
	def __init__(self, x,y):
		self.x= x
		self.y= y
	def dibujar_vidas(self,pantalla):
		if vida_enem1 == 5:
			pantalla.blit(VIDAS_ENEM[1], (self.x-100,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x-20,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+220,self.y))
		elif vida_enem1 == 4:
			pantalla.blit(VIDAS_ENEM[1], (self.x-20,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+220,self.y))
		elif vida_enem1 == 3:
			pantalla.blit(VIDAS_ENEM[1], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+220,self.y))
		elif vida_enem1 == 2:
			pantalla.blit(VIDAS_ENEM[1], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[1], (self.x+220,self.y))
		elif vida_enem1 == 1:
			pantalla.blit(VIDAS_ENEM[1], (self.x+220,self.y))
class VIDAS2(object):
	def __init__(self, x,y):
		self.x= x
		self.y= y
	def dibujar_vidas(self,pantalla):
		if vida2 == 3:
			pantalla.blit(VIDA, (self.x,self.y))
			pantalla.blit(VIDA, (self.x+65,self.y))
			pantalla.blit(VIDA, (self.x+130,self.y))	
		elif vida2 == 2:
			pantalla.blit(VIDA, (self.x,self.y))
			pantalla.blit(VIDA, (self.x+65,self.y))
		elif vida2 == 1:
			pantalla.blit(VIDA, (self.x,self.y))
class VIDAS_ENEM2(object):
	def __init__(self, x,y):
		self.x= x
		self.y= y
	def dibujar_vidas(self,pantalla):
		if vida_enem2 == 5:
			pantalla.blit(VIDAS_ENEM[0], (self.x-100,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x-20,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+220,self.y))
		elif vida_enem2 == 4:
			pantalla.blit(VIDAS_ENEM[0], (self.x-20,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+220,self.y))
		elif vida_enem2 == 3:
			pantalla.blit(VIDAS_ENEM[0], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+220,self.y))
		elif vida_enem2 == 2:
			pantalla.blit(VIDAS_ENEM[0], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[0], (self.x+220,self.y))
		elif vida_enem2 == 1:
			pantalla.blit(VIDAS_ENEM[0], (self.x+220,self.y))
class VIDAS3(object):
	def __init__(self, x,y):
		self.x= x
		self.y= y
	def dibujar_vidas(self,pantalla):
		if vida3 == 3:
			pantalla.blit(VIDA, (self.x,self.y))
			pantalla.blit(VIDA, (self.x+65,self.y))
			pantalla.blit(VIDA, (self.x+130,self.y))	
		elif vida3 == 2:
			pantalla.blit(VIDA, (self.x,self.y))
			pantalla.blit(VIDA, (self.x+65,self.y))
		elif vida3 == 1:
			pantalla.blit(VIDA, (self.x,self.y))
class VIDAS_ENEM3(object):
	def __init__(self, x,y):
		self.x= x
		self.y= y
	def dibujar_vidas(self,pantalla):
		if vida_enem3 == 5:
			pantalla.blit(VIDAS_ENEM[2], (self.x-100,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x-20,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+220,self.y))
		elif vida_enem3 == 4:
			pantalla.blit(VIDAS_ENEM[2], (self.x-20,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+220,self.y))
		elif vida_enem3 == 3:
			pantalla.blit(VIDAS_ENEM[2], (self.x+60,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+220,self.y))
		elif vida_enem3 == 2:
			pantalla.blit(VIDAS_ENEM[2], (self.x+140,self.y))
			pantalla.blit(VIDAS_ENEM[2], (self.x+220,self.y))
		elif vida_enem3 == 1:
			pantalla.blit(VIDAS_ENEM[2], (self.x+220,self.y))
class PETROL(pygame.sprite.Sprite):
	def __init__(self,x,y,ancho,alto):
		self.alto = alto
		self.ancho = ancho
		self.x = x
		self.y = y
		self.image = pygame.Surface([self.ancho,self.alto])
		self.rect =self.image.get_rect()
	def dibujar_petroleo(self,pantalla):
		PETROLEO.blit(pantalla,(self.x,self.y))
		PETROLEO.play()
		self.hitbox = (self.x+10, self.y+100, 180,180)
		#pygame.draw.rect(pantalla, (0,0,0), self.hitbox,2)
class QUIMI(pygame.sprite.Sprite):
	def __init__(self,x,y,ancho,alto):
		self.alto = alto
		self.ancho = ancho
		self.x = x
		self.y = y
		self.image = pygame.Surface([self.ancho,self.alto])
		self.rect =self.image.get_rect()
	def dibujar_quimico(self,pantalla):
		QUIM.blit(pantalla,(self.x,self.y))
		QUIM.play()
		self.hitbox = (self.x+10, self.y+100, 180,180)
class BASU(pygame.sprite.Sprite):
	def __init__(self,x,y,ancho,alto):
		self.alto = alto
		self.ancho = ancho
		self.x = x
		self.y = y
		self.image = pygame.Surface([self.ancho,self.alto])
		self.rect =self.image.get_rect()
	def dibujar_basura(self,pantalla):
		BASURA.blit(pantalla,(self.x,self.y))
		BASURA.play()
		self.hitbox = (self.x+10, self.y+100, 300,300)
		#pygame.draw.rect(pantalla, (0,0,0), self.hitbox,2)
def DIBUJAR_PETROL():
	FONDO.blit(pantalla, (0,0))
	FONDO.play()
	petr.dibujar_petroleo(pantalla)
	p.dibujar_monito(pantalla)
	v1.dibujar_vidas(pantalla)
	V1.dibujar_vidas(pantalla)
	pantalla.blit(TRONC, (0,0))
	balas.pintar(pantalla,BALA)
	balas.reagregar(20,23)
	pygame.display.update()
def DIBUJAR_QUIM():
	FONDOQUIMI.blit(pantalla, (0,0))
	FONDOQUIMI.play()
	quim.dibujar_quimico(pantalla)
	p.dibujar_monito(pantalla)
	v2.dibujar_vidas(pantalla)
	V2.dibujar_vidas(pantalla)
	pantalla.blit(PILAR, (0,0))
	balas.pintar(pantalla,BALA1)
	balas.reagregar(20,23)
	pygame.display.update()
def DIBUJAR_BAS():
	FONDOBAS.blit(pantalla, (0,0))
	FONDOBAS.play()
	bas.dibujar_basura(pantalla)
	p.dibujar_monito(pantalla)
	v3.dibujar_vidas(pantalla)
	V3.dibujar_vidas(pantalla)
	balas.pintar(pantalla,BALA2)
	balas.reagregar(20,23)
	pygame.display.update()
p = monito(400,300,100,100)
v1 = VIDAS1(10,10)
v2 = VIDAS2(10,10)
v3 = VIDAS3(10,10)
V1 = VIDAS_ENEM1(674,10)
V2 = VIDAS_ENEM2(674,10)
V3 = VIDAS_ENEM3(674,10)
petr = PETROL(700,50,300,300)
quim = QUIMI(500,200,300,300)
bas = BASU(500,100,300,300)
vida1 = 3
vida2 = 3
vida3 = 3
vida_enem1 = 5
vida_enem2 = 5
vida_enem3 = 5
balas = Recs(10,20,23)
def pet():
	global pause
	global vida1
	global vida_enem1
	vida1=3
	vida_enem1=5

	if lenguaje == 0:
		pantalla_ingles()
	else:
		pantalla_espanol()

	if pygame.mixer.music.get_busy() == True:
		pygame.mixer.music.stop()
	if musi == 0:
		pygame.mixer.music.load(musica_pet)
		pygame.mixer.music.play()
	while True:
		reloj.tick(FPS)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause = True
					paused()
		if colision(p,balas):
			vida1 -= 1
			p.hurt = True
			uf.play(0)
			print(vida1)
			balas.reagregar2(20,23)
		if vida1 == 0:
			perder(FONDO)

		elif vida_enem1 == 0:
			ganar(FONDO,PET_VENCIDO,(630,320))

		#ANIMACION PARA SALTAR
		if p.y < 230:
			p.ANIM_SALTAR = 3

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			p.golpe = True
			if p.x >= 700 and p.y <= 350:
				print('hit')
				vida_enem1 -= 1
				p.x -= 500

		if keys[pygame.K_a] and p.x > p.vel:
			p.x -= p.vel
			p.left = True
			p.right = False
			p.standing = False
		elif keys[pygame.K_d] and p.x < ANCHO -300:
			p.x += p.vel
			p.right = True
			p.left = False
			p.standing = False
		else:
			p.standing = True
			p.walkCount = 0
		if not(p.isJump):
			if keys[pygame.K_w]:
				p.isJump = True
				p.ANIM_SALTAR =1
				p.walkCount = 0
		else:
			if p.jumpCount >= -10:
				neg = 1
				if p.jumpCount < 0:
					neg = -1
				p.y -= (p.jumpCount ** 2) * 0.5 * neg
				p.jumpCount -= 1
			else:
				p.isJump = False
				p.jumpCount = 10

		DIBUJAR_PETROL()
		balas.mover(4)
def quimico():
	global pause
	global vida2
	global vida_enem2
	vida2=3
	vida_enem2=5
	if lenguaje == 0:
		pantalla_ingles()
	else:
		pantalla_espanol()
	if pygame.mixer.music.get_busy() == True:
		pygame.mixer.music.stop()
	if musi == 0:
		pygame.mixer.music.load(musica_quim)
		pygame.mixer.music.play()
	run  = True
	while True:
		reloj.tick(FPS)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause = True
					paused()
		if colision(p,balas):
			vida2 -= 1
			p.hurt = True
			uf.play(0)
			print(vida2)
			balas.reagregar2(20,23)
		if vida2 == 0:
			perder(FONDOQUIMI)

		elif vida_enem2 == 0:
			ganar(FONDOQUIMI,QUIMICO_VENCIDO,(500,290))

		#ANIMACION PARA SALTAR
		if p.y < 230:
			p.ANIM_SALTAR = 3

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			p.golpe = True
			if p.x >= 600 and p.y >= 200:
				print('hit')
				vida_enem2 -= 1
				p.x -= 500
		if keys[pygame.K_a] and p.x > p.vel:
			p.x -= p.vel
			p.left = True
			p.right = False
			p.standing = False
		elif keys[pygame.K_d] and p.x < ANCHO -300:
			p.x += p.vel
			p.right = True
			p.left = False
			p.standing = False
		else:
			p.standing = True
			p.walkCount = 0
		if not(p.isJump):
			if keys[pygame.K_w]:
				p.isJump = True
				p.ANIM_SALTAR =1
				p.walkCount = 0
		else:
			if p.jumpCount >= -10:
				neg = 1
				if p.jumpCount < 0:
					neg = -1
				p.y -= (p.jumpCount ** 2) * 0.5 * neg
				p.jumpCount -= 1
			else:
				p.isJump = False
				p.jumpCount = 10
		DIBUJAR_QUIM()
		balas.mover(4)
def basura():
	global pause
	global vida3
	global vida_enem3
	vida3=3
	vida_enem3=5
	if lenguaje == 0:
		pantalla_ingles()
	else:
		pantalla_espanol()
	if pygame.mixer.music.get_busy() == True:
		pygame.mixer.music.stop()
	if musi == 0:
		pygame.mixer.music.load(musica_basura)
		pygame.mixer.music.play()
	run  = True
	while True:
		reloj.tick(FPS)
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause = True
					paused()
		if colision(p,balas):
			vida3 -= 1
			p.hurt = True
			uf.play(0)
			print(vida3)
			balas.reagregar2(20,23)
		if vida3 == 0:
			perder(FONDOBAS)

		elif vida_enem3 == 0:
			ganar(FONDOBAS,BASURA_VENCIDO,(550,320))

		#ANIMACION PARA SALTAR
		if p.y < 230:
			p.ANIM_SALTAR = 3

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			p.golpe = True
			if p.x >= 500 and p.y >= 100:
				print('hit')
				vida_enem3 -= 1
				p.x -= 500
		if keys[pygame.K_a] and p.x > p.vel:
			p.x -= p.vel
			p.left = True
			p.right = False
			p.standing = False
		elif keys[pygame.K_d] and p.x < ANCHO - p.ancho:
			p.x += p.vel
			p.right = True
			p.left = False
			p.standing = False
		else:
			p.standing = True
			p.walkCount = 0
		if not(p.isJump):
			if keys[pygame.K_w]:
				p.isJump = True
				p.ANIM_SALTAR =1
				p.walkCount = 0
		else:
			if p.jumpCount >= -10:
				neg = 1
				if p.jumpCount < 0:
					neg = -1
				p.y -= (p.jumpCount ** 2) * 0.5 * neg
				p.jumpCount -= 1
			else:
				p.isJump = False
				p.jumpCount = 10
		DIBUJAR_BAS()
		balas.mover(4)

game_intro()
mainloop()
pygame.quit()
quit()