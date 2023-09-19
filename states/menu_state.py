import pygame

class MenuState:
    def __init__(self):
        self.start_menu = StartMenu()

    def setup(self):
        pass

    def cleanup(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        self.start_menu.draw(screen)
        action = self.start_menu.handle_input()
        if action == "start_game":
            game_state_manager.change_state(LevelState())
        elif action == "quit":
            pygame.quit()