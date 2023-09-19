# level.py

import pygame
import json
from game.platform import Platform 

class Level:
    def __init__(self, player, level_data):
        self.player = player
        self.platforms = pygame.sprite.Group()
        
        # Load level data from JSON
        self.load_level_data(level_data)

    def load_level_data(self, level_data):
        with open(level_data, "r") as file:
            data = json.load(file)
        
        # Create platforms from JSON data
        for platform_data in data["platforms"]:
            platform = Platform(platform_data["x"], platform_data["y"], platform_data["width"], platform_data["height"])
            self.platforms.add(platform)


    def update(self):
        # Update level-specific logic (e.g., enemy AI).
        pass

    def draw(self, screen):
        # Draw level-specific elements (platforms, enemies).
        self.platforms.draw(screen)