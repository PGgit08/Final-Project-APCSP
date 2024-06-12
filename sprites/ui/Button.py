import pygame
from base_sprite import BaseSprite

class Button(BaseSprite):
    
    def __init__(self, group, text):
        super().__init__(group)

        self.text = text
        
        self.font = pygame.font.SysFont("Poppins", 14)
        self.load_surface("/assets/button.png")
        
    


