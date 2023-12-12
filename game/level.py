# level.py

import pygame
import json
from game.platform import Platform 

class Level:
    def __init__(self, level_data):
        self.platforms = pygame.sprite.Group()
        # Load level data from JSON
        data = load_level_data(level_data)

        # Create platforms from JSON data
        for platform_data in data["platforms"]:
            platform = Platform(platform_data["x"], platform_data["y"], platform_data["width"], platform_data["height"])
            self.platforms.add(platform)
        
        # Player to starting position
        self.start_position = data["player_start"]
        self.end_point = data["end_point"]
        self.bottom = data["bottom"]
        self.next_level = data["next_level"]

    def setOffset(self, offset):
        self.end_point += offset.x
        for platform in self.platforms:
             platform.rect.topleft += offset

    def update(self):
        # Update level-specific logic (e.g., enemy AI).
        pass

    def draw(self, screen):
        screen.fill((0,0,0))
        # Draw level-specific elements (platforms, enemies).
        self.platforms.draw(screen)
        pygame.draw.line(screen, (255,0,0), (self.end_point, -100), (self.end_point, 1000))

def load_level_data(level_data):
        with open(level_data, "r") as file:
            data = json.load(file)
        return data