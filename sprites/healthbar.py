import pygame
from globals import healths


class Health:
    entity: pygame.sprite.Sprite
    
    def __init__(self, entity):
        self.entity = entity

    def draw(self, win):

        if (not self.entity.alive()):
            healths.remove(self)

        if not (self.entity.health < self.entity.max_health):
            return

        pygame.draw.rect(win, "red", (self.entity.pos.x - 45, self.entity.pos.y - 40, 75, 10))
        pygame.draw.rect(win, "green", (self.entity.pos.x - 45, self.entity.pos.y - 40, 75 * (self.entity.health / self.entity.max_health), 10))

        