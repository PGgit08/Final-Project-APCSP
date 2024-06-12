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
    max_health = 40

    speed = 0.15

    gun = None

    def __init__(self, pos, gun="pistol"):
        super().__init__(globals.enemies)

        self.pos = pos

        self.width = 100
        self.offset_angle = 180

        self.gun = gun

        if self.gun == "pistol":
            self.height = 150
            self.speed = 0.4
            self.max_health = 40

            self.change_image("/assets/enemies/pistol_enemy.png")
        
        if self.gun == "shotgun":
            self.height = 180
            self.speed = 0.04
            self.max_health = 120

            self.change_image("/assets/enemies/shotgun_enemy.png")

        self.health = self.max_health

        # create health bar for this enemy
        h = Health(self)
        globals.healths.append(h)

        self.timer = Timer()
        self.timer.reset()

    def create_bullet(self):
        globals.shoot_sound.play()

        if self.gun == "pistol":
            Bullet(self.angle, pygame.Vector2(self.pos.x, self.pos.y), self.gun, globals.enemy_bullets)
            
        elif self.gun == "shotgun":
            for i in range(5):
                offset = random.randint(-25, 25)
                Bullet(self.angle + offset, pygame.Vector2(self.pos.x, self.pos.y), self.gun, globals.enemy_bullets)

    def update(self):
        ## health damage code
        hit_bullets = list(map(lambda b: b.type, pygame.sprite.spritecollide(self, globals.player_bullets, True)))
        
        if hit_bullets: # Takes damage from bullet
            if "pistol" in hit_bullets: self.health -= 12
            else: self.health -= 6
        
        if (self.health <= 0):
            self.kill()
            coin_pos = pygame.Vector2(self.pos.x, self.pos.y)
            Pickup("/assets/pickups/coin.png", "coin", coin_pos, 40, 40)

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
