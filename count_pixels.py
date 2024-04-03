import time
import board
import neopixel
import numpy as np
p1 = neopixel.NeoPixel(board.D21, 1800, brightness=0.3)
n = 1367
#x1 = slice(0,61)
#x2 = slice(61,277)
#x3 = slice(277,339)
#x4 = slice(339,402)
#x5 = slice(402,620)
#x5 = slice(620,682)
#x6 = slice(682,856)
#x6 = slice(856,988)
#x7 = silice(988,1162)
#x8 = slice(1162,1292)
#x9 = slice(1292,1330)
#x10 = slice(1330,1368)
slicing = [slice(0,61),slice(61,277),slice(277,339),slice(339,402),slice(402,620),slice(620,682),slice(682,856),slice(856,988),slice(988,1162),slice(1162,1292),slice(1292,1330),slice(1330,1368)]
#x = np.zeros(339) + np.ones(-339+988) + np.zeros(-988+1368)
#x = np.multiply(x,(255,255,255))
p1.fill((0, 0, 0))
x = []

for j in range(0,339):
	x.append([255,255,255])
for j in range(988-339):
	x.append([0,0,0])
for j in range(1292-988):
	x.append([255,255,255])
for j in range(1330-1292):
	x.append([0,0,0])
for j in range(1368-1330):
	x.append([255,255,255])

print(x)
p1[:len(x)] = x
time.sleep(1)
x.reverse()
p1[:len(x)] = x
time.sleep(1)
p1.fill((0, 0, 0))
