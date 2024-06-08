import pygame
from camera import Camera
from messages import Messages

# the app's dimensions
WIDTH = 1024
HEIGHT = 576

# the map's dimensions
MAP_WIDTH = WIDTH * 2
MAP_HEIGHT = HEIGHT * 2

# all sprite groups
backgrounds = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
healths = []

# display message system and camera
messages = Messages()
game_cam = Camera(WIDTH, HEIGHT)

# a rect the size of the game map for collision and etc
map_rect = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)

# get the mouse position after camera transformations
def mouse_pos() -> pygame.Vector2:
    return pygame.mouse.get_pos() + -game_cam.offsets()

# returns the closest entity in a group to a target entity 
def closest(e, targets: pygame.sprite.Group):
    pos = e.pos

    if (len(targets.sprites()) <= 0):
        return None

    closest = min([t for t in targets.sprites()], key=lambda t: pos.distance_to(t.pos))

    return closest
