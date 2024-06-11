import pygame
import os

# base sprite for all sprites in this game
class BaseSprite(pygame.sprite.Sprite):
    # the sprite's position
    pos = pygame.Vector2(0, 0) 

    # width
    width = 100

    # height
    height = 100

    # colorkey
    colorkey = (255, 255, 255)

    # the sprite's angle
    angle = 0
    old_angle = 0

    # the angle to offset the image by
    offset_angle = 0

    original_image = None

    def __init__(self, group) -> None:
        super().__init__(group)
    
    # change the image for the sprite
    def change_image(self, image_path):
        self.image = pygame.image.load(os.getcwd() + image_path)

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.rotate(self.image, self.offset_angle)
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))
        
        # set image to the original image
        self.image = self.original_image
        self.image.set_colorkey(self.colorkey)
        self.image = pygame.Surface.convert_alpha(self.image)

        self.rect = self.image.get_rect(center=self.pos)

    # preforms all necessary transformations on this sprite after updating but before drawing
    def transform(self):
        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos
