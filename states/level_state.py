import pygame
from game.level import Level
# Create levels

class LevelState:
    def __init__(self, level_data, player, action_handler):
        self.current_level = Level(level_data)  # Start with the first level
        self.player = player
        self.action_handler = action_handler
        self.screen_center_x = pygame.display.get_window_size()[0]

    def setup(self):
        x = self.current_level.start_position["x"]
        y = self.current_level.start_position["y"]
        self.player.set_position(x, y)

    def cleanup(self):
        pass

    def update(self, events):
        self.player.update()
        offset = pygame.math.Vector2(100 - self.player.get_position().x, 0)
        self.current_level.setOffset(offset)
        self.player.set_position(100, self.player.get_position().y)
        self.current_level.update()
        self.player.check_platform_collision(self.current_level.platforms)
        if (self.player.get_position().x > self.current_level.end_point):
            if self.current_level.next_level:
                self.action_handler("next_level")
            else:
                self.action_handler("game_finished")
        if (self.player.get_position().y > self.current_level.bottom):
            self.action_handler("game_over")
    def draw(self, screen):        
        self.current_level.draw(screen)
        screen.blit(self.player.image, self.player.rect)
    
    def next_level(self):
        return LevelState(self.current_level.next_level, self.player, self.action_handler)
        