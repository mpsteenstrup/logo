import time
import board
import neopixel

#pixels1 = neopixel.NeoPixel(board.D21, 685, brightness=1)
pixels1 = neopixel.NeoPixel(board.D21, 1, brightness=1)

pixels1.fill((255, 0, 0))
time.sleep(0.5)
pixels1.fill((0,255, 0))
time.sleep(0.5)
pixels1.fill((0,0,255))
time.sleep(0.5)
pixels1.fill((55, 55, 55))
time.sleep(0.5)
pixels1.fill((255, 0, 0))
time.sleep(0.5)

pixels1.fill((0, 0, 0))
