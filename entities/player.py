import pygame

class Player():

    def __init__(self, screen):
        self.screen = screen
        self.speed = 12
        # img = pygame.image.load("Assets/Player/Player.png")
        self.player_img = pygame.image.load("Assets/Player/Player01-Sheet.png")
        self.default_image = 2 # default forward image

        img_width = 25
        img_height = 25
        self.playerRect = self.player_img.get_rect(center=(screen.get_size()[0] / 2, screen.get_size()[1] / 1.1 ))
        screen.blit(self.player_img, self.playerRect)

    def get_image(self, frame,  width, height, scale):
        #https://www.youtube.com/watch?v=M6e3_8LHc7A
        image = pygame.Surface((width, height))
        image.blit(self.player_img, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def update(self):
        image = self.get_image(self.default_image,48, 48, 1)
        self.screen.blit(image, self.playerRect)
        self.default_image = 2



    def move(self, direction):
        self.playerRect.move_ip((self.speed * direction.x), (self.speed * direction.y))
        self.default_image = 2 + direction.x
        #border detection
        if self.playerRect.left < 0:
            self.playerRect.left = 0
        if self.playerRect.right > 1280:
            self.playerRect.right = 1280









