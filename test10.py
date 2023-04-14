import time
import board
import neopixel

#pixels1 = neopixel.NeoPixel(board.D21, 685, brightness=1)
pixels1 = neopixel.NeoPixel(board.D18, 1800, brightness=1)

#c = (2*(100,0,0))
#for i in range(1):
#	pixels1.fill(c)
#	time.sleep(0.5)
#	pixels1.fill((0,255, 0))
#	time.sleep(0.5)
#	pixels1.fill((0,0,255))
#	time.sleep(0.5)
#	pixels1.fill((55, 55, 55))
#	time.sleep(0.5)
#	pixels1.fill((255, 0, 0))
#	time.sleep(0.5)

pixels1.fill((255,255,255))
time.sleep(2)
pixels1.fill((0, 0, 0))
