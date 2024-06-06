import os
import pygame
from sprites.player import Player
from sprites.enemy import Enemy
# from sprites.health_bar import HealthBar
from camera import Camera
from globals import *

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(os.getcwd() + "/assets/background.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
cursor_image = pygame.image.load(os.getcwd() + "/assets/crosshair.png")
cursor_image =  pygame.transform.scale(cursor_image, (42.5, 22.5))

pygame.display.set_caption("Untitled Shooter Game")

dead = False

def update_sprites():
    players.update()
    enemies.update()
    player_bullets.update()
    enemy_bullets.update()

    
def draw_sprites():
    game_display.blit(bg, (0,0))
    players.draw(game_display)
    enemies.draw(game_display)
    player_bullets.draw(game_display)
    enemy_bullets.draw(game_display)
    for i in healths:
        i.draw(game_display)

    cursor_rect.center = pygame.mouse.get_pos()
    game_display.blit(cursor_image, cursor_rect)


## SETUP CODE
p = Player()
e = Enemy()
e.pos.x = 100
e.pos.y = 100

game_cam.target = p

pygame.mouse.set_visible(False)
cursor_rect = cursor_image.get_rect()

while not (dead):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                dead = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                p.create_bullet()

    # if len(player_bullets.sprites()) > 0 or len(enemy_bullets.sprites()) > 0:
    #     print("BULLET(S) EXIST")
    # else:
    #     print("NO BULLET(S)")

    # print(            -(game_cam.target.rect.centerx - int(game_cam.width / 2)),
    #        -(game_cam.target.rect.centery - int(game_cam.height / 2)))

    update_sprites()
    game_display.fill((0, 0, 0))

    
    draw_sprites()
    pygame.display.flip()
