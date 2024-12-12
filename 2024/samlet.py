# NeoPixels must be connected to GPIO10, GPIO12, GPIO18 or GPIO21
import neopixel
import board
import time
import numpy as np
import random
from datetime import datetime, timedelta

n1 = 1368
#n1 = 23
p1 = neopixel.NeoPixel(board.D21,n1, brightness=0.4)

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
H = (50,50,50)
Hfull =(255,255,255) 
Y = (255,255,0)
BL = (0,0,0)

p1.fill(BL)

def farve(c):
        
        p1.fill(c)

def blink(c,n):
        p1.fill(c)
        time.sleep(0.1)
        return n

def blinkSH():
        c = (255,255,255)
        p1.fill(c)
        time.sleep(0.1)

switch = False
def skift(c1,c2):
        global switch
        template = [c1,c1,c1,c1,c1,c1,c1,c1,c1,c1,c2,c2,c2,c2,c2,c2,c2,c2]
        x = template*(n1//len(template))
        if switch:
                x.reverse()
        p1[:len(x)] = x
        switch =not switch
#       time.sleep(0.5) 



def randomPixel(n):
        p1.fill(BL)
        for k in range(n):
                for j in range(n1):
                        p1[random.randint(1, n1-1)]=(random.randint(1, 50),random.randint(1, 50),random.randint(1, 255))
                        p1[random.randint(1, n1-1)]=(BL)
                        p1[random.randint(1, n1-1)]=(BL)

def half(c1,c2):
        x = [c1]*(n1//2)
        x += [c2]*(n1//2)
        p1[:len(x)] = x
#       time.sleep(t)

#       x.reverse()
#       p1[:len(x)] = x 
#       time.sleep(t) 



def pulsing(c, n, t):
        t1 = datetime.now()
        interval = np.power(np.arange(1.1,1.6,0.01),8)/256
        for j in range(n):
                for i in interval:
                                                          [ Wrote 148 lines ]

