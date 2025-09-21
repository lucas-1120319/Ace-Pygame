import pygame

class Button():
    def __init__(self, button_image, button_position):
        self.button_image = button_image
        self.button_position = button_position

        self.button_size = self.button_image.get_size()
        self.button_rect = self.button_image.get_rect()

        #Centers the position of the button, according to the class argument
        self.button_rect.center = button_position

        # Create the hover image by scaling the original's width [0] and height [1] by 1.2 and converting them to integers.
        self.hovered_image = pygame.transform.smoothscale(self.button_image, (int(self.button_size[0] * 1.2), int(self.button_size[1] * 1.2)))


    def is_hovering(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False


    def draw(self, screen):

        if self.is_hovering() == True:
            screen.blit(self.hovered_image, self.button_rect)
        else:
            screen.blit(self.button_image, self.button_rect)
