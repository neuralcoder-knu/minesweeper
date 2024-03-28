import pygame

from sprite import Sprite


class TextSprite(Sprite):
    def __init__(self, x, y, text='', size=20, color=(0, 0, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, size)
        self.color = color
        self.text = text

    def generateImage(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def setText(self, text):
        self.text = text
        if text == 'b':
            self.color = (255, 0, 0)
        elif text == 'f':
            self.color = (255, 150, 100)

    def setColor(self, color):
        self.color = color

    def setSize(self, size):
        self.font = pygame.font.Font(None, size)
