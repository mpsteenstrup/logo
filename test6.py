import time
import board
import neopixel

#pixels1 = neopixel.NeoPixel(board.D21, 685, brightness=1)
pixels1 = neopixel.NeoPixel(board.D21, 800, brightness=1)

x=0

pixels.fill((255, 0, 0))
time.sleep(1)
pixels.fill((0, 0, 0))
