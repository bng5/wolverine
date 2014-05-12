import pygame
from pygame.locals import *
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
		print self.estado
		self.frame = self.frame + 1
		if self.frame >= len(self.mapa[self.estado]):
			self.frame = 0
		screen.blit(self.image, (100,150), self.mapa[self.estado][self.frame])
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