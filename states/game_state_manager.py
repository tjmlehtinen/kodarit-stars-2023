import pygame
import sys
from states.menu_state import MenuState
from menus.start_menu import StartMenu
from menus.game_over_menu import GameOverMenu
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

    def startMenu(self):
        self.change_state(MenuState(StartMenu(), self.process_menu_action))

    def gameOver(self):
        self.change_state(MenuState(GameOverMenu(1), self.process_menu_action))
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
        if action == "next_level":
            self.change_state(self.current_state.next_level())
        if action == "game_finished":
            print("game finished")
            self.startMenu()
        if action == "game_over":
            print("game_over")
            self.gameOver()