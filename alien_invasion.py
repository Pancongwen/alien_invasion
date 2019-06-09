import pygame
import game_function as gf
import ship

class AlienInvasion():
    """
    """
    def __init__(self):
        """
        """
        self.WindowWeight = 1200
        self.WindowHeight = 800
        self.WindowTitle = "Alien Invasion"
        self.WindowColor = (230, 230, 230)

    def run(self):
        """
        """
        pygame.init()
        pygame.display.set_caption(self.WindowTitle)
        screen = pygame.display.set_mode((self.WindowWeight, self.WindowHeight))
        
        Ship = ship.Ship(screen)

        while True:
            gf.check_events(Ship)
            gf.update_screen(self.WindowColor, screen, Ship)
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion()
    GAME.run()