# NeoPixels must be connected to GPIO10, GPIO12, GPIO18 or GPIO21
import neopixel
import board
import time
import numpy as np
from datetime import datetime, timedelta

n1 = 24
n2 = 1
n3 = 0
n4 = 0

p1 = neopixel.NeoPixel(board.D18,n1)
p2 = neopixel.NeoPixel(board.D21,n2)

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
H = (255,255,255)
BL = (0,0,0)

p1.fill((100,100,100))

def half(c1,c2,t):
	x = [c1]*(n1//2)
	x += [c2]*(n1//2)
	p1[:len(x)] = x
	time.sleep(t)



def skift(c1,c2,t):
	template = [c1,c1,c1,c1,c2,c2,c2,c2]
	x = template*(n1//len(template))
	p1[:len(x)] = x
	time.sleep(t) 
	x.reverse()
	p1[:len(x)] = x 
	time.sleep(t) 



def blink(c, n, t):
	for j in range(n):
		p1.fill(c)
		time.sleep(t)
		p1.fill((0,0,0))
		time.sleep(t)
	p1.fill((0,0,0))

def pulsing(c, n, t):
	t1 = datetime.now()
	interval = np.power(np.arange(1.2,1.8,0.01),8)/256
	for j in range(n):
		for i in interval:
			p1.fill((i*c[0],i*c[1],i*c[2]))
			time.sleep(t)
			p1.show()
		for i in reversed(interval):
			p1.fill((i*c[0],i*c[1],i*c[2]))
			time.sleep(t)
			p1.show()
		d = datetime.now()-t1
		print(d)
	p1.fill((0,0,0))


def farve(c,n,t):
	p1.fill(c)
	time.sleep(t)

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
	for j in range(n):
		for k in range(0,255,10):
			for i in range(n1):
				pixel_index = (i * 256 // n1) + k
				p1[i] = wheel(pixel_index & 255)
			p1.show()
			time.sleep(t)
	p1.fill((0,0,0))


if __name__ == "__main__":
#	blink((0,255,0),4,0.1)
#	pulsing((0,255,0),1,0.01)
#	blink((255,0,0),4,0.1)
#	blink((0,0,255),4,0.1)
#	rainbow_cycle((0,0,0),2,0.01)
	skift(G,B,0.5)
	half(R,BL,1)
