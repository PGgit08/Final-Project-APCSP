import pygame
from sprites.base_sprite import BaseSprite
from globals import globals

class Text(BaseSprite):
    text = None

    def __init__(self, text):
        super().__init__(globals.uis)

        self.text = text

        self.load_surface(width=10, height=10)

