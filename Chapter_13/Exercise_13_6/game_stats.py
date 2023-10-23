class GameStat:
    def __init__(self, game):
        self.settings = game.settings
        self.reset()

    def reset(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0