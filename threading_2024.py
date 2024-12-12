import time
from samlet import *
import threading
import sys

v = 100

def background(c1,c2):
    while True:
        if n==1:
            p1.fill(c1)
        else:
            p1.fill(c2)

def other_function():
    print('You disarmed me! Dying now.')

# now threading1 runs regardless of user input
threading1 = threading.Thread(target=background(R,G))
threading1.daemon = True
threading1.start()

while True:
    try:
        n = int(input('give me a number 2 or 1'))
    except:
        n = 0
    if n == 0 :
        time.sleep(1)
        other_function()
        sys.exit()