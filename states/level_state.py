import pygame

class LevelState:
    def __init__(self, level):
        self.current_level = level  # Start with the first level

    def setup(self):
        pass

    def cleanup(self):
        pass

    def update(self):
        self.current_level.update()

    def draw(self, screen):
        self.current_level.draw(screen)