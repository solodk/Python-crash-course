import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStat

class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """

    def __init__(self):
        """
        Initialize the game, and create game resources.
        """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.game_active = True
        self.stats = GameStat(self)
        
        # Fullscreen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        """
        Start the main loop for the game.
        """
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)

    def _create_alien(self):
        new_alien = Alien(self)
        self.aliens.add(new_alien)

    def _update_aliens(self):
        if not self.aliens:
            self._create_alien()
        else:
            self.aliens.update()

    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        Respond to keypresses
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_bullet_alien_colisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
            self.stats.score += 1

    def _check_keyup_events(self, event):
        """
        Respond to key releases
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """
        Create a new bullet and add it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.ship.center_ship()
            self.bullets.empty()
            self.aliens.empty()

            sleep(0.5)
        else:
            self.game_active = False

    def _update_bullets(self):
        """
        Update position of bullets and get rid of old bullets
        """
        # Update bullet positions.
        self.bullets.update()
        
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_colisions()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _update_screen(self):
        """
        Update images on the screen, and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()