import time
import pygame.midi
from samlet import *

# Set the animation speed and initialize timing
speed = 0.005  # Adjust the speed for smoother animation
last_update_time = time.time()

# Initialize the MIDI system
pygame.midi.init()
input_id = 3  # Set MIDI Input ID to 3 (adjust based on your MIDI configuration)
midi_input = pygame.midi.Input(input_id)

# Initialize animation-related variables
animation_number = 0
animation_number_saved = 0
global current_index
current_index = 0
animation = [farve, H, H]  # Default animation function and parameters

# Mapping MIDI notes to animations and their arguments
map_notes_animation = {
	# Static colors
	60: [farve, BL, 0],    # Set all LEDs to color BL
	61: [farve, H, 0],     # Set all LEDs to color H
	62: [farve, R, 0],     # Set all LEDs to color R
	63: [farve, G, 0],     # Set all LEDs to color G
	64: [farve, B, 0],     # Set all LEDs to color B
	65: [farve, Y, 0],     # Set all LEDs to color Y
	66: [farve, Hfull, 0], # Set all LEDs to full brightness with color H (for blinking)

	# Pulsing animations
	67: [pulsing, H, 40],  # Pulsing effect with color H
	68: [pulsing, R, 40],  # Pulsing effect with color R
	69: [pulsing, G, 40],  # Pulsing effect with color G
	70: [pulsing, B, 40],  # Pulsing effect with color B
	71: [pulsing, Y, 40],  # Pulsing effect with color Y

	# Transition animations
	72: [skift, H, R],     # Transition from color H to R
	73: [skift, R, B],     # Transition from color R to B
	74: [skift, G, B],     # Transition from color G to B
	75: [skift, B, H],     # Transition from color B to H
	76: [skift, Y, R],     # Transition from color Y to R

	# Random pixel animations
	77: [randomPixel, H, 100],    # Randomly light up pixels with color H
	78: [randomPixel, R, 100],    # Randomly light up pixels with color R
	79: [randomPixel, G, 100],    # Randomly light up pixels with color G
	80: [randomPixel, B, 100],    # Randomly light up pixels with color B
	81: [randomPixel, Y, 100],    # Randomly light up pixels with color Y
	82: [randomPixel, Hfull, 100],# Randomly light up pixels with full brightness H

	# Random color animations
	83: [randomFarve, H, 100]     # Randomly set LEDs to different colors
}

# Main loop
try:
	print("Starting loop. Press MIDI notes to trigger animations.")

	while True:
		# Handle MIDI updates
		if midi_input.poll():
			midi_events = midi_input.read(10)  # Read up to 10 MIDI events
			for event in midi_events:
				status, note, velocity, timestamp = event[0]
				if status == 144 and velocity > 0:  # MIDI Note On
					if note in map_notes_animation:  # Check if note exists in the mapping
						animation = map_notes_animation[note]  # Update the current animation
		
		# Handle time-based updates
		current_time = time.time()  # Get current time to control animation speed
		if current_time - last_update_time > speed:  # Update only after 'speed' interval
			animation[0](animation[1], animation[2], current_index)  # Call the animation function
			current_index += 1
			current_index = current_index % n1  # Wrap current index within the range of pixels
			last_update_time = current_time  # Update the last update time

except KeyboardInterrupt:
	print("Program interrupted.")

finally:
	# Clean up before exiting
	farve(H, 1, 2)  # Set LEDs to default state
	midi_input.close()
	pygame.midi.quit()
	print("MIDI input closed.")