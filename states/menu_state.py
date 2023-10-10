import pygame

class MenuState:
    def __init__(self, menu, action_handler):
        self.menu = menu
        self.action_handler = action_handler

    def setup(self):
        pass

    def cleanup(self):
        pass

    def update(self, events):
        for event in events:
            action = self.menu.handle_input(event)
            self.action_handler(action)

    def draw(self, screen):
        self.menu.draw(screen)
        