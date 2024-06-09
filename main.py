import pygame

pygame.init()

import os
from sprites.player import Player
from sprites.enemy import Enemy
from sprites.background import Background
from globals import globals
import random
from timer import Timer

game_display = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
game_map = pygame.Surface((globals.MAP_WIDTH, globals.MAP_HEIGHT))

cursor_image = pygame.image.load(os.getcwd() + "/assets/crosshair.png")
cursor_image =  pygame.transform.scale(cursor_image, (42.5, 22.5))
cursor_image.set_colorkey((255, 255, 255))

pygame.display.set_caption("Untitled Shooter Game")

dead = False

# to update all sprites
def update_sprites():
    globals.backgrounds.update()
    globals.players.update()
    globals.enemies.update()
    globals.player_bullets.update()
    globals.enemy_bullets.update()

# to draw all sprites
def draw_sprites():
    globals.backgrounds.draw(game_map)
    globals.players.draw(game_map)
    globals.enemies.draw(game_map)
    globals.player_bullets.draw(game_map)
    globals.enemy_bullets.draw(game_map)
    
    for i in globals.healths:
        i.draw(game_map)

## SETUP CODE
for i in range(globals.MAP_WIDTH // globals.WIDTH):
    for j in range(globals.MAP_HEIGHT // globals.HEIGHT):
        # generates 4 backgrounds
        Background(((i * globals.WIDTH) + (globals.WIDTH / 2), (j * globals.HEIGHT) + (globals.HEIGHT / 2)))

# creates this computer's player and attaches the camera to it
p = Player()
globals.game_cam.target = p
enemy_spawner = Timer()
pygame.mouse.set_visible(False)

while not (dead):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                dead = True
    
    # enemy spawning system
    if (enemy_spawner.has_elapsed(5)):
        e = Enemy()
        e.pos = pygame.Vector2(
            random.randint(0, globals.MAP_WIDTH),
            random.randint(0, globals.MAP_HEIGHT)
        )

        enemy_spawner.reset()

    # main player life status
    if not p.alive():
        globals.messages.warning = ""
        globals.messages.game_status = "YOU DIED GAME OVER!"
        globals.enemies.empty()

    # update all sprites
    update_sprites()

    # clear game map and draw on it
    game_map.fill((0, 0, 0))
    draw_sprites()

    # draw game map onto game display based on cam position
    cam_offsets = globals.game_cam.offsets()
    game_display.fill((128, 128, 128))
    game_display.blit(game_map, cam_offsets)

    # draw cursor
    cursor_rect = cursor_image.get_rect()
    cursor_rect.center = pygame.mouse.get_pos()
    game_display.blit(cursor_image, cursor_rect)

    # for display messages
    globals.messages.score = "Score: " + str(globals.score) + ", High Score: " + "(unknown)"
    globals.messages.draw(game_display)

    pygame.display.flip()
