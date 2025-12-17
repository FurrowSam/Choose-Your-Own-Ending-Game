import pygame
from scenes.city_exploration import CityExplorationScene

class GoToTheCityScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = [
            "You arrive at the city, neon lights flickering around you.",
            "The streets are crowded with people.",
            "Danger lurks in every shadow.",
            "But so does opportunity..."
        ]
        self.current_line = 0
        self.next_scene = None
        self.timer = 0  # Initialize timer

        # Load background
        self.background = pygame.image.load("assets/images/city_background.png")
        self.background = pygame.transform.scale(self.background, (800, 600))

        # Load character images
        self.samurai_image = pygame.image.load("assets/images/samurai.png")
        self.cowboy_image = pygame.image.load("assets/images/cowboy.png")

        # Scale character images
        self.samurai_image = pygame.transform.scale(self.samurai_image, (200, 300))
        self.cowboy_image = pygame.transform.scale(self.cowboy_image, (200, 300))

    def update(self):
        """Advance text every 4 seconds"""
        self.timer += 1
        if self.timer > 240:  # 4 seconds at 60 FPS
            self.timer = 0
            self.current_line += 1
            if self.current_line >= len(self.text):
                self.next_scene = CityExplorationScene(self.screen)

    def draw(self):
        """Draw the scene"""
        self.screen.blit(self.background, (0, 0))
        
        # Draw character images
        if self.current_line >= 2:  # Show samurai after second line
            self.screen.blit(self.samurai_image, (100, 200))
        if self.current_line >= 3:  # Show cowboy after third line
            self.screen.blit(self.cowboy_image, (500, 200))
        
        # Draw current text line
        if self.current_line < len(self.text):
            text_surface = self.font.render(self.text[self.current_line], True, (255, 255, 255))
            self.screen.blit(text_surface, (50, 50))
