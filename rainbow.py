import neopixel
import board
import time
import numpy as np


num_pixels = 2200

def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow_cycle(c,n,t):
	with neopixel.NeoPixel(board.D18,num_pixels, auto_write = False) as p:
		for j in range(n):
			for k in range(0,255,10):
				for i in range(num_pixels):
					pixel_index = (i * 256 // num_pixels) + k
					p[i] = wheel(pixel_index & 255)
				p.show()
				time.sleep(t)

rainbow_cycle((0,0,0),4,0.01)
