import time
import threading

# Create printer function to print output
# make sure you add a lock so the printing doesn't go all funny
i = 100

def printer(lock):
    while True:
        time.sleep(0.2)
        with lock:
            print(f"i's value is {i}")

# create a thread lock to allow for printing
lock = threading.Lock()

# Create the thread to print
p = threading.Thread(target=printer, args=(lock,), daemon=True)

# start the thread
p.start()

# wait for input and when received stop the thread.
if input():
    i = input('skriv et tal')
#    p.join()

