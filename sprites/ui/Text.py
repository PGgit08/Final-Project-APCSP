import pygame
from sprites.base_sprite import BaseSprite
from globals import globals

class Text(BaseSprite):
    def __init__(self, text, font, color, size, pos, bold=False, bg_color=(255, 255, 255)):
        super().__init__(globals.uis)

        self.text = text
        self.font = font
        self.color = color
        self.bold = bold
        self.bg_color = bg_color
        self.size = size
        self.pos = pos
        
        self.textSurf = None
        self.textW = None
        self.textH = None

        self.smallest = True

        # to draw
        self.update_surface()
        self.load_surface(color=self.bg_color)
        self.blit_text()

    # updates this sprite's surface with any text changes
    def update_surface(self):
        self.textSurf = pygame.font.SysFont(self.font, self.size, bold=self.bold).render(self.text, True, self.color)
        
        self.textW = self.textSurf.get_width()
        self.textH = self.textSurf.get_height()

    # to blit text in the correct location
    def blit_text(self):
        if self.smallest:
            self.width = self.textW
            self.height = self.textH
        
        self.image.blit(
            self.textSurf,
            ((self.width - self.textW) / 2, (self.height - self.textH) / 2)
        )

    def update(self):
        # to draw
        self.update_surface()
        self.load_surface(color=self.bg_color)
        self.blit_text()

        self.transform()
