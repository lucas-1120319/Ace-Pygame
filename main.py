import pygame
from entities.player import Player
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    player_class = Player(screen)
    pygame.display.flip()

pygame.quit()