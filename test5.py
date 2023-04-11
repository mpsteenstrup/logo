import time
import board
import neopixel

#pixels1 = neopixel.NeoPixel(board.D21, 685, brightness=1)
pixels1 = neopixel.NeoPixel(board.D21, 400, brightness=1)

x=0

pixels1.fill((0, 0, 0))

pixels1[0] = (255, 0, 0)

time.sleep(1)


#Below will loop until variable x has a value of 35
x=0
s=10
if 1==2:
#    
    pixels1[x] = (255, 0,0)
    pixels1[x-s] = (0, 0,0)
    pixels1[-x] = (0, 0, 255)
    pixels1[-x+s] = (0, 0,0)
#

    x=x+s
    time.sleep(0.01)
    if x>654:
        s = -s
    if x<0:
        s = -s


#Below section is the same process as the above loop just in reverse

#Add a brief time delay to appreciate what has happened    

for i in range(1):
	pixels1.fill((0,0,50))
	time.sleep(1)
pixels1.fill((0,0,0))

#for i in range(50):
#	pixels1.fill((i,i,i))
#	time.sleep(0.2)


#Complete the script by returning all the LED to off
