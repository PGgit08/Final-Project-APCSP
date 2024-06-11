import pygame
import os
import math
from globals import globals
from .bullet import Bullet
from sprites.healthbar import Health
from timer import Timer

class Player(pygame.sprite.Sprite):
    pos = pygame.Vector2(0, 0)

    angle = 0
    old_angle = 0

    speed = 0.8

    health = 100
    max_health = 100

    timer = Timer()

    mouse_clicked = False

    gun = "pistol"

    original_image = None

    def __init__(self):
        super().__init__(globals.players)

        self.change_gun(self.gun)

        # create healthbar for this player
        h = Health(self)
        globals.healths.append(h)

        self.timer.reset()

    # creates a new bullet
    def create_bullet(self):
        if self.mouse_clicked:
            return

        Bullet(self.angle, pygame.Vector2(self.pos.x, self.pos.y), globals.player_bullets)

    # change the image for the player
    def change_image(self, image_path):
        self.image = pygame.image.load(os.getcwd() + image_path)

        # original image is a scaled down non-rotated image of the player
        self.original_image = pygame.transform.scale(self.image, (100, 150))
        self.original_image = pygame.transform.rotate(self.original_image, 180)
        
        # set image to the original image
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.Surface.convert_alpha(self.image)

        self.rect = self.image.get_rect(center=self.pos)

    # change the gun for the player
    def change_gun(self, gun):
        self.gun = gun

        if self.gun == "pistol":
            self.change_image("/assets/pistol_player.png")
        if self.gun == "shotgun":
            self.change_image("/assets/shotgun_player.png")

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

        if self.old_angle != self.angle:
            self.old_angle = self.angle

            # transform original image to correct rotation
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.center = self.pos
