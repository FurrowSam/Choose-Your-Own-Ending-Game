import pygame

class Choice1Scene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = "Do they head to the city or confront the corporation directly?"
        self.choices = ["Go to the City", "Attack the Corporation"]
        self.selected_choice = 0
        self.next_scene = None

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.selected_choice = (self.selected_choice - 1) % len(self.choices)
        if keys[pygame.K_DOWN]:
            self.selected_choice = (self.selected_choice + 1) % len(self.choices)
        if keys[pygame.K_RETURN]:
            if self.selected_choice == 0:
                print("Player chose to go to the city.")
                # Add logic to transition to a city scene
            elif self.selected_choice == 1:
                print("Player chose to attack the corporation.")
                # Add logic to transition to a corporation scene

    def draw(self):
        self.screen.fill((0, 0, 0))
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 100))

        for i, choice in enumerate(self.choices):
            color = (255, 255, 255) if i == self.selected_choice else (100, 100, 100)
            choice_surface = self.font.render(choice, True, color)
            self.screen.blit(choice_surface, (50, 200 + i * 40))
