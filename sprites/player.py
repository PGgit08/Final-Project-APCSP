import pygame
import os
import math
from globals import players, player_bullets, enemy_bullets, game_cam, healths
from .bullet import Bullet
from sprites.healthbar import Health

class Player(pygame.sprite.Sprite):
    pos = pygame.Vector2(0, 0)

    angle = 0
    old_angle = 0

    speed = 0.15

    health = 100
    max_health = 100

    def __init__(self):
        super().__init__(players)

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


    def create_bullet(self):
        Bullet(self.angle, pygame.Vector2(self.pos.x, self.pos.y), player_bullets)

    def update(self):
        if pygame.sprite.spritecollide(self, enemy_bullets, True):
            self.health -= 10
            if (self.health <= 0):
                self.kill()
                
            pass

        keys = pygame.key.get_pressed() 

        if keys[pygame.K_w]:
            self.pos.y -= self.speed
        if keys[pygame.K_s]:
            self.pos.y += self.speed
        if keys[pygame.K_a]:
            self.pos.x -= self.speed
        if keys[pygame.K_d]:
            self.pos.x += self.speed       

        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx)) - 90

        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos

        game_cam.apply(self)
