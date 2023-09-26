import pygame

class MenuState:
    def __init__(self, menu):
        self.menu = menu

    def setup(self):
        pass

    def cleanup(self):
        pass

    def update(self, events):
        for event in events:
            action = self.menu.handle_input(event)

    def draw(self, screen):
        self.start_menu.draw(screen)
        