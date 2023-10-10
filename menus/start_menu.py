import pygame

class StartMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Platformer title", True, (255, 255, 255))
        self.start_option = self.font.render("Start Game", True, (255, 255, 255))
        self.quit_option = self.font.render("Quit", True, (255, 255, 255))
        self.selected_option = 0  # Initially select the "Start Game" option
        self.option_color = (255, 255, 255)
        self.selected_color = (255, 0, 0)  # Color for the selected option

    def draw(self, screen):
        screen.fill((100, 80, 80))
        screen.blit(self.title, (200, 100))
        screen.blit(self.start_option, (300, 200))
        screen.blit(self.quit_option, (300, 250))

        if self.selected_option == 0:
            screen.blit(self.start_option, (300, 200))
            pygame.draw.rect(screen, self.selected_color, (295, 200, self.start_option.get_width() + 10, self.start_option.get_height()), 2)
        else:
            screen.blit(self.start_option, (300, 200))

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
