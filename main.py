import pygame

pygame.init()

import os
from sprites.player import Player
from sprites.enemy import Enemy
from sprites.background import Background
from sprites.pickup import Pickup
from globals import globals
import random
from timer import Timer

game_display = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
game_map = pygame.Surface((globals.MAP_WIDTH, globals.MAP_HEIGHT))

cursor_image = pygame.image.load(os.getcwd() + "/assets/crosshair.png")
cursor_image =  pygame.transform.scale(cursor_image, (42.5, 22.5))
cursor_image.set_colorkey((255, 255, 255))

pygame.display.set_caption("Untitled Shooter Game")

high_score = int(open("high_score.txt", "r").readlines()[0])

dead = False

# to update all sprites
def update_sprites():
    globals.backgrounds.update()
    globals.players.update()
    globals.enemies.update()
    globals.player_bullets.update()
    globals.enemy_bullets.update()
    globals.pickups.update()

# to draw all sprites
def draw_sprites():
    globals.backgrounds.draw(game_map)
    globals.players.draw(game_map)
    globals.enemies.draw(game_map)
    globals.player_bullets.draw(game_map)
    globals.enemy_bullets.draw(game_map)
    globals.pickups.draw(game_map)
    
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

# create all timers
enemy_spawner = Timer()
enemy_spawner.lock()
enemy_countdown = 5

health_spawner = Timer()
health_spawner.lock()
health_countdown = 15 - (globals.PLAYER_MAX_HEALTH / p.health)

gun_spawner = Timer()
gun_spawner.lock()
gun_countdown = random.randint(10, 25)

pygame.mouse.set_visible(False)

globals.messages.game_status = "Welcome to (name)! WASD to move, left click to shoot. Please select level (click 1 for easy, 2 for medium, 3 for hard)."

level = None

while not (dead):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                dead = True
            if level == None:
                if event.key == pygame.K_1:
                    level = 1
                if event.key == pygame.K_2:
                    level = 2
                if event.key == pygame.K_3:
                    level = 3

    # main player life status
    if not p.alive():
        level = None
        globals.messages.warning = ""
        globals.messages.game_status = "YOU DIED GAME OVER!"
        enemy_spawner.lock()

    # update all sprites
    if level != None:
        enemy_spawner.unlock()
        health_spawner.unlock()
        gun_spawner.unlock()

        # enemy spawning
        if (enemy_spawner.has_elapsed(enemy_countdown)):
            Enemy(pygame.Vector2(
                random.randint(0, globals.MAP_WIDTH),
                random.randint(0, globals.MAP_HEIGHT)
            ))

            enemy_countdown = 5
            enemy_spawner.reset()

        # medkit spawning
        if (health_spawner.has_elapsed(health_countdown)):
            health_countdown = 15 - (globals.PLAYER_MAX_HEALTH / p.health)
            
            Pickup("/assets/pickups/medkit.png", "health", pygame.Vector2(
                random.randint(0, globals.MAP_WIDTH),
                random.randint(0, globals.MAP_HEIGHT)
            ), 100, 100, colorkey=(0, 255, 0))

            health_countdown = 15 - (globals.PLAYER_MAX_HEALTH / p.health)
            health_spawner.reset()

        # gun spawning
        if (gun_spawner.has_elapsed(gun_countdown)):
            gun_countdown = random.randint(10, 25)
            gun_type = random.choice(["pistol", "shotgun"])

            Pickup("/assets/pickups/" + gun_type + ".png", gun_type, pygame.Vector2(
                random.randint(0, globals.MAP_WIDTH),
                random.randint(0, globals.MAP_HEIGHT)
            ), 100, 100)

            gun_countdown = random.randint(10, 25)
            gun_spawner.reset()

        globals.messages.game_status = ""

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
    globals.messages.score = "Score: " + str(globals.score) + ", High Score: " + str(high_score) + ", Level: " + str(level)
    globals.messages.draw(game_display)

    pygame.display.flip()

if globals.score > high_score:
    open("high_score.txt", "w").close()
    open("high_score.txt", "w").write(str(globals.score))
