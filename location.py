import sys

import pygame
from pygame import KEYDOWN, K_ESCAPE, QUIT, MOUSEBUTTONUP

from textsprite import TextSprite


class Location(object):
    parent = None

    def __init__(self, parent):
        self.window = pygame.display.get_surface()
        self.parent = parent
        self.background = pygame.image.load('data/background.png').convert()

    def event(self, event):
        pass

    def draw(self):
        pass
    
class StartLocation(Location):

    def __init__(self, parent):
        Location.__init__(self, parent)
        pygame.mouse.set_visible(1)
        pygame.key.set_repeat(0)
        self.messages = pygame.sprite.Group()
        self.window = pygame.display.get_surface()
        self.parent = parent
        self.restartbtn = TextSprite(40, 15, 'Restart', 30, (0, 0, 0))
        self.mainbuttons = pygame.sprite.Group()
        self.restartbtn.generateImage()
        self.mainbuttons.add(self.restartbtn)
        self.window.blit(self.background, (0, 0))
        self.in_game = False
        self.restart()

    def draw(self):
        self.controls.clear(self.window, self.background)
        self.controls.draw(self.window)
        self.controls_captions.draw(self.window)
        self.mainbuttons.draw(self.window)
        self.messages.draw(self.window)

    def event(self, event):
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        else:
            pass
        if event.type == MOUSEBUTTONUP:
            for p in self.points:
                for point in p:
                    if (point.rect.collidepoint(pygame.mouse.get_pos())) and (self.in_game):
                        # pass
                        print(event)
                        if event.button == 1:
                            point.push()
                        elif event.button == 3:
                            point.p_flag()
                        elif event.button == 2:
                            point.p_test()
            x, y = pygame.mouse.get_pos()
            print('x=%d,y=%d' % (x, y))
            self.test_finish()
            if y < 40:
                self.restart()

    def bombing(self, points):
        #Todo:


    def restart(self):
        #Todo:


    def end_game(self, reason):
        #Todo:


    def check_finish(self):
        #Todo:
