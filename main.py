import pygame
from sprites.player import Player
from sprites.enemy import Enemy
from globals import *

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Untitled Shooter Game")

dead = False

def update_sprites():
    players.update()
    enemies.update()
    player_bullets.update()
    enemy_bullets.update()

def draw_sprites():
    players.draw(game_display)
    enemies.draw(game_display)
    player_bullets.draw(game_display)
    enemy_bullets.draw(game_display)

## SETUP CODE
p = Player()
e = Enemy()
e.pos.x = 100
e.pos.y = 100

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

    if len(player_bullets.sprites()) > 0 or len(enemy_bullets.sprites()) > 0:
        print("BULLET(S) EXIST")
    else:
        print("NO BULLET(S)")

    update_sprites()
    game_display.fill((0, 0, 0))
    draw_sprites()
    pygame.display.flip()