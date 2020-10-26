# custom buttons
import pygame, pygame.surface
from needs.Text import Text

class Button:
    def __init__(self, screen, text, color, x, y, width, height, deltaX, deltaY, fontSize):
        self.screen = screen
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.fontSize = fontSize

    def drawButton(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        buttonText = Text(self.screen, self.text, (self.x, self.y), self.fontSize)
        buttonText.center = (self.x + self.deltaX, self.y + self.deltaY)
        self.screen.blit(buttonText.getText(), buttonText.center)
    

        
    

