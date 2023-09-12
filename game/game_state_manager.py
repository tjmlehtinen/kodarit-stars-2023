# game_state_manager.py

class GameStateManager:
    def __init__(self):
        self.current_state = None

    def change_state(self, new_state):
        if self.current_state:
            self.current_state.cleanup()
        self.current_state = new_state
        self.current_state.setup()

    def update(self):
        if self.current_state:
            self.current_state.update()

    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)
