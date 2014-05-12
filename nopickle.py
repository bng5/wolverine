import pygame, pickle
from pygame.locals import *

pygame.init()
pygame.display.set_mode((100, 100))
#controles = {'arriba': '', 'abajo': '', 'derecha': '', 'izquierda': ''}
in_s = open('./controles.pkl', 'rb')
controles = pickle.load(in_s)
print controles
in_s.close()


"Joystick"
i = 0
while i < pygame.joystick.get_count():
	joystick = pygame.joystick.Joystick(i)
	joystick.init()
	print "\033[4mName\033[0m: ", joystick.get_name()
	print "\033[4mInit\033[0m: ",joystick.get_init()
	print "\033[4mId\033[0m: ",joystick.get_id()
	print "\033[4mNumaxes\033[0m: ",joystick.get_numaxes()
	print "\033[4mNumballs\033[0m: ",joystick.get_numballs()
	#print "Ball: ",joystick.get_ball()
	print "\033[4mNumbuttons\033[0m: ",joystick.get_numbuttons()
	#print "Button: ",joystick.get_button()
	print "\033[4mNumhats\033[0m: ",joystick.get_numhats()
	#print "Hat: ",joystick.get_hat()
	i += 1
	

for k in controles.keys():
	print k, " ", pygame.key.name(controles[k])
	continuar = False
	while continuar is False:
		event = pygame.event.wait()
		if event.type == KEYDOWN:
			controles[k] = event.key
			continuar = True
			print pygame.key.name(event.key)
		elif event.type == pygame.JOYAXISMOTION:
			print "\033[1mJOYAXISMOTION\033[0m"
			print "\033[2;4mjoy\033[0m 0: ",event.joy
			print "\033[2;4maxis\033[0m 0: ",event.axis
			print "\033[2;4mvalue\033[0m 0: ",event.value
			print "\033[2;4mAxis\033[0m 0: ",joystick.get_axis(0)
			print "\033[2;4mAxis\033[0m 1: ",joystick.get_axis(1)
		elif event.type == pygame.JOYBALLMOTION:
			print "\033[1mJOYBALLMOTION\033[0m"
			print "\033[2;4mjoy\033[0m 0: ",event.joy
			print "\033[2;4mball\033[0m 0: ",event.ball
			print "\033[2;4mrel\033[0m 0: ",event.rel
		elif event.type == pygame.JOYHATMOTION:
			print "\033[1mJOYHATMOTION\033[0m"
			print "\033[2;4mjoy\033[0m 0: ",event.joy
			print "\033[2;4mhat\033[0m 0: ",event.hat
			print "\033[2;4mvalue\033[0m 0: ",event.value
		elif event.type == pygame.JOYBUTTONDOWN:
			print "\033[1mJOYBUTTONDOWN\033[0m"
			print "\033[2;4mjoy\033[0m 0: ",event.joy
			print "\033[2;4mbutton\033[0m 0: ",event.button
			controles[k] = event.button
			#continuar = True
		elif event.type == pygame.JOYBUTTONUP:
			print "\033[1mJOYBUTTONUP\033[0m"
			print "\033[2;4mjoy\033[0m 0: ",event.joy
			print "\033[2;4mbutton\033[0m 0: ",event.button


output = open('./controles.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(controles, output)
output.close()


