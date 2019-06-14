import sys
import pygame

def check_events(ship):
    """
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.MovingRight = True
            elif event.key == pygame.K_LEFT:
                ship.MovingLeft = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.MovingRight = False
            elif event.key == pygame.K_LEFT:
                ship.MovingLeft = False

def update_screen(setting, screen, ship):
    """
    """
    screen.fill(setting)
    ship.blitme()