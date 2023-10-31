import pygame 

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set it's starting position"""
        self.screen = screen 

        # Load the ship image 
        self.image = pygame.image.load("assets/playership.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen 
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom 

    
    def draw(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)