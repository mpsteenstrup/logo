import pygame.midi
import time
from samlet import *

def readInput(input_device):
	blink((255,255,255),4,0.1)
	while True:
		try:
			if input_device.poll():
				event = input_device.read(3)
				print (event[0][0][1])
				if event[0][0][1] == 1:
					blink((255,255,255),1,0.1)
				if event[0][0][1] == 2:
					blink((255,0,0),1,0.1)
				if event[0][0][1] == 3:
					blink((0,0,255),1,0.1)
				if event[0][0][1] == 7:
					pulsing((255,255,255),4,0.01)
				if (event[0][0][1]) == 0:
					print('done')
					break
		except:
			print('error')
			pulsing((255,255,255),300,0.2)
			time.sleep(1)
			break
#			connectMidi()


def connectMidi():
	try:
		pygame.midi.init()
		my_input = pygame.midi.Input(3) #only in my case the id is 
		readInput(my_input)
	except:
		print('no device connected')

connectMidi()
