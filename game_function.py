import sys
import pygame

def check_events(ship):
    """
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
            
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_keyup_event(event, ship):
    """
    """
    if event.key == pygame.K_RIGHT:
        ship.MovingRight = False
    elif event.key == pygame.K_LEFT:
        ship.MovingLeft = False

def check_keydown_event(event, ship):
    """
    """
    if event.key == pygame.K_RIGHT:
        ship.MovingRight = True
    elif event.key == pygame.K_LEFT:
        ship.MovingLeft = True

def update_screen(setting, screen, ship):
    """
    """
    screen.fill(setting)
    ship.blitme()