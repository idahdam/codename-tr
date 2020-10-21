import pygame

class Text:
    def __init__(self, text, position):
        self.text = text
        self.font = pygame.font.SysFont(None, 72)
        self.position = position
        self.textPrint = self.font.render(self.text, True, (255, 255, 255))

    def getText(self):
        return self.textPrint

    def getTextPos(self):
        return self.position
