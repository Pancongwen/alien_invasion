import pygame

class Ship():
    """Creat class ship
    """
    def __init__(self, setting, screen):
        """Initialize the spacecraft and set its initial position
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
        self.MovingUp = False
        self.MovingDown = False

    def update(self):
        """Adjust the position of the spacecraft according to the moving sign
        """
        if self.MovingRight and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.setting.ShipSpeed
        # use if not elif
        # if type down both left and right, it will stay still
        if self.MovingLeft and self.rect.left > 0:
            self.rect.centerx -= self.setting.ShipSpeed

        if self.MovingUp and self.rect.bottom > 0:
            self.rect.bottom -= self.setting.ShipSpeed

        if self.MovingDown and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.setting.ShipSpeed

    def blitme(self):
        """Draw the image to a specified location on the screen
        """
        self.screen.blit(self.image, self.rect)

