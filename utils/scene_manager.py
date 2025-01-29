class SceneManager:
    def __init__(self, screen, start_scene):
        self.screen = screen
        self.current_scene = start_scene(self.screen)

    def update(self):
        self.current_scene.update()
        if self.current_scene.next_scene:
            self.current_scene = self.current_scene.next_scene  # Switch scenes

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clears screen before drawing new scene
        self.current_scene.draw()
