import pygame

class Messages:
    # any game warnings are in this variable
    warning = ""

    # the game score is in this variable
    score = ""

    # the game status (welcome / game over) is in this variable
    game_status = ""

    def __init__(self, swidth, sheight):
        self.font = pygame.font.SysFont('Impact', 36)

        self.swidth = swidth
        self.sheight = sheight

    # draws all display messages
    def draw(self, surface):
        if self.warning != "":
            warning_text = self.font.render(self.warning, True, (247, 244, 47))
            warning_text_mask = self.font.render(self.warning, True, (0, 0, 0))
            surface.blit(warning_text_mask, (self.swidth // 2 - 220, self.sheight // 2 + 100))
            surface.blit(warning_text, (self.swidth // 2 - 217, self.sheight // 2 + 102))
        
        if self.score != "":
            score_text = self.font.render(self.score, True, (0, 240, 0))
            surface.blit(score_text, (self.swidth - 500, 10))

        if self.game_status != "":
            game_status_text = self.font.render(self.game_status, True, (0, 200, 0))
            surface.blit(game_status_text, (self.swidth // 2 - 200, self.sheight // 2 + 70))
