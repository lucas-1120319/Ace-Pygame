import pygame

class Bullet():

    def __init__(self, screen, position):
        self.screen = screen
        self.speed = 10
        self.position = position
        self.direction = (0, 1)
        self.damage = 10
        self.img = pygame.image.load("Assets/Projectiles And Explosions/Projectile02.png").convert_alpha()
        self.img = pygame.transform.flip(self.img, False, True)
        self.rect = self.img.get_rect(center=(self.position[0],  self.position[1]))
        screen.blit(self.img, self.rect)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.top < self.screen.get_rect().top:
            return True
        else:
            self.screen.blit(self.img, self.rect)
            return False

    def spawn(self):
        print("spawn")
