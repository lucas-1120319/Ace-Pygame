import pygame

class Player():

    def __init__(self, screen):
        self.screen = screen
        self.speed = 0.2
        self.max_speed = 15
        self.velocity = 0
        self.DEFAULT_IMAGE = 2 # default forward spaceship image
        self.spriteSheet_image = self.DEFAULT_IMAGE

        self.player_img = pygame.image.load("Assets/Player/Player01-Sheet.png").convert_alpha()
        #first frame is needs to be the size of one player not the hole spritesheet
        first_frame = self.get_image(self.spriteSheet_image, 48, 48, 1)
        self.playerRect = first_frame.get_rect(center=(screen.get_size()[0] / 2, screen.get_size()[1] / 1.1))


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

        self.playerRect.move_ip(self.velocity, (self.speed * direction))

        #border detection
        if self.playerRect.left < self.screen.get_rect().left:
            self.playerRect.left = self.screen.get_rect().left
            self.velocity = 0
        if self.playerRect.right > self.screen.get_rect().right:
            self.playerRect.right = self.screen.get_rect().right
            self.velocity = 0








