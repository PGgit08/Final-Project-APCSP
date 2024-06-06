import pygame
from camera import Camera

WIDTH = 1024
HEIGHT = 576

MAP_WIDTH = WIDTH * 2
MAP_HEIGHT = HEIGHT * 2

backgrounds = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
healths = []

bound_rect = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)

game_cam = Camera(WIDTH, HEIGHT)

def mouse_pos() -> pygame.Vector2:
    return pygame.mouse.get_pos() + -game_cam.offsets()
