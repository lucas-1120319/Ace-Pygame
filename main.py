import pygame
from pygame import Vector2

from entities.player import Player
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
game_clock = pygame.time.Clock()
player_class = Player(screen)
def key_pressed():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_class.move(Vector2(-1, 0))
    if pressed_keys[pygame.K_d]:
        player_class.move(Vector2(1, 0))
    player_class.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("red")
    key_pressed()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)
pygame.quit()
