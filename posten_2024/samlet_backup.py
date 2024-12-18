# NeoPixels must be connected to GPIO10, GPIO12, GPIO18 or GPIO21
import neopixel
import board
import time
import numpy as np
import random
from datetime import datetime, timedelta

n1 = 1368

#n1 = 23
p1 = neopixel.NeoPixel(board.D21,n1, brightness=0.4)

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
H = (50,50,50)
Hfull =(255,255,255) 
Y = (255,255,0)
BL = (0,0,0)

p1.fill(BL)

def farve(c,n1,n):
	p1.fill(c)

switch = False
def skift(c1,c2,n):
	if n%200==0: # sætter hastigheden ned
		global switch
		template = [c1,c1,c1,c1,c1,c1,c1,c1,c1,c1,c2,c2,c2,c2,c2,c2,c2,c2]
		x = template*(n1//len(template))
		if switch:
			x.reverse()
		p1[:len(x)] = x
		switch =not switch

def pulsing(c,n1,n):
	n_stop=40 # højere tal giver langsommere pulsering
	range = 0.6
	minimum = 0.2
	n = n % n_stop
	print(n)
	brightness = abs(n-n_stop/2)/(n_stop/2)*range+minimum
	adjusted_color = (int(c[0]*brightness),int(c[1]*brightness),int(c[2]*brightness))
	p1.fill(adjusted_color)


def generate_random_numbers(n, n1):
	return [random.randint(0, n1 - 1) for _ in range(n)]

def randomPixel(c,antal, n):
	n1 = 23
	n = 4
	liste = generate_random_numbers(n,n1)
	x = [BL]*n1
	for k in liste:
		x[k] = c
	p1[:n1] = x

def randomFarve(c,antal, n):
	n1 = 23
	n = 4
	liste = generate_random_numbers(n,n1)
	x = [BL]*n1
	c = [H,R,B,G,Y]
	for k in liste:
		x[k] = random.choice(c)
	p1[:n1] = x


def blink(c,n):
	p1.fill(c)
	time.sleep(0.1)
	return n

def blinkSH():
	c = (255,255,255)
	p1.fill(c)



def half(c1,c2):
	x = [c1]*(n1//2)
	x += [c2]*(n1//2)
	p1[:len(x)] = x

def pulse(n):
        c = (255-n,0,0) 
        p1.fill(c)
        return n-10

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

def reggae(c1,c2,c3,c4,t):
    x = [c1]*(683)
    x += [c2]*(173)
    x += [c3]*(130)
    x += [c2]*(174)
    x += [c3]*(130)
    x += [c4]*(81)
    p1[:len(x)] = x
    time.sleep(t)

if __name__ == "__main__":
#	blink(H,4,0.1)

#	blink((255,0,0),4,1)
#    pulsing((255,255,255),20,0.01)
#	blink((255,0,0),4,0.1)
#	blink((0,0,255),4,0.1)

#    randomPixel(200)
#    reggae(G,Y,R,R,1)
#    rainbow_cycle(B,2,0.01)
#    reggae(G,Y,R,R,1)
    skift(R,H)
#	farve((100,100,100),1,1)

#        half(B,R)
