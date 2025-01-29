class SceneManager:
    def __init__(self, screen, start_scene):
        self.screen = screen
        self.current_scene = start_scene(self.screen)

    def update(self):
        self.current_scene.update()
        if self.current_scene.next_scene:
            self.current_scene = self.current_scene.next_scene  # Move to next scene

    def draw(self):
        self.current_scene.draw()
