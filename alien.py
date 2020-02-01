import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    """
    def __init__(self, setting, screen):
        """Initialize alien and set its' init location
        """
        super().__init__()
        self.screen = screen
        self.setting = setting

        # load image and get rect
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # set the alien init location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien
        """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Alien movement
        """
        self.x += self.setting.AlienSpeedFactor * self.setting.FleetDirection
        self.rect.x = self.x
