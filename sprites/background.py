import pygame
import os
from globals import WIDTH, HEIGHT, backgrounds

class Background(pygame.sprite.Sprite):
    pos = pygame.Vector2(0, 0)

    angle = 0
    old_angle = 0

    def __init__(self):
        super().__init__(backgrounds)

        self.image = pygame.image.load(os.getcwd() + "/assets/background.png")

        # original image is a scaled down non-rotated image of the background
        self.original_image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        
        # reset image to the original image
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.Surface.convert_alpha(self.image)

        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos
