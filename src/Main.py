import pygame

class MainWindow:
    def __init__(self):
        self.backgroundSize = (800, 600)
        self.backgroundColor = (0, 255, 0)
        self.title = "Codename TR"

        # Initialize pygame
        pygame.init()

        screen = pygame.display.set_mode(self.backgroundSize)
        pygame.display.set_caption(self.title)

        # background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(self.backgroundColor)

        screen.blit(background, (0, 0))
        pygame.display.flip()

        self.start()


    def start(self):
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            


            pygame.display.update()
                


if __name__=="__main__":
    start = MainWindow()