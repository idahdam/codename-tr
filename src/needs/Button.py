# custom buttons
import pygame

class Button:
    def __init__(self, screen, text, color, x, y, width, height):
        self.screen = screen
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def drawButton(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        
    

