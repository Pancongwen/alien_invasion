import pygame

class Ship():
    """
    """
    def __init__(self, setting, screen):
        """
        """
        self.setting = setting
        self.screen = screen
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # ship init location
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # move variabes
        self.MovingRight = False
        self.MovingLeft = False

    def update(self):
        """
        """
        if self.MovingRight:
            self.rect.centerx += self.setting.ShipSpeed
        # use if not elif
        # if type down both left and right, it will stay still
        if self.MovingLeft:
            self.rect.centerx -= self.setting.ShipSpeed

    def blitme(self):
        """
        """
        self.screen.blit(self.image, self.rect)

