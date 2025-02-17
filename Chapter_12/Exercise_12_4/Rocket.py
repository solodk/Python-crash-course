import sys
import pygame

from settings import Settings
from rocket import Rocket

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
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Rocket")
        
        self.rocket = Rocket(self)

    def run_game(self):
        """
        Start the main loop for the game.
        """
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

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
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = True
        elif event.key == pygame.K_UP:
            self.rocket.move_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = False
        elif event.key == pygame.K_UP:
            self.rocket.move_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False

    def _update_screen(self):
        """
        Update images on the screen, and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()