import pygame
from camera import Camera

# all global variables are in this class
class globals:
    # the app's dimensions
    WIDTH = 1024
    HEIGHT = 576

    # the map's dimensions
    MAP_WIDTH = WIDTH * 2
    MAP_HEIGHT = HEIGHT * 2

    # sounds
    shoot_sound = pygame.mixer.Sound("./assets/sounds/shoot.wav")
    damage_sound = pygame.mixer.Sound("./assets/sounds/damage.wav")
    coin_sound = pygame.mixer.Sound("./assets/sounds/coin_pickup.wav")
    coin_sound.set_volume(0.5)    
    empty_clip_sound = pygame.mixer.Sound("./assets/sounds/empty_gun.wav")

    # trash when reset
    trash = []

    # reset function
    reset = None

    # all sprite groups
    backgrounds = pygame.sprite.Group()
    players = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    pickups = pygame.sprite.Group()
    uis = pygame.sprite.Group()
    healths = []

    # max healths
    PLAYER_MAX_HEALTH = 100

    # the amount of enemies killed
    score = 0
    high_score = 0

    # game camera (which will follow player)
    game_cam = Camera(WIDTH, HEIGHT)

    # difficulty
    level = None
    level_scale = None

    # a rect the size of the game map for collision and etc
    map_rect = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)

    # the difficulty the game is currently at [1, 10]
    difficulty_change = 1

    @staticmethod
    # empties the trash
    def empty_trash():
        for t in globals.trash:
            t.kill()
        
        globals.trash.clear()

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

    @staticmethod
    # returns the amount of pickups by their type
    def get_pickups_by_type(type):
        return len(list(filter(lambda p: p.type == type, globals.pickups.sprites())))

    @staticmethod
    # clamps a value between a lower and upper
    def clamp(val, lower, upper):
        return min(max(lower, val), upper)

