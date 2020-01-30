import pygame
from pygame.sprite import Group

import game_function as gf
import setting
import ship

class AlienInvasion():
    """Creat class AlienInvasion
    """
    def __init__(self, setting):
        """Initialize the game's settings
        """
        self.setting = setting.Setting()

    def run(self):
        """Initialize the game and create a screen object
        """
        pygame.init()
        pygame.display.set_caption(self.setting.WindowTitle)
        screen = pygame.display.set_mode((self.setting.WindowWeight, self.setting.WindowHeight))
        
        Ship = ship.Ship(self.setting, screen)
        bullets = Group()

        while True:
            gf.check_events(self.setting, screen, Ship, bullets)
            Ship.update()
            bullets.update()
            gf.update_screen(self.setting.WindowColor, screen, Ship, bullets)
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion(setting)
    GAME.run()