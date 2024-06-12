import pygame
from sprites.base_sprite import BaseSprite
from globals import globals

class Image(BaseSprite):
    def __init__(self, source, pos, width, height, alpha=255, bg_color=(255, 255, 255), colorkey=(255, 255, 255)):
        super().__init__(globals.uis)

        self.image_src = source

        self.width = width
        self.height = height

        self.pos = pos

        self.colorkey = colorkey

        self.load_surface(color=bg_color)

        self.image.set_alpha(alpha)

    def update(self):
        self.transform()
