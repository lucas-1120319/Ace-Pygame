import pygame
from pygame import Vector2

from entities.player import Player
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
game_clock = pygame.time.Clock()
player_class = Player(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("red")

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_class.move(Vector2(-1, 0))
    if pressed_keys[pygame.K_d]:
        player_class.move(Vector2(1, 0))
    player_class.update()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
pygame.quit()
