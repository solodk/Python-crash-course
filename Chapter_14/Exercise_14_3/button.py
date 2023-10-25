import pygame.font

class Button:

    def __init__(self, game, msg):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(
            0, 0, self.settings.button_width, self.settings.button_height
        )
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
    
    def draw_button(self):
        self.screen.fill(self.settings.button_bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
    def _prep_msg(self, msg):
        self.msg_image = self.settings.button_font.render(
            msg, 
            True, 
            self.settings.button_text_color,
            self.settings.button_bg_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center