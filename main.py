import time
import pygame

from Button import Button
from Hand import Hand
from Cards import Cards
from Board import Board
from Writing import Writing

# Initialize Pygame
pygame.init()

# Resolution
windowWidth = 1920
windowHeight = 1080
game_display = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("N10")
clock = pygame.time.Clock()

# Player Hands
playerOne = Hand()
playerTwo = Hand()
middleCard = Cards(False)

# Loading Images
background = pygame.image.load('images/tempbackground.png')
background2 = pygame.image.load('images/background without card.png')
play_image = pygame.image.load('images/button.png')
hide_image = pygame.image.load('images/hideicon.png')
addOne = pygame.image.load('images/UnoCardBack.png')
skipImage = pygame.image.load('images/skip.png')
rulesIcon = pygame.image.load('images/rules.png')
rulesBackground = pygame.image.load('images/rulesbackground.png')
play_image2 = pygame.image.load('images/button.png')
playerTwo.imageloader()
playerOne.imageloader()


# Creating Buttons
startButton = Button(520, 800, play_image, 0.7)
startButton2 = Button(775, 800, play_image2, 0.7)
HideButton = Button(1800, 100, hide_image, 1)

plusOne = Button(100, 100, addOne, 0.3)
skipButton = Button(1800, 250, skipImage, 0.45)
rulesButton = Button(1075, 800, rulesIcon, 0.7)
playerOne.buttonCreator(690)
playerTwo.buttonCreator(690)

# Initializing Variables
CardPlayed = False
CardPlayed2 = False
showRules = False
middleCard.ButtonMaker(game_display)
buttonVisibility = True
HideCards = False
turn = 1

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if startButton.draw(game_display) or startButton2.draw(game_display):
                buttonVisibility = False
            if rulesButton.draw(game_display):
                showRules = True
            if HideButton.draw(game_display):
                HideCards = not HideCards
            if plusOne.draw(game_display):
                if turn == 1:
                    playerOne.cardAddition(1)
                else:
                    playerTwo.cardAddition(1)

            if turn == 1 and skipButton.draw(game_display):
                turn = 2
                HideCards = False
            elif turn == 2 and skipButton.draw(game_display):
                turn = 1
                HideCards = False

    # Draw
    game_display.blit(background, (0, 0))
    if buttonVisibility:
        startButton.draw(game_display)
        rulesButton.draw(game_display)
        if showRules:
            game_display.blit(rulesBackground, (0, 0))
            startButton2.draw(game_display)
    else:
        # In Game Buttons
        game_display.blit(background2, (0, 0))
        HideButton.draw(game_display)
        middleCard.ButtonMaker(game_display)
        plusOne.draw(game_display)
        skipButton.draw(game_display)
        if turn == 1:
            Writing().prepText('PlayerOne', (255, 255, 255), 835, 100, game_display)
        elif turn == 2:
            Writing().prepText('PlayerTwo', (255, 255, 255), 835, 100, game_display)

        if HideCards:
            if turn == 1:
                indexPlayerOne = playerOne.buttonDrawer(game_display)
                try:
                    if Board().skipCheck(middleCard, playerOne.getCards()[indexPlayerOne]):
                        middleCard = playerOne.getCards()[indexPlayerOne]
                        middleCard.ButtonMaker(game_display)
                        playerOne.removeCard(indexPlayerOne)

                    elif Board().plusTwo(middleCard, playerOne.getCards()[indexPlayerOne]):
                        middleCard = playerOne.getCards()[indexPlayerOne]
                        middleCard.ButtonMaker(game_display)
                        playerOne.removeCard(indexPlayerOne)
                        playerTwo.cardAddition(2)
                        CardPlayed = True
                        turn += 1

                    elif Board().check(middleCard, playerOne.getCards()[indexPlayerOne]):
                        middleCard = playerOne.getCards()[indexPlayerOne]
                        middleCard.ButtonMaker(game_display)
                        playerOne.removeCard(indexPlayerOne)

                        CardPlayed = True
                        turn += 1

                    #time.sleep(0.10)
                    CardsPlayed2 = False
                    HideCards = False if CardPlayed else True
                except Exception as e:
                    if e.args[0] is None:
                        print("Exception occurred with a None message.")
                    else:
                        print(f"An error occurred: {e}")

            elif turn == 2:
                indexPlayerTwo = playerTwo.buttonDrawer(game_display)
                try:
                    userTwoCurrent = playerTwo.getCards()[indexPlayerTwo]

                    if Board().skipCheck(middleCard, userTwoCurrent):
                        middleCard = userTwoCurrent
                        middleCard.ButtonMaker(game_display)
                        playerTwo.removeCard(indexPlayerTwo)

                    elif Board().plusTwo(middleCard, userTwoCurrent):
                        middleCard = userTwoCurrent
                        middleCard.ButtonMaker(game_display)
                        playerTwo.removeCard(indexPlayerTwo)

                        playerOne.cardAddition(2)
                        CardPlayed2 = True
                        turn -= 1

                    elif Board().check(middleCard, userTwoCurrent):
                        middleCard = userTwoCurrent

                        middleCard.ButtonMaker(game_display)
                        playerTwo.removeCard(indexPlayerTwo)
                        CardPlayed2 = True
                        turn -= 1

                    #time.sleep(0.10)
                    HideCards = False if CardPlayed2 else True
                    CardPlayed = False
                except Exception as e:
                    if e.args[0] is None:
                        print("Exception occurred with a None message.")
                    else:
                        print(f"An error occurred: {e}")
    pygame.display.update()
