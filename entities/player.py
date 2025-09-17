import pygame

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.speed = 12
        self.player_img = pygame.image.load("Assets/Player/Player.png")
        self.playerRect = self.player_img.get_rect(center=(screen.get_size()[0] / 2,screen.get_size()[1] /1.15 ))
        screen.blit(self.player_img, self.playerRect)


    def update(self):
        self.screen.blit(self.player_img, self.playerRect)
    def move(self, direction):
        print(self.playerRect.x)
        if self.playerRect.x >= 10:
            self.playerRect.move_ip((self.speed * direction.x), (self.speed * direction.y))









