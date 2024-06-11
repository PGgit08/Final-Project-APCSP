from globals import globals
from .base_sprite import BaseSprite

class Background(BaseSprite):
    def __init__(self, pos):
        super().__init__(globals.backgrounds)

        self.change_image("/assets/background.png")
    
    def update(self):
        self.transform()
