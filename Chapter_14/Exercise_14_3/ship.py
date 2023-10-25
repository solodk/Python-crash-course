import pygame

class Ship():

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        self.moving_up = False
        self.moving_down = False

        self.reset()

    def update(self):
        if self.moving_up and self.rect.top >= self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
    
        self.rect.y = self.y


    def reset(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)