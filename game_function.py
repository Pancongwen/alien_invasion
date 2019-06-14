import sys
import pygame

def check_events(ship):
    """
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
<<<<<<< HEAD
            if event.key == pygame.K_RIGHT:
                ship.MovingRight = True
            elif event.key == pygame.K_LEFT:
                ship.MovingLeft = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.MovingRight = False
            elif event.key == pygame.K_LEFT:
                ship.MovingLeft = False
=======
            check_keydown_event(event, ship)
            
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_keyup_event(event, ship):
    """
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
    """
    """
    if event.key == pygame.K_RIGHT:
        ship.MovingRight = True
    if event.key == pygame.K_LEFT:
        ship.MovingLeft = True
    if event.key == pygame.K_UP:
        ship.MovingUp = True
    if event.key == pygame.K_DOWN:
        ship.MovingDown = True
>>>>>>> c0397d8c297c5e72b04bbdeefb6702a648d58465

def update_screen(setting, screen, ship):
    """
    """
    screen.fill(setting)
    ship.blitme()