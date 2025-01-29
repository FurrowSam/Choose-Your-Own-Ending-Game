import pygame
import sys
from scenes.intro import IntroScene
from scenes.choice_one import Choice1Scene
from scenes.go_to_the_city import GoToTheCityScene
from scenes.attack_corporation import AttackCorporationScene
from utils.scene_manager import SceneManager  # Handles scene switching

# Initialize PyGame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Samurai and Cowboy: A Dark Tale")

# Game clock
clock = pygame.time.Clock()

def main():
    scene_manager = SceneManager(screen, IntroScene)  # Start at the intro scene

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update and draw the current scene
        scene_manager.update()
        scene_manager.draw()

        # Refresh the display
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
