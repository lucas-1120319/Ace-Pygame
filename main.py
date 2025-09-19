import pygame
from pygame import mixer

from entities.player import Player

pygame.init()
mixer.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
game_clock = pygame.time.Clock()
player_class = Player(screen)

# load sfx for player movement
player_move_left_sfx = pygame.mixer.Sound("Assets/Sound_Effects/player-whoosh.wav")
player_move_right_sfx = pygame.mixer.Sound("Assets/Sound_Effects/player-whoosh.wav")

# set volume
player_move_left_sfx.set_volume(0.5)
player_move_right_sfx.set_volume(0.5)


def key_pressed():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_class.move(-1) # left
    elif pressed_keys[pygame.K_d]:
        player_class.move(1) # right
    else:
        player_class.move(0) #default (glide)
    player_class.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # play sound once when key is pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_move_left_sfx.play(maxtime=200)
            if event.key == pygame.K_d:
                player_move_right_sfx.play(maxtime=200)

    screen.fill("red")
    key_pressed()
    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)

pygame.quit()
