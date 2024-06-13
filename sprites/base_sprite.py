import pygame
import os

# base sprite for all sprites in this game
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        # the sprite's position
        self.pos = pygame.Vector2(0, 0) 

        # width
        self.width = 100

        # height
        self.height = 100

        # colorkey
        self.colorkey = (255, 255, 255)

        # the sprite's angle
        self.angle = 0
        self.old_angle = 0

        # the angle to offset the image by
        self.offset_angle = 0

        # the original image for this sprite
        self.original_image = None

        # the path for this sprite's image
        self.image_src = None

    
    # loads the surface for this sprite
    # if image_src is none, then a rectangle of given specified width/height is created
    def load_surface(self, color=None):
        if (self.image_src != None):
            self.image = pygame.image.load(os.getcwd() + self.image_src)

        else:
            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(color)

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.rotate(self.image, self.offset_angle)
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))
        
        # set image to the original image
        self.image = self.original_image
        self.image.set_colorkey(self.colorkey)
        self.image.convert_alpha()

        self.rect = self.image.get_rect(center=self.pos)

    # preforms all necessary transformations on this sprite after updating but before drawing
    def transform(self):
        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos
