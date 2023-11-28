import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))  # Blue color for the player (customize as needed)
        self.rect = self.image.get_rect()
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
        if keys[pygame.K_SPACE]:
            self.jump()
        if not self.on_ground:
            self.velocity.y += 1  # Simulate gravity
        self.rect.move_ip(self.velocity.x, self.velocity.y)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_position(self):
        return pygame.math.Vector2(self.rect.x, self.rect.y)

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power

    def check_platform_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Player is colliding with the platform
                # You might want to adjust the collision behavior (e.g., stop falling, set on_ground flag, etc.)
                self.rect.bottom = platform.rect.top # Snap player's bottom to the platform's top
                self.velocity.y = 0  # Stop vertical movement
                # Additional collision handling logic
                self.on_ground = True
                return True
        self.on_ground = False
        return False