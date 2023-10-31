# level.py

import pygame
import json
from game.platform import Platform 

class Level:
    def __init__(self, level_data, player):
        self.platforms = pygame.sprite.Group()
        self.player = player
        self.all_sprites = pygame.sprite.Group(self.player)
        # Load level data from JSON
        self.load_level_data(level_data)

    def load_level_data(self, level_data):
        with open(level_data, "r") as file:
            data = json.load(file)
        
        # Create platforms from JSON data
        for platform_data in data["platforms"]:
            platform = Platform(platform_data["x"], platform_data["y"], platform_data["width"], platform_data["height"])
            self.platforms.add(platform)
        
        # Player to starting position
        start_pos = data["player_start"]
        self.player.set_position(start_pos["x"], start_pos["y"])


    def update(self, events):
        # Update level-specific logic (e.g., enemy AI).
        self.player.check_platform_collision(self.platforms)
        self.all_sprites.update()

    def draw(self, screen):
        screen.fill((0,0,0))
        # Draw level-specific elements (platforms, enemies).
        self.platforms.draw(screen)
        self.all_sprites.draw(screen)
