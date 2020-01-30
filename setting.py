
class Setting():
    """Class that stores all settings for Alien Invasion
    """
    def __init__(self):
        """Initialize the game's settings
        """
        self.WindowWeight = 1200
        self.WindowHeight = 800
        self.WindowTitle = "Alien Invasion"
        self.WindowColor = (230, 230, 230)
    
        self.ShipSpeed = 1

        self.BulletSpeedFactor = 1
        self.BulletWidth = 3
        self.BulletHeight = 13
        self.BulletColor = 60, 60, 60