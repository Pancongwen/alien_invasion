import sys
import pygame

class AlienInvasion():
    """
    """
    def __init__(self):
        """
        """
        self.WindowWeight = 1200
        self.WindowHeight = 800
        self.WindowTitle = "Alien Invasion"

    def run(self):
        """
        """
        pygame.init()
        pygame.display.set_mode((self.WindowWeight, self.WindowHeight))
        pygame.display.set_caption(self.WindowTitle)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion()
    GAME.run()