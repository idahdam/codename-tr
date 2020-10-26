import pygame, pygame.surface, pygame.font, time
from needs.Text import Text
from needs.Button import Button
from needs.TextSlowPrint import TextSlowPrint

positionText = (100, 500)

class StoryStart:
    def __init__(self):
        self.backgroundSize = (800, 600)
        self.backgroundColor = (0, 0, 0)
        self.title = "Codename TR - Before Start..."
        self.continueX = 650
        self.continueY = 500

        self.counter = 1

        self.background1 = pygame.image.load('./images/intro-pics/background1.png')
        self.background1 = pygame.transform.scale(self.background1, self.backgroundSize)
        self.background2 = pygame.image.load('./images/intro-pics/background2.png')
        self.background2 = pygame.transform.scale(self.background2, self.backgroundSize)
        self.background3 = pygame.image.load('./images/intro-pics/background3.png')
        self.background3 = pygame.transform.scale(self.background3, self.backgroundSize)
        self.background4 = pygame.image.load('./images/intro-pics/background4.png')
        self.background4 = pygame.transform.scale(self.background4, self.backgroundSize)
        self.background5 = pygame.image.load('./images/intro-pics/background5.png')
        self.background5 = pygame.transform.scale(self.background5, self.backgroundSize)

        self.start()

    def start(self):
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # initiate mouse
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            screen = pygame.display.set_mode(self.backgroundSize)

            pygame.display.set_caption(self.title)

            # background
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill(self.backgroundColor)

            # print texts
            firstText = TextSlowPrint(screen, "It's cold...", positionText, 36)
            secondText = TextSlowPrint(screen, "No one loves me.", positionText, 36)
            thirdText = TextSlowPrint(screen, "I want to die.", positionText, 36)

            screen.blit(background, (0, 0))

            if self.counter == 1:
                screen.blit(self.background1, (0,0))
                firstText.blitText()

            elif self.counter == 2:
                screen.blit(self.background2, (0,0))
                secondText.blitText()

            elif self.counter == 3:
                screen.blit(self.background3, (0,0))
                thirdText.blitText()

            # next hover mouse detector
            if self.continueX + 100 > mouse[0] > self.continueX and self.continueY + 50 > mouse[1] > self.continueY:
                continueButton = Button(screen, "Next", (0, 150, 0), self.continueX, self.continueY, 100, 50, 35, 20, 20)
                continueButton.drawButton()

                # click detector
                if click[0] == 1:
                    print(self.counter)
                    running = False
                    self.counter += 1
                    self.start()

                elif click[2] == 1:
                    print('you right clicked the start button')
            else:
                continueButton = Button(screen, "Next", (0, 255, 0), self.continueX, self.continueY, 100, 50, 35, 20, 20)
                continueButton.drawButton()

            pygame.display.flip() 
            pygame.display.update()

