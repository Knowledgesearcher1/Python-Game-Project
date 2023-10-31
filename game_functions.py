import sys 
import pygame

# Load the back ground image 
bg = pygame.image.load("assets/bg.jpg")
    
def check_keydown_events(event, ship):
    """Respond to keydown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 

def check_keyup_events(event, ship):
    """Respond to keyup events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 

def check_events(ship):
    """ Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(screen, ship, stars):
    """Updae images on the screen and flip to the next screen"""
    # Redraw the screen during each pass through the loop 
    stars.update()
    screen.blit(bg, (0,0))
    stars.draw()
    ship.update()
    ship.draw()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()