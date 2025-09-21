import pygame
import math
from pygame import Vector2


class Player():

    def __init__(self, screen):
        self.screen = screen
        self.speed = 0.2
        self.max_speed = 15
        self.velocity = 0
        self.DEFAULT_IMAGE = 2 # default forward spaceship image
        self.spriteSheet_image = self.DEFAULT_IMAGE

        self.player_img = pygame.image.load("Assets/Player/Player01-Sheet.png").convert_alpha()


        #first frame is needs to be the size of one player not the whole spritesheet
        first_frame = self.get_image(self.spriteSheet_image, 48, 48, 1)

        #clean copy, pre rotation
        self.original_image = first_frame

        #This  will hold the current image to be drawn
        self.image = self.original_image.copy()

        #Get the rectangle
        self.rect = self.image.get_rect(center=(screen.get_size()[0] / 2, screen.get_size()[1] / 1.1))


    def get_image(self, frame,  width, height, scale):
        #https://www.youtube.com/watch?v=M6e3_8LHc7A
        #get a part of the larger sprite sheet
        #pygame.srcalpha and covert_alpha is for the transparancy
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.player_img, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image


    def update(self):
        # This gets the un-rotated image based on the player's current movement state.
        base_animation_frame = self.get_image(self.spriteSheet_image, 48, 48, 1)

        # Get the current position of the mouse and the player's center
        mouse_pos = pygame.mouse.get_pos()
        player_center = self.rect.center

        # Calculate the angle between the player and the mouse in degrees https://www.reddit.com/r/pygame/comments/pjzf2b/angle_to_mouse/ https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.angle_to
        dx = mouse_pos[0] - player_center[0]
        dy = mouse_pos[1] - player_center[1]
        angle = math.degrees(math.atan2(-dy, dx)) - 90

        # Rotate the CURRENT animation frame (not the original_image anymore)
        self.image = pygame.transform.rotate(base_animation_frame, angle)

        # Update the rect to prevent the sprite from wobbling as it rotates
        self.rect = self.image.get_rect(center=player_center)

        self.screen.blit(self.image, self.rect)


    def move(self, direction):
        #set velocity based on the a or d button
        self.velocity += (direction * self.speed)

        #show correct image
        self.spriteSheet_image = self.DEFAULT_IMAGE + direction
        if direction != 0:
            #set lean pose if the velocity matches the direction
            self.spriteSheet_image = self.DEFAULT_IMAGE + direction
            if abs(self.velocity) > self.max_speed * (1 / 3) and (self.velocity * direction) > 0:
                self.spriteSheet_image = self.DEFAULT_IMAGE + (2 * direction)

        #speed limiter
        if self.velocity >= self.max_speed:
            self.velocity = self.max_speed
        if self.velocity <= -self.max_speed:
            self.velocity = -self.max_speed

        self.rect.move_ip(self.velocity, (self.speed * direction))

        #border detection
        if self.rect.left < self.screen.get_rect().left:
            self.rect.left = self.screen.get_rect().left
            self.velocity = 0
        if self.rect.right > self.screen.get_rect().right:
            self.rect.right = self.screen.get_rect().right
            self.velocity = 0








