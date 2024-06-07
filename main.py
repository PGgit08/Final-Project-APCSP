import os
import pygame
from sprites.player import Player
from sprites.enemy import Enemy
from sprites.background import Background
from globals import *
import random
from timer import Timer

pygame.init()

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
game_map = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))

hud_font = pygame.font.SysFont('Impact', 36)

cursor_image = pygame.image.load(os.getcwd() + "/assets/crosshair.png")
cursor_image =  pygame.transform.scale(cursor_image, (42.5, 22.5))
cursor_image.set_colorkey((255, 255, 255))

pygame.display.set_caption("Untitled Shooter Game")

dead = False

def update_sprites():
    backgrounds.update()
    players.update()
    enemies.update()
    player_bullets.update()
    enemy_bullets.update()

def draw_sprites():
    backgrounds.draw(game_map)
    players.draw(game_map)
    enemies.draw(game_map)
    player_bullets.draw(game_map)
    enemy_bullets.draw(game_map)
    
    for i in healths:
        i.draw(game_map)

## SETUP CODE
p = Player()

for i in range(MAP_WIDTH // WIDTH):
    for j in range(MAP_HEIGHT // HEIGHT):
        Background(((i * WIDTH) + (WIDTH / 2), (j * HEIGHT) + (HEIGHT / 2)))

game_cam.target = p

pygame.mouse.set_visible(False)

enemy_spawner = Timer()

while not (dead):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                dead = True

    if (enemy_spawner.has_elapsed(0.1)):
        e = Enemy()
        e.pos = pygame.Vector2(
            random.randint(0, MAP_WIDTH),
            random.randint(0, MAP_HEIGHT)
        )

        enemy_spawner.reset()

    update_sprites()

    game_map.fill((0, 0, 0))
    draw_sprites()

    cam_offsets = game_cam.offsets()

    game_display.fill((128, 128, 128))
    game_display.blit(game_map, cam_offsets)

    cursor_rect = cursor_image.get_rect()
    cursor_rect.center = pygame.mouse.get_pos()
    game_display.blit(cursor_image, cursor_rect)

    text = hud_font.render(messages.display_message, True, (247, 244, 47))
    text_mask = hud_font.render(messages.display_message, True, (0, 0, 0))
    
    game_display.blit(text_mask, (WIDTH // 2 - 197, HEIGHT // 2 + 100))
    game_display.blit(text, (WIDTH // 2 - 194, HEIGHT // 2 + 102))

    pygame.display.flip()
