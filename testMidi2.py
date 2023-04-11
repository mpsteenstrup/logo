import pygame.midi
import time

def readInput(input_device):
	while True:
		try:
	        	if input_device.poll():
        	    		event = input_device.read(3)
            			print (event[0][0][1])
		except:
			print('no device connected')
			time.sleep(1)
			readInput(input_device)

if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(3) #only in my case the id is 
    readInput(my_input)
