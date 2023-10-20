import pygame

class Rocket:
    """
    A class to manage the rocket.
    """

    def __init__(self, ai_game):
        """
        Initialize the rocket and set its starting position.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right:
            self.x += self.settings.rocket_speed
        if self.move_left:
            self.x -= self.settings.rocket_speed
        if self.move_up:
            self.y -= self.settings.rocket_speed
        if self.move_down:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()

    def blitme(self):
        """
        Draw the rocket at its current location.
        """
        self.screen.blit(self.image, self.rect)