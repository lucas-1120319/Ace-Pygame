import pygame

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.speed = 12
        self.player_img = pygame.image.load("Assets/Player/Player.png")
        self.playerRect = self.player_img.get_rect(center=(640,550))
        print("spawn")
        screen.blit(self.player_img, self.playerRect)


    def update(self):
        self.screen.blit(self.player_img, self.playerRect)
    def move(self, direction):
        self.playerRect.move_ip((self.speed * direction.x), (self.speed * direction.y))








