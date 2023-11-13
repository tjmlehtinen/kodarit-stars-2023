import pygame
import sys
from states.level_state import LevelState
from game.player import Player

class GameStateManager:
    def __init__(self):
        self.current_state = None

    def change_state(self, new_state):
        if self.current_state:
            self.current_state.cleanup()
        self.current_state = new_state
        self.current_state.setup()

    def update(self, events):
        if self.current_state:
            self.current_state.update(events)

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)
    
    def process_menu_action(self, action):
        if action == "start_game":
            self.change_state(LevelState("./levels/level1.json", Player(), self.process_level_action))
        elif action == "quit":
            pygame.quit()
            sys.exit()
    
    def process_level_action(self, action):
        if action == "next level":
            self.change_state(self.current_state.next_level())
        if action == "game finished":
            pygame.quit()
            sys.exit()