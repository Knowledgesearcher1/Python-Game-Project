import pygame 
from pygame.sprite import Sprite 

class Enemy(Sprite):
    """A class to represent single enemyship in the fleet"""

    def __init__(self, settings, screen) -> None:
        super().__init__() # initialize the parent class 
        self.screen = screen 
        self.settings = settings 

        # Load the enemy ship image and set it's rect attribute 
        self.image = pygame.image.load("assets/enemyship.png")
        self.rect = self.image.get_rect()

        # Start each new enemyship near the top left to the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        # Store the each enemyship's exact position 
        self.x = float(self.rect.x)

    def display(self):
        """Draw the enemy ship at its current location"""
        self.screen.blit(self.image, self.rect)