import sys
import pygame

def check_events():
    """
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(setting, screen, ship):
    """
    """
    screen.fill(setting)
    ship.blitme()