import pygame

class CityExplorationScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = "The city is alive with danger and opportunity."
        self.next_scene = None

        # Load background
        self.background = pygame.image.load("assets/images/city_exploration.png")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:  # Move to the next scene on Enter
            self.next_scene = None  # Replace with an actual next scene

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 50))
