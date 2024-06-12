import pygame
import os
import math
from globals import globals
from .bullet import Bullet
from .base_sprite import BaseSprite
from sprites.healthbar import Health
import random

class Player(BaseSprite):
    speed = 0.8

    health = 100
    max_health = globals.PLAYER_MAX_HEALTH
    
    mouse_clicked = False

    gun = None

    bullets = 0

    def __init__(self):
        super().__init__(globals.players)

        self.offset_angle = 180

        self.change_gun("pistol")

        # create healthbar for this player
        h = Health(self)
        globals.healths.append(h)

    # creates a new bullet
    def create_bullet(self):
        if self.mouse_clicked or self.bullets <= 0:
            return
        
        self.bullets -= 1

        globals.shoot_sound.play()

        if self.gun == "pistol":
            Bullet(self.angle, pygame.Vector2(self.pos.x, self.pos.y), self.gun, globals.player_bullets)
            
        elif self.gun == "shotgun":
            for i in range(5):
                offset = random.randint(-25, 25)
                Bullet(self.angle + offset, pygame.Vector2(self.pos.x, self.pos.y), self.gun, globals.player_bullets)
                   

    # change the gun for the player
    def change_gun(self, gun):
        self.gun = gun

        if self.gun == "pistol":
            self.height = 150
            self.speed = 0.80
            self.bullets = 15
            self.image_src = "/assets/players/pistol_player.png"

        if self.gun == "shotgun":
            self.height = 190
            self.speed = 0.60
            self.bullets = 8
            self.image_src = "/assets/players/shotgun_player.png"
        
        self.load_surface()

    # when the player picks up a pickup
    def picked_up(self, t):
        if t == "coin":
            globals.score += 1 * globals.level

        if t == "health":
            self.health += 15

            if self.health > self.max_health:
                self.health = self.max_health

        if t == "shotgun":
            self.change_gun("shotgun")
        
        if t == "pistol":
            self.change_gun("pistol")


    def update(self):
        ## health damage code
        hit_bullets = list(map(lambda b: b.type, pygame.sprite.spritecollide(self, globals.enemy_bullets, True)))

        if hit_bullets: # Takes damage from bullet
            globals.damage_sound.play()

            if "pistol" in hit_bullets: self.health -= 10 
            else: self.health -= 5
        
        if (self.health <= 0):
            self.kill()

        if not globals.map_rect.collidepoint(self.pos.x, self.pos.y):
            self.health -= 0.1
            globals.messages.warning = "GET BACK INTO THE MAP!"
        
        else:
            globals.messages.warning = ""

        ## input code
        keys = pygame.key.get_pressed() 
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_w]:
            self.pos.y -= self.speed
        if keys[pygame.K_s]:
            self.pos.y += self.speed
        if keys[pygame.K_a]:
            self.pos.x -= self.speed
        if keys[pygame.K_d]:
            self.pos.x += self.speed

        if mouse[0]:
            self.create_bullet()
            self.mouse_clicked = True

        else:
            self.mouse_clicked = False

        ## look at mouse
        mx, my = globals.mouse_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx)) - 90

        self.transform()
