import pygame

class GoToTheCityScene:  # Ensure this matches the correct class name
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = "You arrive at the city, neon lights flickering around you."
        self.next_scene = None  # Placeholder for the next scene

        # Load background
        self.background = pygame.image.load("assets/images/city_background.png")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:  # Move to the next scene when Enter is pressed
            self.next_scene = None  # Change this to transition to the next part of the game

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 50))
