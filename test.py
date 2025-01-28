import pygame
import os

pygame.init()

# Set up screen
screen = pygame.display.set_mode((800, 600))

# Ensure correct working directory
os.chdir(os.path.dirname(__file__))

# Absolute and relative paths
background_path_relative = "assets/images/background.png"
background_path_absolute = os.path.abspath(background_path_relative)

print("Testing path:", background_path_absolute)

try:
    background = pygame.image.load(background_path_relative)
    print("Background loaded successfully!")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except pygame.error as e:
    print(f"PyGame error: {e}")
