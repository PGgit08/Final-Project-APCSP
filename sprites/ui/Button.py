from sprites.ui.text import Text
import pygame

class Button(Text):
    mouse_clicked = False
    onclick = None

    def __init__(self, src, text, font, color, size, pos, onclick, bold=False):
        super().__init__(text, font, color, size, pos, bold=bold)

        self.image_src = src

        self.onclick = onclick

        # to draw
        self.resize_text()

        self.width += 40
        self.height += 10
        
        self.load_surface()
        self.blit_text()
    

    def update(self):
        mouse = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if  self.rect.collidepoint(mouse_pos) and self.mouse_clicked and mouse[0]:
            pass
    
        elif self.rect.collidepoint(mouse_pos) and not self.mouse_clicked and mouse[0]:
            self.onclick()
            self.mouse_clicked = True

        else:
            self.mouse_clicked = False


        # to draw
        self.resize_text()

        self.width += 40
        self.height += 10
        
        self.load_surface()
        self.blit_text()

        self.transform()
