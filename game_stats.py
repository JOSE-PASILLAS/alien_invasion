class GameStats():
    """Track statistics for alein invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start alien invasion in an active state
        self.game_active = False
        # High score should never be reset
        self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """Read highest score"""
        f = open("high_score.txt", "r")
        if f.mode == 'r':
            self.high_score = int(f.read())
        f.close()

