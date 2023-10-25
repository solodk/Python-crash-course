class Settings:
    """
    A class to store all settings for Alien Invasion.
    """

    def __init__(self):
        """
        Initialize the game's settings.
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings  
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Difficulties
        self.difficulty_list = ['Easy', 'Normal', 'Hard']
        self.difficulty_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, mode='Easy'):
        """
        Initialize settings that change throughout the game.
        """
        self.difficulty_scale += self.difficulty_list.index(mode)
        
        self.ship_speed = 15 * self.difficulty_scale
        self.bullet_speed = 20.0 * self.difficulty_scale
        self.alien_speed = 10.0 * self.difficulty_scale

        # fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """
        Increase speed settings.
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale