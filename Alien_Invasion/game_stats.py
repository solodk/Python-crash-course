from pathlib import Path
import json

class GameStats:
    """
    Track statistics for Alien Invasion.
    """

    def __init__(self, ai_game):
        """
        Initialize statistics.
        """
        self.settings = ai_game.settings
        self.file = Path("highscore.json")

        self.reset_stats()
        self.load()


    def reset_stats(self):
        """
        Initialize statistics that can change during the game.
        """
        self.score = 0
        self.level = 1
        self.ships_left = self.settings.ship_limit

    def save(self):
        """
        Saves high score from file
        """
        dictionary = {
            "high_score":self.high_score
        }
        content = json.dumps(dictionary)
        self.file.write_text(content)
    def load(self):
        """
        Loads high score from file
        """
        try:
            content = self.file.read_text()
            dictionary = json.loads(content)
            self.high_score = dictionary["high_score"]
        except Exception as ex:
            print(ex)
            self.high_score = 0    