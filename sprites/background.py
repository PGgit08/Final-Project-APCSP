from globals import globals
from .base_sprite import BaseSprite

class Background(BaseSprite):
    def __init__(self, pos):
        super().__init__(globals.backgrounds)

        self.pos = pos

        self.width = globals.WIDTH
        self.height = globals.HEIGHT

        self.image_src = "/assets/background.png"

        self.load_surface()
    
    def update(self):
        self.transform()
