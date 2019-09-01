class Settings():
    """Initialize the game's settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        #ship settings:
        self.ship_speed_factor = 1.5

        #Bullet settings:
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60