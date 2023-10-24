import pygame.font

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (123,123,123)
        
        # Ship
        self.ships_limit = 3
        self.ship_speed = 5

        # Bullet
        self.bullet_width = 15
        self.bullet_height = 2
        self.bullet_speed = 20
        self.bullet_color = (255,255,255)

        # Button
        self.button_bg_color = (0,155,23)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)
        self.button_width = 150
        self.button_height = 50
       
        # Target
        self.target_width = 75
        self.target_height = 75
        self.target_speed = 1
        self.target_color = (0,0,235)