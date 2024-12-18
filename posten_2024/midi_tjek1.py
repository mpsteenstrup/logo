import pygame.midi

# Initialize Pygame MIDI
pygame.midi.init()

# List all available MIDI devices
for i in range(pygame.midi.get_count()):
    player_info = pygame.midi.get_device_info(i)
    name = player_info[1]
    input_device = player_info[2]
    if input_device:
        print(f"Input device {i}: {name}")
    else:
        print(f"Output device {i}: {name}")

pygame.midi.quit()

