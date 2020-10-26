import pygame, pygame.surface, os, pygame.font
from needs.Text import Text
from needs.Button import Button
from StoryStart import StoryStart

# comment this thing below
from doNotUploadThis import absolutePath

# change absolutePath into os.getcwd()
icon = pygame.image.load(absolutePath + '/images/basic-stuff/icon.png')

class MainWindow:
    def __init__(self):
        self.backgroundSize = (800, 600)
        self.backgroundColor = (0, 0, 0)
        self.title = "Codename TR"
        self.startButtonX = 350
        self.startButtonY = 300

        # Initialize pygame
        pygame.init()

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
            
            pygame.display.set_icon(icon)
            pygame.display.set_caption(self.title)

            # background
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill(self.backgroundColor)

            # print title
            titleText = Text(screen, "Codename Tr", (225, 150), 72)

            screen.blit(background, (0, 0))

            # blit text
            titleText.blitText()


            # initiate button
            # hover mouse detector
            if self.startButtonX + 100 > mouse[0] > self.startButtonX and self.startButtonY + 50 > mouse[1] > self.startButtonY:
                startButton = Button(screen, "Are you sure?", (0, 150, 0), self.startButtonX, self.startButtonY, 100, 50, 8, 20, 20)
                startButton.drawButton()

                # click detector
                if click[0] == 1:
                    running = False
                    storyStart = StoryStart()

                elif click[2] == 1:
                    print('you right clicked the start button')
            else:
                startButton = Button(screen, "Start", (0, 255, 0), self.startButtonX, self.startButtonY, 100, 50, 35, 20, 20)
                startButton.drawButton()

            pygame.display.flip()
            
            pygame.display.update()
                


if __name__=="__main__":
    start = MainWindow()
