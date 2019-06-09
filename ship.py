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

        self.MovingRight = False
        self.MovingLeft = False

    def update(self):
        """
        """
        if self.MovingRight:
            self.rect.centerx += 1
        elif self.MovingLeft:
            self.rect.centerx -= 1

    def blitme(self):
        """
        """
        self.screen.blit(self.image, self.rect)

