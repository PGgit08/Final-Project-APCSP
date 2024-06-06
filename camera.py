import pygame

class Camera:
    def __init__(self, width, height, target=None):
        self.width = width
        self.height = height
        
        self.target = target