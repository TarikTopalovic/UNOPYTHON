import random
from Button import Button
import pygame
from ImageDeCoder import ImageDeCoder


class Cards:
    def __init__(self, canBeSpecial):
        self.isSpecial = canBeSpecial
        self.color = None
        self.shape = None
        self.specialType = None
        self.randomizer()
        self.image = None

    def randomizer(self):
        self.color = random.randint(1, 4)
        self.shape = random.randint(1, 4)

        if self.isSpecial:
            if random.randint(1, 100) < 25:
                self.specialType = random.randint(0, 1)
                self.shape = None

    def getCardCode(self):
        if self.specialType == 1 or self.specialType == 0:
            return f'{self.color}0{self.specialType}'
        else:
            return f'{self.color}{self.shape}0'


    def ButtonMaker(self, surface):
        self.image = pygame.image.load(ImageDeCoder[self.getCardCode()])
        Button.draw(Button(870, 300, self.image, 0.32), surface)


