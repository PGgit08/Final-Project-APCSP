import pygame
from sprites.base_sprite import BaseSprite
from globals import globals

class Text(BaseSprite):
    text = None

    def __init__(self, text):
        super().__init__(globals.uis)

        self.text = text

        self.image = pygame.font.SysFont("Arial", 2).render(text, True, (0, 0, 0))

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.rotate(self.image, self.offset_angle)
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))
        
        # set image to the original image
        self.image = self.original_image

        self.pos = pygame.Vector2(100, 100)

