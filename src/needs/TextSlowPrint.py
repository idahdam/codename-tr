# slow print
import pygame, pygame.font, time

class TextSlowPrint:
    def __init__(self, screen, text, position, size):
        super().__init__()
        self.screen = screen
        self.text = text
        self.font = pygame.font.SysFont(None, size)
        self.position = position
        # self.textPrint = self.font.render(self.text, True, (255, 255, 255))

    def getText(self):
        return self.textPrint

    def getTextPos(self):
        return self.position

    def blitText(self):
        for letter in self.text:
            textPrintSlow = self.font.render(letter, True, (255, 255, 255))
            self.screen.blit(textPrintSlow, self.getTextPos())
            time.sleep(0.5)

