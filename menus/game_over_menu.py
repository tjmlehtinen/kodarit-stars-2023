import pygame

class GameOverMenu:
    def __init__(self, score):
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Game Over", True, (255, 255, 255))
        self.score_label = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.restart_option = self.font.render("Restart", True, (255, 255, 255))
        self.quit_option = self.font.render("Quit", True, (255, 255, 255))
        self.selected_option = 0  # Initially select the "Restart" option
        self.option_color = (255, 255, 255)
        self.selected_color = (255, 0, 0)  # Color for the selected option

    def draw(self, screen):
        screen.fill((100, 80, 80))
        screen.blit(self.title, (200, 100))
        screen.blit(self.score_label, (300, 150))
        screen.blit(self.restart_option, (300, 200))
        screen.blit(self.quit_option, (300, 250))

        if self.selected_option == 0:
            screen.blit(self.restart_option, (300, 200))
            pygame.draw.rect(screen, self.selected_color, (295, 200, self.restart_option.get_width() + 10, self.restart_option.get_height()), 2)
        else:
            screen.blit(self.restart_option, (300, 200))

        if self.selected_option == 1:
            screen.blit(self.quit_option, (300, 250))
            pygame.draw.rect(screen, self.selected_color, (295, 250, self.quit_option.get_width() + 10, self.quit_option.get_height()), 2)
        else:
            screen.blit(self.quit_option, (300, 250))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % 2
            elif event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % 2
            elif event.key == pygame.K_RETURN:
                if self.selected_option == 0:
                    return "start_game"
                elif self.selected_option == 1:
                    return "quit"
