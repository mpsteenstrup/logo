import time
import board
import neopixel
n = 100
#pixels1 = neopixel.NeoPixel(board.D21, 685, brightness=1)
p1 = neopixel.NeoPixel(board.D18, n, auto_write=False)

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

p1[:] = [(255,0,0)]*1368
p1.show()
time.sleep(2)
#p1.fill((0, 0, 0))
#p1.show()
p1[:] = [(255,0,0)]*1368
time.sleep(1)
p1.show()
time.sleep(2)
p1[:] = [(0,255,0)]*1368
time.sleep(0.1)
p1.show()
time.sleep(2)
p1.fill((255,255,255))
time.sleep(0.1)
p1.show()
time.sleep(2)
p1.fill((0, 0, 0))
p1.show()
