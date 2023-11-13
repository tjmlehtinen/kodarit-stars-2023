from game.level import Level
# Create levels

class LevelState:
    def __init__(self, level_data, player, action_handler):
        self.current_level = Level(level_data)  # Start with the first level
        self.player = player
        self.action_handler = action_handler

    def setup(self):
        x = self.current_level.start_pos["x"]
        y = self.current_level.start_pos["y"]
        self.player.set_position(x, y)

    def cleanup(self):
        pass

    def update(self, events):
        self.player.update()
        self.current_level.update()
        self.player.check_platform_collision(self.current_level.platforms)
        if (self.player.get_position()[0] > self.current_level.end_point):
            if self.current_level.next_level:
                self.action_handler("next level")
            else:
                self.action_handler("game finished")

    def draw(self, screen):
        self.current_level.draw(screen)
        screen.blit(self.player.image, self.player.rect)
    
    def next_level(self):
        return LevelState(self.current_level.next_level, self.player, self.action_handler)
        