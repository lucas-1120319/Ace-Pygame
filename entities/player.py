import pygame

class Player():

    def __init__(self, screen):
        self.screen = screen
        self.speed = 12
        self.DEFAULT_IMAGE = 2 # default forward spaceship image
        self.spriteSheet_image = self.DEFAULT_IMAGE

        self.player_img = pygame.image.load("Assets/Player/Player01-Sheet.png").convert_alpha()
        #first frame is needs to be the size of one player not the hole spritesheet
        first_frame = self.get_image(self.spriteSheet_image, 48, 48, 1)
        self.playerRect = first_frame.get_rect(center=(screen.get_size()[0] / 2, screen.get_size()[1] / 1.1))

        screen.blit(self.player_img, self.playerRect)


    def get_image(self, frame,  width, height, scale):
        #https://www.youtube.com/watch?v=M6e3_8LHc7A
        #get a part of the larger sprite sheet
        #pygame.srcalpha and covert_alpha is for the transparancy
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.player_img, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def update(self):
        image = self.get_image(self.spriteSheet_image,48, 48, 1)
        self.screen.blit(image, self.playerRect)
        self.spriteSheet_image = self.DEFAULT_IMAGE


    def move(self, direction):
        self.playerRect.move_ip((self.speed * direction.x), (self.speed * direction.y))
        self.spriteSheet_image = self.DEFAULT_IMAGE + direction.x
        #border detection
        if self.playerRect.left < self.screen.get_rect().left:
            self.playerRect.left = self.screen.get_rect().left
        if self.playerRect.right > self.screen.get_rect().right:
            self.playerRect.right = self.screen.get_rect().right









