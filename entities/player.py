import pygame

class Player():
    def __init__(self, screen):
        player_img = pygame.image.load("Assets/Player/Player.png")
        playerRect = player_img.get_rect()
        screen.blit(player_img, playerRect)

    def update(self):
        pass
