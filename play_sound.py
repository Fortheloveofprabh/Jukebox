import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load your sound file
pygame.mixer.music.load("Pigstep.mp3")

# Play the sound file
pygame.mixer.music.play()

# Keep the script running while the music plays
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Playback finished")