import time
from samlet import *

v = 100
n = 100
while True:
	try:
		print('1:Hvid')
		print('2:Roed')
		print('3:Roed pulsing')
		print('4:Blaa')
		print('5:Gul')
		print('6:skift roed/hvid')
		print('8:roed hvid skift')
		print('9:random')
		print('10:sluk')
		animation_number = int(input("heltal: "))
		if animation_number == 0:
			farve(BL,1,0.01)
			break


			# Farver
		if animation_number == 1:
			speed = 0.005
			farve(H)
		if animation_number == 2:
			speed = 0.005
			farve(R)
		if animation_number == 3:
			speed = 0.005
			farve(G)
		if animation_number == 4:
			speed = 0.005
			farve(B)
		if animation_number == 5:
			speed = 0.005
			farve(Y)
		if animation_number == 6:
			speed = 0.005
			farve(BL)



	except Exception as e:
		print(e)
		farve(H)
		time.sleep(1)
		break
