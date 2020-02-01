import pygame
from pygame.sprite import Group

import game_function as gf
from setting import Setting
from ship import Ship
from alien import Alien

class AlienInvasion():
    """Creat class AlienInvasion
    """
    def __init__(self, setting):
        """Initialize the game's settings
        """
        self.setting = Setting()

    def run(self):
        """Initialize the game and create a screen object
        """
        pygame.init()
        pygame.display.set_caption(self.setting.WindowTitle)
        screen = pygame.display.set_mode((self.setting.WindowWidth, self.setting.WindowHeight))
        
        # create ship, bullets group and aliens group
        ship = Ship(self.setting, screen)
        bullets = Group()
        aliens = Group()

        # create alien fleet
        gf.create_fleet(self.setting, screen, ship, aliens)

        while True:
            gf.check_events(self.setting, screen, ship, bullets)
            ship.update()
            gf.update_bullets(self.setting, screen, ship, aliens, bullets)
            gf.update_aliens(self.setting, aliens)
            gf.update_screen(self.setting.WindowColor, screen, ship, aliens, bullets)
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion(Setting)
    GAME.run()