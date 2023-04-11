import time
import board
import neopixel
import pygame.midi


pixels1 = neopixel.NeoPixel(board.D18, 55, brightness=1)

x=0

pixels1.fill((0, 220, 0))

pixels1[0] = (0, 20, 255)

time.sleep(1)

def running():
    x=0
    print('running')
    while x<4:
        pixels1.fill((0,0,0))
        pixels1[x] = ((255,0,0))
        x = x + 1
        time.sleep(0.1)
def running2():
    x=0
    print('running2')
    while x<4:
        pixels1.fill((0,0,0))
        pixels1[x] = ((0,255,0))
        x = x + 1
        time.sleep(0.1)

def flash():
    pixels1.fill((0,0,0))
    pixels1.fill((255,255,255))
    time.sleep(0.1)
    pixels1.fill((0,0,0))


def readInput(input_device):
    value2 = 0
    c = 0
    while True:
        if input_device.poll():
            event = input_device.read(1)
            value = event[0][0][1]
            c +=1
            if value>0 and value<60 and c>20:
                running()
                c = 0

            if value>60 and value <70 and c>20:
                c = 0
                running2()
            if value>70 and c>10:
                value2 = value
                flash()
                c = 0

# problemer med dobbelt 



if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(3) #only in my case the id is 
    readInput(my_input)





while x<4:
    
    pixels1[x] = (255, 0, 0)
    pixels1[x-1] = (255, 0, 100)
    pixels1[x-2] = (0, 0, 255)
    #Add 1 to the counter
    x=x+1
    #Add a small time pause which will translate to 'smoothly' changing colour
    time.sleep(0.05)


while x>-1:
    pixels1[x] = (255, 0, 0)
    pixels1[x+1] = (255, 0, 100)
    pixels1[x+2] = (0, 255, 0)
    x=x-1
    time.sleep(0.05)

time.sleep(4)

pixels1.fill((0, 0, 0))
