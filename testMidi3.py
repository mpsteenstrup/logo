import pygame.midi
import time
from samlet import *

def readInput(input_device):
	blink((255,0,0),1,0.1)
	c = 100

	while True:
		try:
			if input_device.poll():
					event = input_device.read(3)
					c = event[0][0][1]
					print(c)
			if c == 1:
				blink((100,100,100),1,0.1)
				c  = 100
			if c == 2:
				blink(R,1,0.1)
				c  = 100
			if c == 3:
				blink(G,1,0.1)
				c  = 100
			if c == 4:
				farve(R,1,0.01)
			if c == 5:
				rainbow_cycle(R,4,0.01)
			if c == 6:
				skift(R,H,0.4)
			if c == 7:
				pulsing(B,4,0.01)
			if c == 8:
				half(B,G,0.01)
			if c == 9:
				half(G,B,0.01)
			if c == 0:
				blink(BL,1,0.01)

		except Exception as e:
			print(e)
			pulsing((255,255,255),300,0.2)
			time.sleep(1)
			break

def connectMidi():
	try:
		pygame.midi.init()
		my_input = pygame.midi.Input(3) #only in my case the id is 
		readInput(my_input)
#		test(my_input)

	except:
		print('no device connected')

connectMidi()
