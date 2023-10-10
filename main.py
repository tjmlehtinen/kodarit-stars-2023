# main.py

import pygame
from game.player import Player
from states.game_state_manager import GameStateManager
from states.menu_state import MenuState
from menus.start_menu import StartMenu

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Create a game state manager
game_state_manager = GameStateManager()

# Set state to start menu
game_state_manager.change_state(MenuState(StartMenu(), game_state_manager.process_menu_action))


# Create the player
player = Player(WIDTH // 2, HEIGHT // 2)

# Create the group for sprites
all_sprites = pygame.sprite.Group(player)

# Create levels
level1 = Level(player, "./levels/level1.json")
level2 = Level(player, "./levels/level1.json")

# Game loop
clock = pygame.time.Clock()
current_level = None  # Start with the first level

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update the current game state
    game_state_manager.update(events)

    # Draw the current game state
    game_state_manager.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

