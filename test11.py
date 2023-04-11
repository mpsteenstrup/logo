import time
import board
import neopixel
import random

#pixels1 = neopixel.NeoPixel(board.D21, 685, brightness=1)
pixels1 = neopixel.NeoPixel(board.D21, 682, brightness=1)

for x in range(681):
	pixels1[random.randint(0,681)]=(random.randint(1,55),random.randint(1,55),random.randint(1,55))
for x in range(681):
	pixels1[random.randint(0,681)]=(0,0,0)
#time.sleep(1)
pixels1.fill((0, 0, 0))
