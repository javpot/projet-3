import sys
import pygame as pg
from Button import Button
from settings import *


class Intro:
    def __init__(self, game):
        self.game = game

        start = Button("start", 400, 275, 300, 100)
        guide = Button("guide", 400, 400, 300, 100)
        about = Button("about", 400, 525, 300, 100)
        INTRO_BG = pg.image.load("../assests/backgrounds/intro.png")

        while self.game.status == INTRO:
            pg.display.set_caption("INTRO")

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.game.screen.blit(INTRO_BG, ORIGIN)
            self.game.screen.blit(start.image, (start.x, start.y))
            self.game.screen.blit(guide.image, (guide.x, guide.y))
            self.game.screen.blit(about.image, (about.x, about.y))

            pg.display.flip()
