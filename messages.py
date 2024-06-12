import pygame

class Messages:
    # any game warnings are in this variable
    warning = ""

    # the game score is in this variable
    score = ""

    # the game status (welcome / game over) is in this variable
    game_status = ""

    def __init__(self, swidth, sheight):
        self.big_font = pygame.font.SysFont('Impact', 36)
        self.small_font = pygame.font.SysFont('Impact', 21)

        self.swidth = swidth
        self.sheight = sheight

    # creates a text to render
    def render_text(self, text, color):
        if len(text) > 100:
            return self.small_font.render(text, True, color)

        return self.big_font.render(text, True, color)

    # draws all display messages
    def draw(self, surface):
        if self.warning != "":
            warning_text = self.render_text(self.warning, (247, 244, 47))
            warning_text_mask = self.render_text(self.warning, (0, 0, 0))
            surface.blit(warning_text_mask, (self.swidth // 2 - 220, self.sheight // 2 + 100))
            surface.blit(warning_text, (self.swidth // 2 - 217, self.sheight // 2 + 102))
        
        if self.score != "":
            score_text = self.render_text(self.score, (0, 240, 0))
            surface.blit(score_text, (self.swidth - 700, 10))

        if self.game_status != "":
            game_status_text = self.render_text(self.game_status, (0, 0, 0))
            surface.blit(game_status_text, (10, self.sheight // 2 + 70))
