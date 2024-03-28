import pygame
from pygame import RLEACCEL


class Sprite(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.rect = None
        self.x = x
        self.y = y

    def init_image(self, imgPath):
        self.image = pygame.image.load(imgPath).convert()
        self.image.set_colorkey(self.image.get_at((0, 0)), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def move_x(self, x):
        self.x = self.x + x
        self._move()

    def move_y(self, y):
        self.y = self.y + y
        self._move()

    def set_x(self, x):
        self.x = x
        self._move()

    def set_y(self, y):
        self.y = y
        self._move()

    def _move(self):
        self.rect.center = (self.x, self.y)
