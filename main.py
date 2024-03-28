import pygame

from config import tps
from game import Game
from location import StartLocation


def main():
    game = Game()

    start_location = StartLocation(game)

    game.location = start_location

    clock = pygame.time.Clock()
    while 1:
        clock.tick(tps)
        game.location.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            game.location.event(event)
            game.event(event)

if __name__ == "__main__":
    main()
