import pygame
from random import choice

class Target:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.color = self.settings.target_color
        self.rect = pygame.Rect(
            0, 0, self.settings.target_width, self.settings.target_height
            )
        self.reset()

    def update(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.settings.screen_height:
            self.dirrection = 1 if self.dirrection != 1 else -1

        self.y += self.settings.target_speed * self.dirrection
        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def reset(self):
        self.rect.midright = self.screen.get_rect().midright
        self.y = self.rect.y
        self.dirrection = choice([1, -1])
