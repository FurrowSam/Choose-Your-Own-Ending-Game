import pygame
from scenes.choice_1 import Choice1Scene

# Fonts and colors
FONT_NAME = "assets/fonts/your_font.ttf"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class IntroScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(FONT_NAME, 36)
        self.text = [
            "In a world torn apart by greed...",
            "A samurai from the East, seeking vengeance...",
            "A cowboy from the West, searching for justice...",
            "Together, they must face the darkness."
        ]
        self.current_line = 0
        self.next_scene = None
        self.timer = 0  # For text delay

    def update(self):
        # Advance text every 2 seconds
        self.timer += 1
        if self.timer > 120:  # 2 seconds at 60 FPS
            self.timer = 0
            self.current_line += 1
            if self.current_line >= len(self.text):
                self.next_scene = Choice1Scene(self.screen)

    def draw(self):
        self.screen.fill(BLACK)
        if self.current_line < len(self.text):
            line = self.text[self.current_line]
            text_surface = self.font.render(line, True, WHITE)
            self.screen.blit(text_surface, (50, 300))
