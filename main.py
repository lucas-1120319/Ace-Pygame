from operator import truediv

import pygame
from pygame import mixer

from entities.player import Player
from entities.button import Button

pygame.init()
mixer.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FRAMES_PER_SECOND = 60
game_clock = pygame.time.Clock()
player_class = Player(screen)

# load sfx for player movement
player_move_left_sfx = pygame.mixer.Sound("Assets/Sound_Effects/player-whoosh.wav")
player_move_right_sfx = pygame.mixer.Sound("Assets/Sound_Effects/player-whoosh.wav")

# set volume
player_move_left_sfx.set_volume(0.5)
player_move_right_sfx.set_volume(0.5)


#Background (image)
background = pygame.image.load("Assets/Backgrounds/Purple_Nebula_05-1024x1024.png").convert_alpha()
scaled_background = pygame.transform.smoothscale(background, (1280, 720)) # scale background to screen size
background_rect = scaled_background.get_rect()

#Button instance
position = (SCREEN_WIDTH/2 , SCREEN_HEIGHT/3)
load_button = pygame.image.load("Assets/UI/play_button.png").convert_alpha()
scale_button = pygame.transform.smoothscale(load_button, (200, 75))
play_button = Button(scale_button,  position)

#Defining Game state
game_state = "Menu"


def key_pressed():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        player_class.move(-1) # left
    elif pressed_keys[pygame.K_d]:
        player_class.move(1) # right
    else:
        player_class.move(0) #default (glide)
    player_class.update()

# --- Main Game Loop ---

while True:
    # --- 1. EVENT HANDLING SECTION ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # --- State-specific event handling ---
        if game_state == "Menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_hovering():
                    # Play a sound when the button is clicked, then change state
                    # player_move_left_sfx.play() # Example sound
                    game_state = "Playing"

        elif game_state == "Playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_move_left_sfx.play(maxtime=200)
                if event.key == pygame.K_d:
                    player_move_right_sfx.play(maxtime=200)

    # --- 2. GAME LOGIC SECTION ---
    if game_state == "Playing":
        key_pressed()

    # --- 3. DRAWING SECTION ---

    if game_state == "Menu":
        play_button.draw(screen)

    elif game_state == "Playing":
        screen.blit(scaled_background, background_rect)
        player_class.update()

    pygame.display.flip()
    game_clock.tick(FRAMES_PER_SECOND)

pygame.quit()