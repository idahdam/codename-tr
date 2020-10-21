import pygame
from needs.Text import Text
from needs.Button import Button

class MainWindow:
    def __init__(self):
        self.backgroundSize = (800, 600)
        self.backgroundColor = (0, 0, 0)
        self.title = "Codename TR"

        # Initialize pygame
        pygame.init()

        self.start()


    def start(self):
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            screen = pygame.display.set_mode(self.backgroundSize)
            pygame.display.set_caption(self.title)

            # background
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill(self.backgroundColor)

            # print title
            titleText = Text("Codename Tr", (225, 150))

            screen.blit(background, (0, 0))
            screen.blit(titleText.getText(), titleText.getTextPos())
            # initiate button
            startButton = Button(screen, "hola", (0, 255, 0), 150, 450, 100, 50)
            startButton.drawButton()

            pygame.display.flip()
            
            pygame.display.update()
                


if __name__=="__main__":
    start = MainWindow()