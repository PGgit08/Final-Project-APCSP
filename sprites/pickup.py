import pygame
import os
import math
from globals import globals
from .bullet import Bullet
from timer import Timer
from sprites.healthbar import Health
import random

class Pickup(pygame.sprite.Sprite):
    pos = pygame.Vector2(0, 0)

    angle = 0
    old_angle = 0

    def __init__(self, image_path, type, pos):
        super().__init__(globals.pickups)

        self.pos = pos

        self.image = pygame.image.load(os.getcwd() + image_path)

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.scale(self.image, (100, 150))
        
        # reset image to the original image
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.Surface.convert_alpha(self.image)
        self.rect = self.image.get_rect(center=self.pos)

        # type of pickup
        self.type = type


    def update(self):
        ## pickup code
        collided_players = pygame.sprite.spritecollide(self, globals.players, False)
        
        if (len(collided_players) > 0):
            collided_players[0].picked_up(self.type)
            self.kill()
        
        ## angle code
        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos
