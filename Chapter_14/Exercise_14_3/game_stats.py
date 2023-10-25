class GameStats:
    def __init__(self):
        self.life_limit = 3
        
        self.reset()

    def reset(self):
        self.lives = self.life_limit
        self.score = 0