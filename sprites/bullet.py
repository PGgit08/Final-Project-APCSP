import pygame
import os
from globals import globals
from .base_sprite import BaseSprite

class Bullet(BaseSprite):
    type = None

    # direction vector of this bullet (velocity)
    def get_direction(self) -> pygame.Vector2:
        return pygame.Vector2(0, 1).rotate(self.angle)

    def __init__(self, angle, pos, type, group):
        super().__init__(group)

        self.type = type

        self.pos = pos
        self.angle = angle

        self.width = 15
        self.height = 30

        self.offset_angle = 90

        self.image_src = "/assets/bullet.png"
        self.load_surface()

    def update(self):
        # constant movement by direction vector code
        vel = self.get_direction().normalize() * 10
        
        self.pos.x += vel.x
        self.pos.y += -vel.y

        # health damage code
        if not globals.map_rect.collidepoint(self.pos.x, self.pos.y):
            self.kill()

        self.transform()

