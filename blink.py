import neopixel
import board
import time
import numpy as np

n1 = 23
n2 = 1

p1 = neopixel.NeoPixel(board.D18,n1)
p2 = neopixel.NeoPixel(board.D21,n2)

def blink(c, n, t):
	for j in range(n):
		p1.fill(c)
		p2.fill((255,0,0))
		time.sleep(t)
		p1.fill((0,0,0))
		p2.fill((0,0,0))
		time.sleep(t)
blink((0,255,0),4,0.1)
blink((255,0,0),4,0.1)
blink((0,0,255),4,0.1)
