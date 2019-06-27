import sys
import pygame

def check_events(ship):
    """Respond to button and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
            
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_keyup_event(event, ship):
    """Respond to button and mouse events
    """
    if event.key == pygame.K_RIGHT:
        ship.MovingRight = False
    if event.key == pygame.K_LEFT:
        ship.MovingLeft = False
    if event.key == pygame.K_UP:
        ship.MovingUp = False
    if event.key == pygame.K_DOWN:
        ship.MovingDown = False

def check_keydown_event(event, ship):
    """Respond to button and mouse events
    """
    if event.key == pygame.K_RIGHT:
        ship.MovingRight = True
    if event.key == pygame.K_LEFT:
        ship.MovingLeft = True
    if event.key == pygame.K_UP:
        ship.MovingUp = True
    if event.key == pygame.K_DOWN:
        ship.MovingDown = True

def update_screen(setting, screen, ship):
    """Update the image on the screen and switch to the new screen
    """
    screen.fill(setting)
    ship.blitme()