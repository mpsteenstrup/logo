import neopixel
import board
import time
import numpy as np
n=4
x = 0

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
p1 = neopixel.NeoPixel(board.D18, 2300)
p1.fill((55,55,55))
time.sleep(0.1)

def test():
	for x in range(0,23,2*n):
		print(x)
		p1.fill(R)
		p1[x:x+n] = [G]*n
		time.sleep(0.5)
	p1.fill((0,0,0))

	i = 1
	for j in range(4):
		p1[i:23+i:2]= [(255,255,255)]*len(p1[i:23+i:2])
		p1[1-i:23+1-i:2]= [(255,255,0)]*len(p1[1-i:23+1-i:2])
		time.sleep(0.1)
		i = (i+1) % 2
		print(i)
	p1.fill((0,0,0))


template = [G,G,G,G,R,R,R,R]
x = template*(23//len(template))
p1[:len(x)] = x
time.sleep(0.1)
x.reverse()
p1[:len(x)] = x
time.sleep(0.1)


x = [G]*(24//2)
x += [B]*(24//2)
p1[:len(x)] = x
time.sleep(1)




p1.fill(B)
p1.fill(G)
for j in range(0,23,n*2):
	p1[j:j+n] = [R]*4
