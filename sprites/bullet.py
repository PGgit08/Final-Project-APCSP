import pygame
import os
from globals import bound_rect

class Bullet(pygame.sprite.Sprite):
    pos = pygame.Vector2(0, 0)

    angle = 0
    old_angle = 0

    def get_direction(self) -> pygame.Vector2:
        return pygame.Vector2(0, 1).rotate(self.angle)

    def __init__(self, angle, pos, group):
        super().__init__(group)

        self.image = pygame.image.load(os.getcwd() + "/assets/bullet.png")

        self.angle = angle
        self.pos = pos

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.scale(self.image, (100, 100))
        
        # reset image to the original image
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.Surface.convert_alpha(self.image)

        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        vel = self.get_direction().normalize() * 10
        
        self.pos.x += vel.x
        self.pos.y += -vel.y

        if not bound_rect.collidepoint(self.pos.x, self.pos.y):
            self.kill()

        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos

