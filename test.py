import pygame
import os

pygame.init()

# Set up screen
screen = pygame.display.set_mode((800, 600))

# Correct path definition
background_path_relative = r"C:\Users\18176\Desktop\samurai_and_cowboy\assets\images\background.png"

# Print resolved path
print("Testing path:", background_path_relative)

try:
    background = pygame.image.load(background_path_relative)
    print("Background loaded successfully!")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except pygame.error as e:
    print(f"PyGame error: {e}")
