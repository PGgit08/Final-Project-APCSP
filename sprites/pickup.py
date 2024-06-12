import pygame
import os
import math
from globals import globals
from .bullet import Bullet
from .base_sprite import BaseSprite
from timer import Timer
from sprites.healthbar import Health
import random

class Pickup(BaseSprite):
    def __init__(self, image_src, type, pos, width, height, colorkey=(255, 255, 255)):
        super().__init__(globals.pickups)

        self.pos = pos
        self.width = width
        self.height = height
        self.colorkey = colorkey

        self.image_src = image_src
        self.load_surface()

        # type of pickup
        self.type = type


    def update(self):
        ## pickup code
        collided_players = pygame.sprite.spritecollide(self, globals.players, False)
        
        if (len(collided_players) > 0):
            collided_players[0].picked_up(self.type)
            self.kill()
        
        self.transform()
