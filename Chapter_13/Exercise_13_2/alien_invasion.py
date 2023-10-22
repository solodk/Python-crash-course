import sys
import pygame

from random import randint
from settings import Settings
from star import Star

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
        
        # Fullscreen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Alien Invasion")

        self.stars = pygame.sprite.Group()

        self._create_row()

    def run_game(self):
        """
        Start the main loop for the game.
        """
        while True:
            #self._check_events()
            #self.ship.update()
            #self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _create_row(self): 
        """
        Create the fleet of aliens.
        """
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens in one alien width and one alien height.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                random_number = randint(-10, 10)
                current_x += random_number
                current_y += random_number

                self._create_star(current_x, current_y)
                
                current_x -= random_number
                current_y -= random_number
                current_x += 2 * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """
        Create an alien and place it in the row
        """
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """
        Respond to key releases
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """
        Create a new bullet and add it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Update position of bullets and get rid of old bullets
        """
        # Update bullet positions.
        self.bullets.update()
        
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """
        Update images on the screen, and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        #for bullet in self.bullets.sprites():
        #    bullet.draw_bullet()
        #self.ship.blitme()
        self.stars.draw(self.screen)

        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()