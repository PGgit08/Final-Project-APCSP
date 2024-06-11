import pygame
import os
import math
from globals import globals
from .bullet import Bullet
from timer import Timer
from sprites.healthbar import Health
import random
from .pickup import Pickup
from .base_sprite import BaseSprite

class Enemy(BaseSprite):
    health = 40
    max_health = globals.ENEMY_MAX_HEALTH

    speed = 0.15

    def __init__(self, pos):
        super().__init__(globals.enemies)

        self.pos = pos

        self.width = 100
        self.height = 150
        self.offset_angle = 180

        self.change_image("/assets/enemies/pistol_enemy.png")

        # create health bar for this enemy
        h = Health(self)
        globals.healths.append(h)

        self.timer = Timer()
        self.timer.reset()

    def create_bullet(self):
        Bullet(self.angle + random.randint(-30, 30), pygame.Vector2(self.pos.x, self.pos.y), globals.enemy_bullets)

    def update(self):
        ## health damage code
        if pygame.sprite.spritecollide(self, globals.player_bullets, True):
            self.health -= 12
        
        if (self.health <= 0):
            self.kill()
            coin_pos = pygame.Vector2(self.pos.x, self.pos.y)
            Pickup("/assets/pickups/coin.png", "coin", coin_pos, 100, 100)

        ## find target player
        target = globals.closest(self, globals.players)

        if (target):
            distance_from_player = target.pos.distance_to(self.pos)
            
            if not(distance_from_player < 250): # Move towards player
                direction_vector = (target.pos - self.pos).normalize()
                self.pos += direction_vector * 0.25

            mx, my = target.pos
            dx, dy = mx - self.rect.centerx, my - self.rect.centery
            self.angle = (math.degrees(math.atan2(-dy, dx)) - 90) 

            if self.timer.has_elapsed(1) and distance_from_player < 300:
                self.create_bullet()
                self.timer.reset()

        else:
            self.angle += random.randint(0, 1)

        self.transform()
