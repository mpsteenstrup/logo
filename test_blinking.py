import time
import board
import neopixel

p = neopixel.NeoPixel(board.D21, 600, brightness=1)

p[::5] = (0,0,200)
time.sleep(1)

for i in range(23):
	p[i]=(255, 0, 0)

#	time.sleep(0.001)

p[0] = (0,255,0)
p[1] = (0,255,0)
p[2] = (0,255,0)
p[3] = (0,255,0)
p[4] = (0,255,0)
p[5] = (0,255,0)
p[6] = (0,255,0)
p[7] = (0,255,0)
p[8] = (0,255,0)
p[9] = (0,255,0)

p.fill((0, 0, 0))
