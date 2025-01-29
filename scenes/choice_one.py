import pygame
from scenes.go_to_the_city import GoToTheCityScene
from scenes.attack_corporation import AttackCorporationScene

class Choice1Scene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = "Do they head to the city or confront the corporation directly?"
        self.choices = ["Go to the City", "Attack the Corporation"]
        self.selected_choice = 0
        self.next_scene = None

        # Load background
        self.background = pygame.image.load("assets/images/choice_background.png")

    def update(self):
        """Handles input and scene transition logic."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.selected_choice = (self.selected_choice - 1) % len(self.choices)
        if keys[pygame.K_DOWN]:
            self.selected_choice = (self.selected_choice + 1) % len(self.choices)
        if keys[pygame.K_RETURN]:
            if self.selected_choice == 0:
                self.next_scene = GoToTheCityScene(self.screen)
            elif self.selected_choice == 1:
                self.next_scene = AttackCorporationScene(self.screen)

    def draw(self):  
        """Draws the choice menu on the screen."""
        self.screen.fill((0, 0, 0))  # Clears the previous screen
        self.screen.blit(self.background, (0, 0))  # Draws new background

        # Render main question
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 50))

        # Render choices with visual enhancements
        for i, choice in enumerate(self.choices):
            if i == self.selected_choice:
                color = (255, 255, 0)  # Highlighted choice (yellow)
                background_color = (50, 50, 50)  # Dark background for selection
                choice_rect = pygame.Rect(40, 195 + i * 50, 300, 50)
                pygame.draw.rect(self.screen, background_color, choice_rect, border_radius=10)
            else:
                color = (200, 200, 200)  # Default greyish text

            choice_surface = self.font.render(choice, True, color)
            self.screen.blit(choice_surface, (50, 200 + i * 50))
