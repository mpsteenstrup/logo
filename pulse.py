import neopixel
import board
import time
import numpy as np

def pulsing(c, n, t):
	interval = np.power(np.arange(1.4,2,0.01),8)/256
	with neopixel.NeoPixel(board.D21,100) as p:
		for j in range(n):
			for i in interval:
				p.fill((i*c[0],i*c[1],i*c[2]))
				time.sleep(t)
			for i in reversed(interval):
				p.fill((i*c[0],i*c[1],i*c[2]))
				time.sleep(t)

pulsing((0,255,0),4,0.1)
