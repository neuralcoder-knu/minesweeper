import os

import pygame
from pygame import RLEACCEL

from textsprite import TextSprite


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, area, parent, bomb=False):
        pygame.sprite.Sprite.__init__(self)

        self.parent = parent
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.px = x
        self.py = y
        self.x = x * 20
        self.y = y * 20 + 40
        self.area_p = area
        self.bomb = bomb
        self.open = False
        self.flag = False
        self.textSprite = TextSprite(self.x + 10, self.y + 10)
        self.paint()
        self.generateImage()

    def generateImage(self):
        self.image = pygame.image.load(os.path.join('data', 'point.png')).convert()
        self.image.set_colorkey(self.image.get_at((0, 0)), RLEACCEL)
        self.rect = self.image.get_rect()

        self.rect.center = (self.x + 10, self.y + 10)

    def get_surface_rect(self):
        left = self.rect.left
        top = self.rect.top
        width = self.rect.width
        height = self.rect.height * 0.1
        return pygame.Rect(left, top, width, height)

    def paint(self):
        if self.open:
            if self.have_bomb():
                self.textSprite.setText('b')
                self.parent.end_game(1)
            else:
                number = self.near_bombs()
                self.textSprite.setText('%d' % (number,))
                if number == 0:
                    self.textSprite.setText('-')
                    for p in self.get_around():
                        if not p.open:
                            p.push()
        elif self.flag:
            self.textSprite.setText('f')
        else:
            self.textSprite.setText(' ')
        self.textSprite.generateImage()

    def _test_p(self, x, y):
        if x in range(len(self.area_p[0])):
            if y in range(len(self.area_p)):
                return True
        return False

    def have_bomb(self):
        return self.bomb

    def get_around(self):
        ret = []
        if self._test_p(self.px - 1, self.py - 1):
            ret.append(self.area_p[self.px - 1][self.py - 1])
        if self._test_p(self.px, self.py - 1):
            ret.append(self.area_p[self.px][self.py - 1])
        if self._test_p(self.px + 1, self.py - 1):
            ret.append(self.area_p[self.px + 1][self.py - 1])
        if self._test_p(self.px - 1, self.py):
            ret.append(self.area_p[self.px - 1][self.py])
        if self._test_p(self.px + 1, self.py):
            ret.append(self.area_p[self.px + 1][self.py])
        if self._test_p(self.px - 1, self.py + 1):
            ret.append(self.area_p[self.px - 1][self.py + 1])
        if self._test_p(self.px, self.py + 1):
            ret.append(self.area_p[self.px][self.py + 1])
        if self._test_p(self.px + 1, self.py + 1):
            ret.append(self.area_p[self.px + 1][self.py + 1])
        return ret

    def near_bombs(self):
        b = 0
        for x in self.get_around():
            if x.have_bomb():
                b += 1
        return b

    def push(self):
        if not self.flag:
            self.open = True
        self.paint()

    def p_flag(self):
        if not self.open:
            self.flag = not self.flag
        self.paint()

    def p_test(self):
        b = self.near_bombs()
        b, self.open, self.flag
        if (b > 0) and (self.open) and (not self.flag):
            f_len = 0
            for x in self.get_around():
                if x.flag:
                    f_len += 1
            if f_len == b:
                for x in self.get_around():
                    x.push()
