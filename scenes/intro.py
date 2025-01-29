import pygame
from scenes.choice_one import Choice1Scene


# Fonts and colors
FONT_NAME = "assets/fonts/game_font.ttf"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class IntroScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text = [
            "In a world torn apart by greed...",
            "Two warriors emerge from the shadows...",
            "Bound by fate, they must unite...",
            "A samurai from the East, seeking vengeance...",
            "A cowboy from the West, searching for justice...",
            "Their destinies intertwined, they must fight to save their world...",
            "Together, they must face the darkness of the corporation..."
        ]
        self.current_line = 0
        self.next_scene = None
        self.timer = 0  # For text delay

        # Load background image
        self.background = pygame.image.load("assets/images/background.png")

        # Scale background image
        self.background = pygame.transform.scale(self.background, (800, 600))

        # Load character images
        self.samurai_image = pygame.image.load("assets/images/samurai.png")
        self.cowboy_image = pygame.image.load("assets/images/cowboy.png")

        # Scale character images
        self.samurai_image = pygame.transform.scale(self.samurai_image, (200, 300))  # Adjust size
        self.cowboy_image = pygame.transform.scale(self.cowboy_image, (200, 300))    # Adjust size

    def update(self):
        # Advance text every 2 seconds
        self.timer += 1
        if self.timer > 120:  # 2 seconds at 60 FPS
            self.timer = 0
            self.current_line += 1
            if self.current_line >= len(self.text):
                self.next_scene = Choice1Scene(self.screen)

    def draw(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))

        # Draw character images based on the current line
        if self.current_line >= 3:  # Show samurai after the third line
            self.screen.blit(self.samurai_image, (100, 200))  # Position samurai on the left
        if self.current_line >= 4:  # Show cowboy after the fourth line
            self.screen.blit(self.cowboy_image, (500, 200))   # Position cowboy on the right

        # Draw text
        if self.current_line < len(self.text):
            line = self.text[self.current_line]
            text_surface = self.font.render(line, True, BLACK)
            self.screen.blit(text_surface, (50, 50))  # Adjust position as needed
