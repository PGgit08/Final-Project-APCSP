import pygame

class Camera:
    def __init__(self, width, height, target=None):
        self.width = width
        self.height = height

        self.target = target
    
    def offsets(self) -> pygame.Vector2:
        return pygame.Vector2(
            - (self.target.pos.x - self.width / 2),
            - (self.target.pos.y - self.height / 2)
        )