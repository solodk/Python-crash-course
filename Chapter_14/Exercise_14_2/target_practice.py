import pygame
from time import sleep
import sys

from settings import Settings
from bullet import Bullet
from ship import Ship
from button import Button
from target import Target
from game_stats import GameStats

class TargetPractice:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        self.game_active = False

        self.target = Target(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.stats = GameStats()
        self.button = Button(self, "Play")

    def run(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.target.update()
            self._screen_update()
            self.clock.tick(60)

    def _start_game(self):
        #self.stats.reset()
        #self.aliens.empty()
        self.bullets.empty()
        self.ship.reset()
        self.stats.reset()
        self.target.reset()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets:
            if bullet.rect.left >= self.settings.screen_width:
                self._bullet_miss(bullet)
        
        self._check_bullet_target_collision()

    def _bullet_miss(self, bullet):
        if self.stats.lives > 0:
            self.bullets.remove(bullet)
            self.stats.lives += -1
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()

    def _check_keyup(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        pressed = self.button.rect.collidepoint(mouse_pos)
        if pressed and not self.game_active:
            self._start_game()

    def _check_bullet_target_collision(self):
        collison = pygame.sprite.spritecollide(
            self.target, self.bullets, True
            )

        if collison:
            self._target_hit()

    def _target_hit(self):
        self.stats.score += 1
        print('THERE IS HIT')

    def _screen_update(self):
        self.screen.fill(self.settings.screen_bg_color)
        #self.ship.blit()
        self.target.draw_target()
        self.screen.blit(self.ship.image, self.ship.rect)
        for bullet in self.bullets:
            bullet.draw_bullet()

        if not self.game_active:
            self.button.draw_button()

        pygame.display.flip()

if __name__ == "__main__":
    game = TargetPractice()
    game.run()