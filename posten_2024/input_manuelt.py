import time
import pygame.midi
from samlet import *

speed = 0.005  # Adjust the speed for smoother animation
last_update_time = time.time()
pygame.midi.init()
input_id = 3  # Set MIDI Input ID to 3, as per your configuration

animation_number = 0
animation_number_saved = 0
global current_index
current_index = 0
animation = [farve, H, H]

map_notes_animation = {
	60: [farve, BL, 0],  # Call `farve(BL)`
	61: [farve, H, 0],   # Call `farve(H)`
	62: [farve, R, 0],   # Call `farve(R)`
	63: [farve, G, 0],   # Call `farve(G)`
	64: [farve, B, 0],   # Duplicate is fine
	65: [farve, Y, 0],    # Call `farve(Y)`
	66: [farve, Hfull, 0],  # bør kun bruges til blink Call `farve(BL)`

	67: [pulsing, H, 40],   # Call `farve(H)`
	68: [pulsing, R, 40],   # Call `farve(R)`
	69: [pulsing, G, 40],   # Call `farve(G)`
	70: [pulsing, B, 40],   # Duplicate is fine
	71: [pulsing, Y, 40],    # Call `farve(Y)`

	71: [skift, H, R],   # Call `farve(H)`
	72: [skift, H, BL],   # Call `farve(R)`
	73: [skift, R, B],   # Call `farve(R)`
	74: [skift, G, B],   # Call `farve(G)`
	75: [skift, B, H],   # Duplicate is fine
	76: [skift, Y, R],    # Call `farve(Y)`

	77: [randomPixel, H, 100],    # Call `farve(Y)`
	78: [randomPixel, R, 100],    # Call `farve(Y)`
	79: [randomPixel, G, 100],    # Call `farve(Y)`
	80: [randomPixel, B, 100],    # Call `farve(Y)`
	81: [randomPixel, Y, 100],    # Call `farve(Y)`
	82: [randomPixel, Hfull, 100],    # Call `farve(Y)`

	83: [randomFarve, H, 100]    # Call `farve(Y)`


}

# Main loop
try:
	print("Starting loop. Press MIDI notes to trigger animations.")

	while True:
		# Handle MIDI updates
		note = int(input('nummer 60:'))
		if note in map_notes_animation:  # Check if note exists in mapping
			animation = map_notes_animation[note]  #
		current_time = time.time()  # Get current time to control animation speed
		if current_time - last_update_time > speed:  # Only update after 'speed' seconds
			print('test')
			animation[0](animation[1],animation[2],current_index)  # Call the function with the argument
			current_index += 1
			current_index = current_index % n1  # strip.numPixels()
			last_update_time = current_time  # Update the last update time

except KeyboardInterrupt:
	print("Program interrupted.")

finally:
	farve(H,1,2)
	midi_input.close()
	pygame.midi.quit()
	print("MIDI input closed.")

