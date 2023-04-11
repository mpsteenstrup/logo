import neopixel
import board
import time

RED = 0x100000 # (0x10, 0, 0) also works
n=4
x = 6
# Using ``with`` ensures pixels are cleared after we're done.
with neopixel.NeoPixel(board.D18, 23) as pixels:
#    pixels[::3] = [RED] * (len(pixels) // 2)
    pixels[x-n:x+n] = [(255,0,0)]*2*n
    time.sleep(0.5)
    x = 12
    pixels[x-n:x+n] = [(0,255,0)]*2*n
    time.sleep(0.5)
    pixels.fill((0,0,0))
