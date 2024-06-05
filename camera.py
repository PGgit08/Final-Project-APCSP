import pygame

class Camera:
    def __init__(self, width, height, target=None):
        self.width = width
        self.height = height
        self.target = target

    def apply(self, moved):
        # moved.rect.center = (
        #     moved.rect.x - (self.target.rect.centerx - int(self.width / 2)),
        #     moved.rect.y - (self.target.rect.centery - int(self.height / 2))
        # )
        pass