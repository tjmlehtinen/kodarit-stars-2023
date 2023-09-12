# main.py

import pygame
from game.player import Player
from game.level import Level

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Create the player
player = Player(WIDTH // 2, HEIGHT // 2)

# Create the group for sprites
all_sprites = pygame.sprite.Group(player)

# Create levels
level1 = Level(player, "./levels/level1.json")
level2 = Level(player, "./levels/level1.json")

# Game loop
clock = pygame.time.Clock()
current_level = level1  # Start with the first level

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    player.update()
    current_level.update()

    

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw game elements
    all_sprites.draw(screen)
    current_level.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

