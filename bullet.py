import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    """
    def __init__(self, setting, screen, ship):
        """
        """
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(
            0, 0,
            setting.BulletWidth,
            setting.BulletHeight
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = setting.BulletColor

        self.speed = setting.BulletSpeedFactor

    def update(self):
        """
        """
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        """
        """
        pygame.draw.rect(self.screen, self.color, self.rect)