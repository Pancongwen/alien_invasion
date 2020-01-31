import sys
import pygame

from bullet import Bullet

def check_events(setting, screen, ship, bullets):
    """Respond to button and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, setting, screen, ship, bullets)

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

def check_keydown_event(event, setting, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        fire_bullets(setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def update_screen(setting, screen, ship, bullets):
    """Update the image on the screen and switch to the new screen
    """
    screen.fill(setting)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blitme()

def update_bullets(bullets):
    """Update bullets location and remove bullets that fly out of window
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))

def fire_bullets(setting, screen, ship, bullets):
    """Fire bullets if bullets number is not reach limit
    """
    if len(bullets) < setting.BulletAllowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)
