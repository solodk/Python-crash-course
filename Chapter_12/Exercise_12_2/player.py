import pygame

class Player:
    """
    A class to manage the player.
    """

    def __init__(self, ai_game):
        """
        Initialize the player and set its starting position.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the player image and get its rect.
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """
        Draw the player at its current location.
        """
        self.screen.blit(self.image, self.rect)