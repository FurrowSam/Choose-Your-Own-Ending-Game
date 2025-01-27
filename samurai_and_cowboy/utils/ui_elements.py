import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

class Button:
    """
    A reusable button class for UI interactions.
    """
    def __init__(self, x, y, width, height, text, font, text_color=WHITE, bg_color=GRAY, hover_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.hovered = False

    def draw(self, screen):
        """Draw the button on the screen."""
        color = self.hover_color if self.hovered else self.bg_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)  # Border

        # Render the button text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        """
        Handle mouse events for the button.
        Returns True if the button is clicked.
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if self.hovered:
                return True
        return False


def render_text(screen, text, font, color, x, y, max_width=None):
    """
    Render text with optional line wrapping.
    """
    lines = []
    if max_width:
        words = text.split(" ")
        current_line = []
        current_width = 0

        for word in words:
            word_width, word_height = font.size(word + " ")
            if current_width + word_width > max_width and current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_width = word_width
            else:
                current_line.append(word)
                current_width += word_width
        if current_line:
            lines.append(" ".join(current_line))
    else:
        lines = [text]

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (x, y + i * font.get_height()))


class HealthBar:
    """
    A reusable health bar class to display HP.
    """
    def __init__(self, x, y, width, height, max_hp):
        self.rect = pygame.Rect(x, y, width, height)
        self.max_hp = max_hp
        self.current_hp = max_hp

    def update(self, current_hp):
        """Update the health bar's current health."""
        self.current_hp = max(0, current_hp)

    def draw(self, screen):
        """Draw the health bar."""
        # Draw the background bar (red)
        pygame.draw.rect(screen, (200, 0, 0), self.rect)

        # Calculate the health ratio
        health_ratio = self.current_hp / self.max_hp

        # Draw the current health bar (green)
        if health_ratio > 0:
            health_width = self.rect.width * health_ratio
            health_rect = pygame.Rect(self.rect.x, self.rect.y, health_width, self.rect.height)
            pygame.draw.rect(screen, (0, 200, 0), health_rect)

        # Draw a border around the health bar
        pygame.draw.rect(screen, BLACK, self.rect, 2)
