import pygame
from sprites.base_sprite import BaseSprite
from globals import globals

class Text(BaseSprite):
    # text properties
    text = None
    font = None
    color = None
    bold = None
    size = None
    bg_color = None

    # pygame text surface
    textSurf = None

    def __init__(self, text, font, color, size, pos, bold=False, bg_color=(255, 255, 255)):
        super().__init__(globals.uis)

        self.text = text
        self.font = font
        self.color = color
        self.bold = bold
        self.bg_color = bg_color
        self.size = size
        self.pos = pos

        self.draw_text()

    def draw_text(self):
        textSurf = pygame.font.SysFont(self.font, self.size, bold=self.bold).render(self.text, True, self.color)

        textW = textSurf.get_width()
        textH = textSurf.get_height()

        self.width = textW
        self.height = textH

        self.load_surface(color=self.bg_color)

        self.image.blit(textSurf, (0, 0))

    def update(self):
        self.draw_text()

        self.transform()
