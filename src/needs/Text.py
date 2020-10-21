import pygame

class Text:
    def __init__(self, text, position, size):
        self.text = text
        self.font = pygame.font.SysFont(None, size)
        self.position = position
        self.textPrint = self.font.render(self.text, True, (255, 255, 255))

    def getText(self):
        return self.textPrint

    def getTextPos(self):
        return self.position
