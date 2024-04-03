import neopixel
import board
import time
import random


# G R B

while True:
	with neopixel.NeoPixel(board.D21, 1368,bpp=3, brightness=0.1) as p:

		for j in range(10):
			p.fill((100,100,100))
			time.sleep(0.2)
			p.fill((0,0,0))
			time.sleep(0.06)
		for j in range(10):
			p.fill((255,255,255))
			time.sleep(0.1)
			p.fill((0,0,0))
			time.sleep(0.1)
			
		time.sleep(1)
		p.fill((100,100,100))
		time.sleep(60*60*5)


