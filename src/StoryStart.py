import pygame, pygame.surface, pygame.font, time
from needs.Text import Text
from needs.Button import Button
from needs.TextSlowPrint import TextSlowPrint

positionText = (0, 0)
counter = 0

class StoryStart:
    def __init__(self):
        self.backgroundSize = (800, 600)
        self.backgroundColor = (0, 0, 0)
        self.title = "Codename TR - Before Start..."
        self.continueX = 700
        self.continueY = 500

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
            firstText = TextSlowPrint(screen, "It's cold...", (225, 150), 72)
            secondText = TextSlowPrint(screen, "No one loves me.", (225, 150), 72)
            thirdText = TextSlowPrint(screen, "I want to die.", (225, 150), 72)

            screen.blit(background, (0, 0))

            # hover mouse detector
            if self.continueX + 100 > mouse[0] > self.continueX and self.continueY + 50 > mouse[1] > self.continueY:
                continueButton = Button(screen, "Next", (0, 150, 0), self.continueX, self.continueY, 100, 50, 8, 20, 20)
                continueButton.drawButton()

                # click detector
                if click[0] == 1:
                    # if counter == 1:
                    #     running = False
                    #     counter+=1
                    #     firstText.blitText()
                        
                    # elif counter == 2:
                    #     running = False
                    #     counter+=1
                    #     secondText.blitText()
                    print('lol')

                elif click[2] == 1:
                    print('you right clicked the start button')
            else:
                continueButton = Button(screen, "Start", (0, 255, 0), self.continueX, self.continueY, 100, 50, 35, 20, 20)
                continueButton.drawButton()


            pygame.display.flip() 
            pygame.display.update()

