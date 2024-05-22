from Cards import Cards
from ImageDeCoder import ImageDeCoder
from Button import Button
import pygame


class Hand:
    def __init__(self):
        self.buttonUpdater = []
        self.deck = []
        self.cardGen(6, True)
        self.loadedImages = []
        self.cardImages = []

    def cardGen(self, num, canBeSpecial):
        for item in range(num):
            self.deck.append(Cards(canBeSpecial))

    def cardAddition(self, num):
        print("Im called chief")
        for item in range(num):
            temp = Cards(True)
            self.deck.append(temp)

            self.cardImages.clear()
            self.loadedImages.clear()

        self.imageloader()
        self.buttonCreator(690)


    def removeCard(self, index):
        self.deck.pop(index)
        self.cardImages.pop(index)
        self.loadedImages.pop(index)

    def getCards(self):
        return self.deck

    def imageloader(self):
        for item in self.deck:
            self.loadedImages.append(pygame.image.load(ImageDeCoder[item.getCardCode()]))

    def centerCards(self):
        width = 1920
        x = (width - (203*len(self.deck)))/2
        return x

    def buttonCreator(self, y):
        x = self.centerCards()
        for item in self.loadedImages:
            self.buttonUpdater.append(self.cardImages.append(Button(x, y, item, 0.27)))
            x += 206

    def buttonDrawer(self, surface):
        for item in range(len(self.cardImages)):
            if self.cardImages[item].draw(surface):
                if item is not None:
                    return item
