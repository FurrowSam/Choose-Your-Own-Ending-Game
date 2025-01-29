import pygame

class AttackCorporationScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = [
            "The towering corporate headquarters looms ahead...",
            "Security drones hover, scanning for intruders.",
            "The samurai tightens his grip on his sword.",
            "The cowboy loads his revolver. It's time."
        ]
        self.current_line = 0
        self.next_scene = None
        self.timer = 0

        # Load background
        try:
            self.background = pygame.image.load("assets/images/corporation_background.png")
        except pygame.error:
            print("Error: Background image not found!")
            self.background = pygame.Surface((800, 600))
            self.background.fill((20, 20, 20))  # Dark fallback background

        # Load character images
        try:
            self.samurai_image = pygame.image.load("assets/images/samurai.png")
            self.cowboy_image = pygame.image.load("assets/images/cowboy.png")
        except pygame.error:
            print("Error: Character images not found!")
            self.samurai_image = None
            self.cowboy_image = None

    def update(self):
        """Advance text every 3 seconds or move to the next scene."""
        self.timer += 1
        if self.timer > 180:  # 3 seconds at 60 FPS
            self.timer = 0
            self.current_line += 1
            if self.current_line >= len(self.text):
                from scenes.corporation_infiltration import CorporationInfiltrationScene
                self.next_scene = CorporationInfiltrationScene(self.screen)  # Next stage

    def draw(self):
        """Draws the scene."""
        self.screen.blit(self.background, (0, 0))

        # Draw characters if loaded
        if self.samurai_image:
            self.screen.blit(self.samurai_image, (100, 200))  # Samurai on the left
        if self.cowboy_image:
            self.screen.blit(self.cowboy_image, (500, 200))  # Cowboy on the right

        # Draw story text
        if self.current_line < len(self.text):
            text_surface = self.font.render(self.text[self.current_line], True, (255, 255, 255))
            self.screen.blit(text_surface, (50, 50))
