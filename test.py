import neopixel
import board
import time

p = neopixel.NeoPixel(board.D21,10000)
p.fill((255,255,255))
time.sleep(1)



with neopixel.NeoPixel(board.D21,100) as p:
	p.fill((10,10,100))
	time.sleep(1)
	p.fill((10,100,10))
	time.sleep(1)


