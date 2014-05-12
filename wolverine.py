# -*- coding: utf-8 -*-

import pygame, sys, os#, Clases
from pygame.locals import *
#from Clases import Wolverine

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 768

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


## clase a revisar
class Spritesheet:
	def __init__(self, filename, colorkey = False):
		self.sheet = pygame.image.load(os.path.join('data', filename)).convert()
	def imgat(self, rect, colorkey = None):
		rect = Rect(rect)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0, 0))
			image.set_colorkey(colorkey, RLEACCEL)
		return image
	def imgsat(self, rects, colorkey = None):
		imgs = []
		for rect in rects:
			imgs.append(self.imgat(rect, colorkey))
		return imgs







class Wolverine(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("wolverine2.gif")#, True)
		self.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
		self.estado = 3
		self.frame = 0
		self.posX = 100
		self.posY = -45
		self.velocidadY = 1.5
		self.mapa = {}
		self.mapa[0] = {}
		self.mapa[0][0] = (0, 5, 60, 60)
		self.mapa[0][1] = (0, 5, 60, 60)
		self.mapa[0][2] = (60, 5, 60, 60)
		self.mapa[0][3] = (60, 5, 60, 60)
		self.mapa[0][4] = (120, 5, 60, 60)
		self.mapa[0][5] = (120, 5, 60, 60)
		self.mapa[0][6] = (60, 5, 60, 60)
		self.mapa[0][7] = (60, 5, 60, 60)
		self.mapa[1] = {}
		self.mapa[1][0] = (2, 430, 60, 60)
		self.mapa[1][1] = (2, 430, 60, 60)
		self.mapa[1][2] = (60, 430, 60, 60)
		self.mapa[1][3] = (60, 430, 60, 60)
		self.mapa[1][4] = (120, 430, 60, 60)
		self.mapa[1][5] = (120, 430, 60, 60)
		self.mapa[1][6] = (180, 430, 60, 60)
		self.mapa[1][7] = (180, 430, 60, 60)
		self.mapa[1][8] = (240, 430, 60, 60)
		self.mapa[1][9] = (240, 430, 60, 60)
		self.mapa[1][10] = (2, 430, 60, 60)
		self.mapa[1][11] = (2, 430, 60, 60)
		self.mapa[1][12] = (300, 430, 60, 60)
		self.mapa[1][13] = (300, 430, 60, 60)
		self.mapa[2] = {}
		self.mapa[2][0] = (7, 690, 60, 60)
		self.mapa[3] = {}
		self.mapa[3][0] = (125, 497, 49, 84)
		self.mapa[4] = {}
		self.mapa[4][0] = (170, 497, 75, 84)
	def caminar(self, direccion):
		self.estado = 1
	def parar(self):
		self.estado = 0
	def agachar(self):
		self.estado = 2
	def update(self, screen):
		if self.estado == 1:
			self.posX = self.posX +6
		if self.estado >= 3:
			self.posX = self.posX +2
			self.velocidadY = self.velocidadY * 1.08
			self.posY = self.posY + self.velocidadY
			if self.posY >= 245:
				self.estado = 4
			if self.posY >= 685:
				self.estado = 0
		print self.estado
		self.frame = self.frame + 1
		if self.frame >= len(self.mapa[self.estado]):
			self.frame = 0
		screen.blit(self.image, (self.posX,self.posY), self.mapa[self.estado][self.frame])
		#screen.blit(self.image, (100,100), self.mapa[self.estado][self.frame])
		"""
		self.rect.move_ip((self.x_direccion * self.velocidad, self.y_direccion * self.velocidad))
		#print (self.x_direccion * self.velocidad)," " ,(self.y_direccion * self.velocidad)
		# Limites para que no se salga de la pantalla
		if self.rect.right < 0:
			self.rect.left = SCREEN_WIDTH
		elif self.rect.left > SCREEN_WIDTH:
			self.rect.right = 0
		if self.rect.bottom < 0:
			self.rect.top = SCREEN_HEIGHT
			#0
			" " " elif self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT " " "
		elif self.rect.top >= SCREEN_HEIGHT:
			self.rect.top = 0
			#
		
		if(self.acelerar == True and (self.velocidad < self.max_velocidad)):
			self.velocidad *= 1.08
		elif(self.acelerar == False and self.velocidad != 0):
			if(self.velocidad < 1):
				self.velocidad = 0
			else:
				self.velocidad /= 1.04

		# Rotar
		if self.rotar != 0:
			#print "rotar: ", self.rotar
			center = self.rect.center
			self.giro = self.giro + (4 * self.rotar)
			if self.giro >= 360:
				self.giro = 0
				self.image = self.original
			elif self.giro < 0:
				self.giro = (360 + self.giro)
				self.image = self.original
			self.image = pygame.transform.rotate(self.original, self.giro)
			#print self.x_direccion, " - " , self.giro #: " ,self.giro, " - rotar: ",self.rotar
			self.rect = self.image.get_rect(center=center)
			#print self.giro
			
			self.radianes = self.giro * math.pi / 180
			self.x_direccion = -(math.sin(self.radianes) * 1)
			self.y_direccion = -(math.cos(self.radianes) * 1)

			radianesTiro = (self.giro+90) * math.pi / 180
			self.disp_inicio[0] = -(math.sin(radianesTiro) * 29)
			self.disp_inicio[1] = -(math.cos(radianesTiro) * 29)

			radianesTiro = (self.giro-90) * math.pi / 180
			self.disp_inicio[2] = -(math.sin(radianesTiro) * 29)
			self.disp_inicio[3] = -(math.cos(radianesTiro) * 29)
			"""






"""
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   # Modificar posición en función de la tecla pulsada
   teclasPulsadas = pygame.key.get_pressed()
   if teclasPulsadas[K_LEFT]:
       pos = pos - 1
   if teclasPulsadas[K_RIGHT]:
       pos = pos + 1
   # Dibujar el fondo de color
   visor.fill((233,233,233))
   # Dibujar a Guy
   visor.blit(guy, (pos,100))
   # Volcar la surface en la ventana de pygame
   pygame.display.update()
"""
















def main():
	pygame.init()
	#pygame.mouse.set_visible(False)

	"""
	pygame.FULLSCREEN    create a fullscreen display
	pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
	pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
	pygame.OPENGL        create an opengl renderable display
	pygame.RESIZABLE     display window should be sizeable
	pygame.NOFRAME       display window will have no border or controls
	"""
	#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)#FULLSCREEN|HWSURFACE|DOUBLEBUF)#NOFRAME, 8)
	pygame.display.set_caption("Wolverine")
	# Creamos el fondo
	background_image, background_rect = load_image("fondo.png")#tmnt4-street.png", True)
	screen.blit(background_image, (0,0))
	#screen.fill((233,233,233))
	# Inicializamos el X-wing del jugador
	personajeSprite = pygame.sprite.RenderClear()
	personaje = Wolverine()
	personajeSprite.add(personaje)
	# y sus lasers !!! xwingLaserSprites = pygame.sprite.RenderClear()
	# Inicializamos algunas variables de control
	running = True
	clock = pygame.time.Clock()
	frame = 0
	while running is True:
		clock.tick(20) # frames por segundo
		# Controles de teclado
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False # Se acaba el juego
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False # Se acaba el juego
				elif event.key == K_LEFT:
					personaje.caminar(1)
					#xwing.acelerar = True
				elif event.key == K_RIGHT:
					personaje.caminar(-1)
					#xwing.image = pygame.transform.flip(xwing.image, 1, 0)
					##xwing.x_velocity = 2
					#xwing.acelerar = True
				elif event.key == K_UP:
					personaje.velocidad = 1
					personaje.acelerar = True
				elif event.key == K_DOWN:
					#xwing.velocidad = -2
					personaje.agachar()
				#elif event.key == K_SPACE:	
					##xwingLaserSprites.add(XWingLaser(xwing, 0))
					##xwingLaserSprites.add(XWingLaser(xwing, 2))
					#.rect.midtop, xwing.x_direccion, xwing.y_direccion, xwing.giro))
			elif event.type == KEYUP:
				if event.key == K_LEFT:
					personaje.parar()
				elif event.key == K_RIGHT:
					#xwing.image = pygame.transform.flip(xwing.image, 1, 0)
					personaje.parar()
				elif event.key == K_UP:
					#xwing.velocidad = 0
					personaje.acelerar = False
				elif event.key == K_DOWN:
					personaje.parar()
		# Actualizamos todos los sprites (Todavia no lo mostramos en pantalla)
		#xwingLaserSprites.update()
		# Limpiamos todo lo que fue pintado la ultima vez
		#xwingLaserSprites.clear( screen, background_image)
		#personajeSprite.clear(screen, background_image )
		# Pinta todo
		#xwingLaserSprites.draw( screen )
		#screen.blit(personaje.image, (100,100), personaje.mapa[personaje.estado][personaje.frame])
		##personajeSprite.draw( screen )
		##pygame.display.update()#flip()
		#screen.fill((233,233,233))
		screen.blit(background_image, (0, 0))
		personajeSprite.update(screen)
		pygame.display.update()
	#Fin del juego
	raise SystemExit
#Esta linea lanza la funcion principal si aun no esta lanzada
if __name__ == '__main__': main()