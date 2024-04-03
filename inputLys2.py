import time
from samlet import *

v = 100

while True:
	print('1:Hvid')
	print('2:Rød')
	print('3:Grøn')
	print('4:Blå')
	print('5:sort')
	print('8:rød hvid skift')
	print('9:random')
	print('10:sluk')
	v = int(input("heltal: ") or v)
	print(v)
	if v == 1:
		farve(H,1,0.01)
	if v == 2:
		farve(R,1,0.01)
	if v == 3:
		farve(G,1,0.01)
	if v == 4:
		farve(B,1,0.01)
	if v == 5:
		skift(R,H,0.4)
	if v == 6:
		skift2(R,H,0.4)
#	if v == 7:
#		lysFalm()
	if v == 8:
		half(R,H,0.01)
		time.sleep(1)
		half(H,R,0.01)
		time.sleep(1)
	if v == 9:
		randomPixel(100)
	if v == 10:
		farve(BL,1,0.01)
	if v == 0:
		farve(BL,1,0.01)
		break
