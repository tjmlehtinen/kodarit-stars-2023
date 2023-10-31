from game.level import Level
# Create levels

class LevelState:
    def __init__(self, level_data, player):
        self.current_level = Level(level_data, player)  # Start with the first level

    def setup(self):
        pass

    def cleanup(self):
        pass

    def update(self, events):
        self.current_level.update(events)

    def draw(self, screen):
        self.current_level.draw(screen)
        