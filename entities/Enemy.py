import pygame
from random import randrange

class Enemy():

    def __init__(self, screen):
        self.screen = screen
        self.speed = 0.1
        self.max_speed = 10
        self.velocity = 0
        self.DEFAULT_IMAGE = 0
        self.spriteSheet_image = self.DEFAULT_IMAGE

        self.EnemyImg = pygame.image.load("Assets/Enemies/fighter1.png").convert_alpha()

        #first frame is size of one enemy, not entire spriteSheet
        first_frame = self.get_image(self.spriteSheet_image,48,48,1)
        self.original_image = first_frame

        #rectangle maken om de enemy heen, zodat we collision kunnen meten
        self.rect = self.original_image.get_rect(center =(screen.get_size()[0] /3,screen.get_size()[1]/ 8))

    def get_image(self, frame, width, height, scale):
        # https://www.youtube.com/watch?v=M6e3_8LHc7A
        # get a part of the larger sprite sheet
        # pygame.srcalpha and covert_alpha is for the transparancy
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.EnemyImg, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def update(self):
        self.rect.y += self.velocity
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.velocity = -self.velocity
