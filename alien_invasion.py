import sys
import pygame

class Ship():
    """
    """
    def __init__(self, screen):
        """
        """
        self.screen = screen
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """
        """
        self.screen.blit(self.image, self.rect)


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
        
        ship = Ship(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.fill(self.WindowColor)
            ship.blitme()
            pygame.display.flip()

if __name__ == "__main__":
    GAME = AlienInvasion()
    GAME.run()