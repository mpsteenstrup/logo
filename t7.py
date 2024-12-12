import pygame.midi
from rpi_ws281x import PixelStrip, Color
import time

animation_number = 0
current_index = 0

# LED configuration
LED_COUNT = 23      # Number of LEDs
#LED_COUNT = 1600
LED_PIN = 21        # GPIO pin connected to the LEDs (changed to 21)
LED_FREQ_HZ = 800000
strip = PixelStrip(LED_COUNT, LED_PIN)
strip.begin()

# MIDI initialization
pygame.midi.init()
input_id = 3  # Set MIDI Input ID to 3, as per your configuration
midi_input = pygame.midi.Input(input_id)

# Color transition speed
speed = 0.0001  # Adjust the speed for smoother animation
running = True  # Is the animation running or paused
reset = False   # Should the animation reset?
last_update_time = time.time()  # Time of last update to control animation speed

# Function to set the entire strip to a single color
def set_color(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def animation1():
    set_color(Color(0,0,255))
    strip.setPixelColor(current_index,Color(255,0,0))
    strip.show()
def animation2():
     set_color(Color(0,255,0))

# Main loop
try:
    print("Starting loop. Press MIDI notes C (60) to reset and D (62) to reverse direction.")
    
    while True:
        current_time = time.time()  # Get current time to control animation speed
        # Check for MIDI input
        if midi_input.poll():
            midi_events = midi_input.read(10)  # Read MIDI events
#            print(f"Received MIDI events: {midi_events}")  # Debugging output

            for event in midi_events:
                status, note, velocity, timestamp = event[0]
#                print(f"Event: {status}, Note: {note}, Velocity: {velocity}")  # Debugging output

                if status == 144 and note == 60:  # Note On for C
#                   print("MIDI C note received. Resetting animation.")
                    animation_number = 1

                elif status == 144 and note == 62:  # Note On for D
                    animation_number = 2

        if running:
            if current_time - last_update_time > speed:  # Only update after 'speed' seconds
                current_index += 1
                current_index = current_index%23 #strip.numPixels()
                if animation_number == 1:
                    animation1()
                if animation_number == 2:
                    animation2()

                last_update_time = current_time  # Update the last update time

        # Pause if the animation is stopped
        elif not running:
            time.sleep(0.1)  # Small delay to reduce CPU usage when paused

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    set_color(Color(100,100,100))
    midi_input.close()
    pygame.midi.quit()
    print("MIDI input closed.")
