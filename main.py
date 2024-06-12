import pygame

pygame.init()
pygame.mixer.init()

import os
from sprites.player import Player
from sprites.enemy import Enemy
from sprites.background import Background
from sprites.pickup import Pickup
from sprites.ui.text import Text
from sprites.ui.image import Image
from globals import globals
import random
from timer import Timer
import json

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
    globals.uis.update()

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
main_player = Player()
globals.game_cam.target = main_player

# create all timers
enemy_spawner = Timer()
enemy_spawner.lock()
enemy_countdown = 5
max_enemies = 1

health_spawner = Timer()
health_spawner.lock()
health_countdown = 3
max_healths = 8

gun_spawner = Timer()
gun_spawner.lock()
gun_countdown = 1
max_guns = 8

status_timer = Timer()
status_timer.lock()

pygame.mouse.set_visible(False)

level_scale = None

score_change = 0
prev_score = 0

# ui stuff
score_text = Text("", "Poppins", (0, 0, 0), 40, pygame.Vector2(850, 30))
bullets_text = Text("", "Poppins", (0, 0, 0), 40, pygame.Vector2(globals.WIDTH - 40, globals.HEIGHT - 50))


Image("/assets/bullets.png", pygame.Vector2(globals.WIDTH - 35, globals.HEIGHT - 50), 62.5, 97.5)

while not (dead):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                dead = True
            if globals.level == None:
                if event.key == pygame.K_1:
                    globals.level = 1
                    level_scale = 1.8
                if event.key == pygame.K_2:
                    globals.level = 2
                    level_scale = 2
                if event.key == pygame.K_3:
                    globals.level = 3
                    level_scale = 2.2

    # update ui
    score_text.text = "Score: "+ str(globals.score)
    bullets_text.text = str(main_player.bullets) + "/0"

    # if dead, end the game updating
    if not main_player.alive():
        level = None

        enemy_spawner.lock()
        health_spawner.lock()
        gun_spawner.lock()
        status_timer.lock()

    # print status
    if (status_timer.has_elapsed(5)):
        os.system('cls')

        print(json.dumps({
            "enemy countdown": enemy_countdown,
            "max enemies": max_enemies,
            "gun countdown": gun_countdown,
            "max guns": max_guns,
            "healths countdown": health_countdown,
            "max healths": max_healths,
            "difficulty change": globals.difficulty_change
        }, indent=2), end="\n")

        status_timer.reset()

    # enemy spawning
    if (enemy_spawner.has_elapsed(enemy_countdown) and len(globals.enemies.sprites()) < max_enemies):
        Enemy(pygame.Vector2(
            random.randint(0, globals.MAP_WIDTH),
            random.randint(0, globals.MAP_HEIGHT)
        ), random.choice(["pistol", "shotgun"]))

        score_change = globals.score - prev_score 
        prev_score = globals.score
        enemy_countdown = globals.clamp(enemy_countdown - globals.difficulty_change / 50, 1, 10)
        max_enemies = globals.clamp(round(max_enemies + globals.difficulty_change / 6), 0, 5)

        enemy_spawner.reset()

    # medkit spawning
    if (health_spawner.has_elapsed(health_countdown) and globals.get_pickups_by_type("health") < max_healths):
        Pickup("/assets/pickups/medkit.png", "health", pygame.Vector2(
            random.randint(0, globals.MAP_WIDTH),
            random.randint(0, globals.MAP_HEIGHT)
        ), 100, 100, colorkey=(0, 255, 0))

        health_countdown = globals.clamp(health_countdown + globals.difficulty_change / 50, 1, 10)
        max_healths = globals.clamp(round(max_healths - globals.difficulty_change / 4), 3, 10)

        health_spawner.reset()

    # gun spawning
    if (gun_spawner.has_elapsed(gun_countdown) and (globals.get_pickups_by_type("pistol") + globals.get_pickups_by_type("shotgun")) < max_guns):
        gun = random.choice([
            ["pistol", (100, 50)], ["shotgun", (150, 50)]
        ])

        Pickup("/assets/pickups/" + gun[0] + ".png", gun[0], pygame.Vector2(
            random.randint(0, globals.MAP_WIDTH),
            random.randint(0, globals.MAP_HEIGHT)
        ), *gun[1])

        gun_countdown = globals.clamp(gun_countdown + globals.difficulty_change / 50, 1, 10)
        max_guns = globals.clamp(round(max_guns - globals.difficulty_change / 4), 3, 10)
        gun_spawner.reset()

    # update all sprites
    if globals.level != None:
        enemy_spawner.unlock()
        health_spawner.unlock()
        gun_spawner.unlock()
        status_timer.unlock()

        globals.difficulty_change = level_scale * score_change

        # update all sprites
        update_sprites()

    # clear game map and draw on it
    game_map.fill((0, 0, 0))
    
    # draw all sprites
    draw_sprites()

    # draw game map onto game display based on cam position
    cam_offsets = globals.game_cam.offsets()
    game_display.fill((128, 128, 128))
    game_display.blit(game_map, cam_offsets)

    # draw ui
    globals.uis.draw(game_display)

    # draw cursor
    cursor_rect = cursor_image.get_rect()
    cursor_rect.center = pygame.mouse.get_pos()
    game_display.blit(cursor_image, cursor_rect)

    pygame.display.flip()

if globals.score > high_score:
    open("high_score.txt", "w").close()
    open("high_score.txt", "w").write(str(globals.score))
