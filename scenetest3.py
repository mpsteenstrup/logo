import neopixel
import board
import time
import random



with neopixel.NeoPixel(board.D21, 1368,bpp=3, brightness=1) as p:
	p.fill((80,80,80))
	time.sleep(1)
	p.fill((250,0,0))
	time.sleep(1)
	p.fill((0,250,0))
	time.sleep(1)
	p.fill((0,0,250))
	time.sleep(1)
	p.fill((80,80,80))
	time.sleep(100)


