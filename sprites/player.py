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
    max_health = 100

    mouse_clicked = False

    gun = "pistol"

    def __init__(self):
        super().__init__(globals.players)

        # self.change_gun("pistol")
        self.width = 100
        self.height = 150
        self.offset_angle = 180

        self.change_image("/assets/players/pistol_player.png")

        # create healthbar for this player
        h = Health(self)
        globals.healths.append(h)

    # creates a new bullet
    def create_bullet(self):
        if self.mouse_clicked:
            return

        if self.gun == "pistol":
            print("PISTOL SPAWN")
            Bullet(self.angle, pygame.Vector2(self.pos.x, self.pos.y), globals.player_bullets)
            
        elif self.gun == "shotgun":
            for i in range(5):
                offset = random.randint(-25, 25)
                Bullet(self.angle + offset, pygame.Vector2(self.pos.x, self.pos.y), globals.player_bullets)
                   

    # change the gun for the player
    def change_gun(self, gun):
        self.gun = gun

        if self.gun == "pistol":
            self.change_image("/assets/players/pistol_player.png")
        if self.gun == "shotgun":
            self.change_image("/assets/players/shotgun_player.png")

    # when the player picks up a pickup
    def picked_up(self, t):
        if t == "coin":
            globals.score += 1

        if t == "health":
            self.health += 1

        if t == "shotgun":
            pass
        
        if t == "pistol":
            pass


    def update(self):
        ## health damage code
        if pygame.sprite.spritecollide(self, globals.enemy_bullets, True): # Takes damage from bullet
            self.health -= 10
            pass
        
        if (self.health <= 0):
            print("DIED")
            self.kill()

        if not globals.map_rect.collidepoint(self.pos.x, self.pos.y):
            self.health -= 0.1
            globals.messages.warning = "GET BACK INTO THE MAP! YOUR HEALTH IS: " + str(int(self.health))
        
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
