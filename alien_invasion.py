import pygame
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

        while True:
            gf.check_events(Ship)
            Ship.update()
            gf.update_screen(self.setting.WindowColor, screen, Ship)
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion(setting)
    GAME.run()