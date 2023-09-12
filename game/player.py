import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((0, 0, 255))  # Blue color for the player (customize as needed)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = pygame.Vector2(0, 0)
        self.jump_power = -15
        self.on_ground = False
        

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0

        self.velocity.y += 1  # Simulate gravity
        self.rect.move_ip(self.velocity.x, self.velocity.y)

        # Keep player within screen bounds
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(800, self.rect.right)  # Assuming a screen width of 800
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(600, self.rect.bottom)  # Assuming a screen height of 600

        # Check if the player is on the ground
        if self.rect.bottom >= 600:  # Assuming a screen height of 600
            self.rect.bottom = 600
            self.velocity.y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power
