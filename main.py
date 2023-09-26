# main.py

import pygame
from game.player import Player
from game.level import Level
from states.game_state_manager import GameStateManager
from menus.start_menu import StartMenu

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Create a StartMenu instance
start_menu = StartMenu()

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
    # Check for input in the start menu
    menu_action = start_menu.handle_input(event)
    if menu_action == "start_game":
        # Start the game or transition to the first level
        current_level = level1
    elif menu_action == "quit":
        running = False  # Quit the game

    # Update the current game state
    game_state_manager.update(events)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the current game state
    game_state_manager.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

