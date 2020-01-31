import sys
import pygame

from bullet import Bullet
from alien import Alien

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

def update_screen(setting, screen, ship, alien, bullets):
    """Update the image on the screen and switch to the new screen
    """
    screen.fill(setting)
    for bullet in bullets.sprites():
        bullet.draw()
    ship.blitme()
    alien.draw(screen)

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
        
def get_number_aliens_x(setting, alien_width):
    """
    """
    avaliable_space_x = setting.WindowWidth - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(setting, ship_height, alien_height):
    """Calculate the row number of aliens
    """
    avaliable_space_y = setting.WindowHeight - (3 * alien_height) - ship_height
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows

def create_alien(setting, screen, aliens, alien_number, row_number):
    """
    """
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(setting, screen, ship, aliens):
    """
    """
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(setting, alien_width)
    number_rows = get_number_rows(setting, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(setting, screen, aliens, alien_number, row_number)