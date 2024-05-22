class Board:
    def __init__(self):
        self.user = []

    def check(self, coreCard, playerCard):
        return coreCard.color == playerCard.color or coreCard.shape == playerCard.shape and playerCard.shape is not None

    def skipCheck(self, coreCard, playerCard):
        if coreCard.color == playerCard.color and playerCard.specialType == 0 and playerCard.shape is None:
            return True
        elif coreCard.specialType == 0 and playerCard.specialType == 0:
            return True

    def plusTwo(self, middleCard, userOne):
        if middleCard.color == userOne.color and userOne.specialType == 1 and userOne.shape is None:
            return True
        elif middleCard.specialType == 1 and userOne.specialType == 1:
            return True
