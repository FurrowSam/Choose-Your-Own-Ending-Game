import pygame
import sys
from scenes import intro

# Initialize PyGame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Samurai and Cowboy: A Dark Tale")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game clock
clock = pygame.time.Clock()

def main():
    # Start with the intro scene
    current_scene = intro.IntroScene(screen)
    
    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update and draw the current scene
        current_scene.update()
        current_scene.draw()
        
        # Check if the scene has transitioned
        if current_scene.next_scene:
            current_scene = current_scene.next_scene
        
        # Refresh the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
