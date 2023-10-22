import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = 1

    def update(self):
        self.x += self.settings.raindrop_x_speed
        #self.y += self.settings.raindrop_y_speed
        self.rect.x = self.x
        #self.rect.y = self.y
    
    