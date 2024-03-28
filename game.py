import sys

import pygame
from pygame import QUIT, KEYUP, K_ESCAPE

from config import width_x, height_y


class Game():

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((width_x * 20, height_y * 20 + 40))
        pygame.display.set_caption('Minesweeper')

    def event(self, event):
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit()
