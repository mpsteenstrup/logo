import time
import pygame.midi
from samlet import *

speed = 0.005  # Adjust the speed for smoother animation
last_update_time = time.time()
pygame.midi.init()
input_id = 3  # Set MIDI Input ID to 3, as per your configuration
midi_input = pygame.midi.Input(input_id)

animation_number = 5
animation_number_saved = 0
current_index = 0

# Main loop
try:
	print("Starting loop. Press MIDI notes C (60) to reset and D (62) to reverse direction.")

	while True:
		current_time = time.time()  # Get current time to control animation speed
		if midi_input.poll():
			midi_events = midi_input.read(10)  # Read MIDI events

			for event in midi_events:
				status, note, velocity, timestamp = event[0]
				if status == 144 and velocity > 0 and note == 60:  # Note On for E
					animation_number = 0
				if status == 144 and velocity > 0 and note == 61:  # Note On for E
					animation_number = 1
				if status == 144 and velocity > 0 and note == 62:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 2
				if status == 144 and velocity > 0 and note == 63:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 3
				if status == 144 and velocity > 0 and note == 64:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 4

				if status == 144 and velocity > 0 and note == 72:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 10
				if status == 144 and velocity > 0 and note == 73:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 11
				if status == 144 and velocity > 0 and note == 74:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 12
				if status == 144 and velocity > 0 and note == 75:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 13
				if status == 144 and velocity > 0 and note == 76:  # Note On for E
					animation_number_saved = animation_number  # tjek ikke 3
					animation_number = 14


				if status == 144 and velocity > 0 and note == 84:  # Note On for E
					animation_number = 20
				if status == 144 and velocity > 0 and note == 85:  # Note On for E
					animation_number = 21
				if status == 144 and velocity > 0 and note == 86:  # Note On for E
					animation_number = 22
				if status == 144 and velocity > 0 and note == 87:  # Note On for E
					animation_number = 23
				if status == 144 and velocity > 0 and note == 88:  # Note On for E
					animation_number = 24



		if current_time - last_update_time > speed:  # Only update after 'speed' seconds
			current_index += 1
			current_index = current_index % n1  # strip.numPixels()
#			print(current_index)

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

			# Blink
			if animation_number == 10:
				speed = 0.005
				animation_number = blink(Hfull, animation_number_saved)
			if animation_number == 11:
				speed = 0.005
				animation_number = blink(R, animation_number_saved)
			if animation_number == 12:
				speed = 0.005
				animation_number = blink(G, animation_number_saved)
			if animation_number == 13:
				speed = 0.005
				animation_number = blink(B, animation_number_saved)
			if animation_number == 14:
				speed = 0.005
				animation_number = blink(Y, animation_number_saved)

			# Pulsing

			if animation_number == 20:
				speed = 0.00001
				pulsing(R, current_index,40)





			if animation_number == 40:
				speed = 0.5
				skift(R, B)

#			time.sleep(0.1)

			last_update_time = current_time  # Update the last update time

		# Pause if the animation is stopped
		elif animation_number == 0:
			time.sleep(0.1)  # Small delay to reduce CPU usage when paused

except KeyboardInterrupt:
	print("Program interrupted.")

finally:
	farve(H)
	midi_input.close()
	pygame.midi.quit()
	print("MIDI input closed.")