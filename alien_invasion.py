import pygame
from pygame.sprite import Group

import game_function as gf
import setting
from ship import Ship
from alien import Alien

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
        
        ship = Ship(self.setting, screen)
        bullets = Group()
        alien = Alien(self.setting, screen)

        while True:
            gf.check_events(self.setting, screen, ship, bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_screen(self.setting.WindowColor, screen, ship, alien, bullets)
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion(setting)
    GAME.run()