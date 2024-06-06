import pygame
import os
import math
from globals import enemies, enemy_bullets, players, player_bullets, game_cam, healths
from .bullet import Bullet
from timer import Timer
from sprites.healthbar import Health
import random

class Enemy(pygame.sprite.Sprite):
    pos = pygame.Vector2(0, 0)

    angle = 0
    old_angle = 0

    health = 40
    max_health = 40

    speed = 0.15

    timer = Timer()

    def __init__(self):
        super().__init__(enemies)

        self.image = pygame.image.load(os.getcwd() + "/assets/temp_player.png")

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.scale(self.image, (100, 150))
        
        # reset image to the original image
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.Surface.convert_alpha(self.image)

        self.rect = self.image.get_rect(center=self.pos)

        h = Health(self)
        healths.append(h)

        self.timer.reset()

    def create_bullet(self):
        Bullet(self.angle + random.randint(-30, 30), pygame.Vector2(self.pos.x, self.pos.y), enemy_bullets)

    def update(self):
        distance_from_player = players.sprites()[0].pos.distance_to(self.pos)
        
        if not(distance_from_player < 180): # Move towards player
            pass 

        if pygame.sprite.spritecollide(self, player_bullets, True):
            self.health -= 12
            if (self.health <= 0):
                self.kill()

        if self.timer.has_elapsed(2):
            self.create_bullet()
            self.timer.reset()

        if (players.sprites()[0]):
            mx, my = players.sprites()[0].pos
            dx, dy = mx - self.rect.centerx, my - self.rect.centery
            self.angle = (math.degrees(math.atan2(-dy, dx)) - 90) 

        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos
