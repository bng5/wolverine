# -*- coding: utf-8 -*-

import pygame, sys, os
from pygame.locals import *

SCREEN_WIDTH  = 296
SCREEN_HEIGHT = 222

def load_image(name, colorkey = False):    
	fullname = os.path.join("Datos", name)
	try: image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'No se puede cargar la imagen: ', fullname
		raise SystemExit, message
	image = image.convert()
	if(colorkey): 
		colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()


"""
obtenido de http://www.pygame.org/wiki/tut_design?parent=tutorials#hModel
"""
class Event:
	"""esta es la super-clase para todos los eventos generados
	por un objeto y enviados al EventosManejador"""
	def __init__(self):
			self.nombre = "Evento Generico"
			#self.tipo = 

class EventoTeclado(Event):
	def __init__(self, evento):#, tipo, tecla):
		self.tipo = evento.type#tipo
		self.tecla = evento.key#tecla

class TickEvent(Event):
	def __init__(self):
		self.nombre = "Evento Tick"	

class EventManager:
	"""this object is responsible for coordinating most communication
	between the Model, View, and Controller."""
	def __init__(self ):
		from weakref import WeakKeyDictionary
		self.listeners = {}#WeakKeyDictionary()
	#----------------------------------------------------------------------
	def Registrar(self, personaje, tecla):
		self.listeners[tecla] = {}
		self.listeners[tecla][ personaje ] = 1
	def RegisterListener( self, listener ):
		self.listeners[ listener ] = 1
	#----------------------------------------------------------------------
	def UnregisterListener( self, listener ):
		if listener in self.listeners.keys():
			del self.listeners[ listener ]
	#----------------------------------------------------------------------
	def Notificar( self, event ):
		if event.tecla in self.listeners.keys():
			for listener in self.listeners[event.tecla].keys():
				#NOTE: If the weakref has died, it will be 
				#automatically removed, so we don't have 
				#to worry about it.
				listener.uUpdate( event )


class KeyboardController:
	def Notify(self, event):
		if isinstance( event, TickEvent ):
			#Handle Input Events
			print "KeyboardController.Notify"

class CPUSpinnerController:
	global evManager
	keepGoing = True
	def Run(self):
		while self.keepGoing:
			event = TickEvent()
			evManager.Post( event )
	def Notify(self, event):
		if isinstance( event, QuitEvent ):
			self.keepGoing = 0


class PygameView:
	def Notify(self, event):
		if isinstance( event, TickEvent ):
			#Draw Everything
			print "PygameView.Notify"

 


"""
def main2():
	evManager = EventManager()
	keybd = KeyboardController()
	spinner = CPUSpinnerController()
	pygameView = PygameView()
	evManager.RegisterListener( keybd )
	evManager.RegisterListener( spinner )
	evManager.RegisterListener( pygameView )
	spinner.Run()
"""






class Wolverine(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("wolverine.gif", True)
		self.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
		self.estado = 0
		self.frame = 0
		self.mapa = {}
		self.mapa[0] = {}
		self.mapa[0][0] = (2, 5, 60, 60)
		self.mapa[0][1] = (67, 6, 60, 60)
		self.mapa[0][2] = (129, 4, 60, 60)
		self.mapa[0][3] = (67, 6, 60, 60)
		self.mapa[1] = {}
		self.mapa[1][0] = (2, 433, 60, 60)
		self.mapa[1][1] = (67, 433, 60, 60)
		self.mapa[1][2] = (129, 433, 60, 60)
		self.mapa[1][3] = (198, 433, 60, 60)
		self.mapa[1][4] = (264, 433, 60, 60)
		self.mapa[1][5] = (324, 433, 60, 60)
		self.mapa[2] = {}
		self.mapa[2][0] = (8, 705, 55, 47)
	def caminar(self, direccion):
		self.estado = 1
	def parar(self):
		self.estado = 0
	def agachar(self):
		self.estado = 2
	def update(self, screen):
		#print self.estado
		self.frame = self.frame + 1
		if self.frame >= len(self.mapa[self.estado]):
			self.frame = 0
		screen.blit(self.image, (100,150), self.mapa[self.estado][self.frame])
	def uUpdate(self, evento):
		print evento.tipo ,' ', evento.tecla












def main():
	pygame.init()
	pygame.mouse.set_visible(False)
	#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#, FULLSCREEN|HWSURFACE|DOUBLEBUF)#NOFRAME, 8)
	pygame.display.set_caption("Wolverine")
	# Creamos el fondo
	background_image, background_rect = load_image("tmnt4-street.png")
	screen.blit(background_image, (0,0))
	evManager = EventManager()
	#screen.fill((233,233,233))
	# Inicializamos el X-wing del jugador
	personajeSprite = pygame.sprite.RenderClear()
	personaje = Wolverine()
	personajeSprite.add(personaje)

	evManager.Registrar(personaje, K_LEFT)
	# y sus lasers !!! xwingLaserSprites = pygame.sprite.RenderClear()
	# Inicializamos algunas variables de control
	running = True
	clock = pygame.time.Clock()
	frame = 0
	while running is True:
		clock.tick(1) # frames por segundo
		i = 0
		# Controles de teclado
		for event in pygame.event.get():
			#evManager.Notificar(EventoTeclado(event.type, event.key))
			#ev = EventoTeclado(event.type, event.key)
			i = i + 1
			if event.type == KEYDOWN or event.type == KEYUP:
				evManager.Notificar(EventoTeclado(event))#.type, event.key))
				#print "--> ",i," ",event.type," - ",event.key
			if event.type == QUIT:
				running = False # Se acaba el juego
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False # Se acaba el juego
		screen.blit(background_image, (0, 0))
		personajeSprite.update(screen)
		pygame.display.update()
	#Fin del juego
	raise SystemExit

#Esta linea lanza la funcion principal si aun no esta lanzada
if __name__ == '__main__': main()

