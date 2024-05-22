import pygame


class Writing:
    def __init__(self):
        self.textFont = pygame.font.SysFont('Bauhaus 93', 70)
        self.img = None

    def prepText(self, text, textCol, x, y, screen):
        self.img = self.textFont.render(text, True, textCol)
        screen.blit(self.img, (x, y))
