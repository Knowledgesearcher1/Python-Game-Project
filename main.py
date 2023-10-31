import sys 
import pygame

from settings import Settings 

def run_game():
    # Initailize the game 
    pygame.init()
    
    settings = Settings()
    # create screen object 
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Cosmic Defenders")

    # Start the main loop for the game 
    while True:

        # Watch keybaord and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        # Redraw the screen during each pass through the loop 
        screen.fill(settings.bg_color)
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()