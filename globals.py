import pygame
from camera import Camera

WIDTH = 1024
HEIGHT = 576

players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
healths = []

game_cam = Camera(WIDTH, HEIGHT)
