import pygame
from scenes.city_exploration import CityExplorationScene

class GoToTheCityScene:  # Ensure this matches the correct class name
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = "You arrive at the city, neon lights flickering around you."
        self.next_scene = None  # Placeholder for the next scene

        # Load background
        self.background = pygame.image.load("assets/images/city_background.png")

    # Scale background image
        self.background = pygame.transform.scale(self.background, (800, 600))

    # Load character images
        self.samurai_image = pygame.image.load("assets/images/samurai.png")
        self.cowboy_image = pygame.image.load("assets/images/cowboy.png")

        # Scale character images
        self.samurai_image = pygame.transform.scale(self.samurai_image, (200, 300))  # Adjust size
        self.cowboy_image = pygame.transform.scale(self.cowboy_image, (200, 300))    # Adjust size


    def update(self):
                # Advance text every 4 seconds 
        self.timer += 1
        if self.timer > 240:  # 4 seconds at 60 FPS
            self.timer = 0
            self.current_line += 1
            if self.current_line >= len(self.text):
                self.next_scene = CityExplorationScene(self.screen)


    def draw(self):
        self.screen.blit(self.background, (0, 0))
        
        # Draw character images based on the current line
        if self.current_line >= 3:  # Show samurai after the third line
            self.screen.blit(self.samurai_image, (100, 200))  # Position samurai on the left
        if self.current_line >= 4:  # Show cowboy after the fourth line
            self.screen.blit(self.cowboy_image, (500, 200))   # Position cowboy on the right
