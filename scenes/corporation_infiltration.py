import pygame

class CorporationInfiltrationScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("assets/fonts/game_font.ttf", 36)
        self.text = "How do you approach the corporation?"
        self.choices = ["Sneak in silently", "Fight your way through"]
        self.selected_choice = 0
        self.next_scene = None

        # Load background
        try:
            self.background = pygame.image.load("assets/images/corporation_inside.png")
        except pygame.error:
            print("Error: Background image not found!")
            self.background = pygame.Surface((800, 600))
            self.background.fill((30, 30, 30))  # Dark fallback background

    def update(self):
        """Handles user choice selection."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.selected_choice = (self.selected_choice - 1) % len(self.choices)
        if keys[pygame.K_DOWN]:
            self.selected_choice = (self.selected_choice + 1) % len(self.choices)
        if keys[pygame.K_RETURN]:
            if self.selected_choice == 0:
                from scenes.stealth_mission import StealthMissionScene
                self.next_scene = StealthMissionScene(self.screen)  # Sneaking path
            elif self.selected_choice == 1:
                from scenes.corporation_battle import CorporationBattleScene
                self.next_scene = CorporationBattleScene(self.screen)  # Combat path

    def draw(self):
        """Draws the scene with choice selection."""
        self.screen.blit(self.background, (0, 0))

        # Render main text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 50))

        # Render choices
        for i, choice in enumerate(self.choices):
            color = (255, 255, 0) if i == self.selected_choice else (200, 200, 200)
            choice_surface = self.font.render(choice, True, color)
            self.screen.blit(choice_surface, (50, 200 + i * 50))
