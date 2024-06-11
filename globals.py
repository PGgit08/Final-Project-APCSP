import pygame
from camera import Camera
from messages import Messages

# all global variables are in this class
class globals:
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
    pickups = pygame.sprite.Group()
    healths = []

    # max healths
    PLAYER_MAX_HEALTH = 100
    ENEMY_MAX_HEALTH = 40

    # the amount of enemies killed
    score = 0

    # display message system and camera
    messages = Messages(WIDTH, HEIGHT)
    game_cam = Camera(WIDTH, HEIGHT)

    # a rect the size of the game map for collision and etc
    map_rect = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)

    @staticmethod
    # get the mouse position after camera transformations
    def mouse_pos() -> pygame.Vector2:
        return pygame.mouse.get_pos() + -globals.game_cam.offsets()

    @staticmethod
    # returns the closest entity in a group to a target entity 
    def closest(e, targets: pygame.sprite.Group):
        pos = e.pos

        if (len(targets.sprites()) <= 0):
            return None

        closest = min([t for t in targets.sprites()], key=lambda t: pos.distance_to(t.pos))

        return closest
