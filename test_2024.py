import board
import neopixel
from time import sleep

n = 23
m = 0
p = neopixel.NeoPixel(board.D21, n, auto_write=False)
p[0] = (255, 0, 0)
p[9] = (0, 10, 0)
p.show()

while True:
        for i in range(n):
                p[(i+m)%n] = (i*10%255, (200-i*10)%255, 0)
        p.show()
        m += 1
        sleep(0.1)
        print(m)