import pygame
import sys
from raindrop import Raindrop
from settings import Settings

class Exercise():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        self.raindrops = pygame.sprite.Group()
        self._make_rain()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
        
            self.clock.tick(60)
    
    def _make_rain(self):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        current_x, current_y = -drop_width, -drop_height

        while current_y < self.settings.screen_height:
            while current_x < self.settings.screen_width:
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width

            current_y += drop_height
            current_x = -drop_width

    def _create_drop(self, x_pos, y_pos):
        new_drop = Raindrop(self)
        new_drop.x = x_pos
        new_drop.rect.x = y_pos
        new_drop.rect.y = y_pos
        self.raindrops.add(new_drop)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            if event.type == pygame.KEYUP:
                self._check_keyup(event)
    
    def _check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup(self, event):
        pass
    
    def _check_edges(self):
        need_new_row = False
        for drop in self.raindrops.sprites():
            if self.check_edges(drop):
                self.raindrops.remove(drop)
                need_new_row = True
        if need_new_row:
            self._new_row()
            need_new_row = False    
    
    def _new_row(self):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        current_x, current_y = -drop_width, -drop_height

        while current_y < self.settings.screen_height:
            self._create_drop(current_x, current_y)
            current_y += drop_height

    def _update_raindrops(self):
        self._check_edges()
        self.raindrops.update()

    def check_edges(self, drop):
        screen_rect = self.screen.get_rect()
        return (drop.rect.left >= screen_rect.right) or (drop.rect.top >= screen_rect.bottom)

    def _update_screen(self):
        self.screen.fill(self.settings.color)
        self._update_raindrops()
        self.raindrops.draw(self.screen)
        print(len(self.raindrops))
        pygame.display.flip()

if __name__ == '__main__':
    instance = Exercise()
    instance.run()