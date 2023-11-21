import sys
import pygame as pg
from settings import *
from Intro import Intro


class Game:
    def __init__(self):
        # game variables
        pg.init()
        self.screen = pg.display.set_mode(BG_SIZE)
        self.status = INTRO
        self.running = True  # game is running

    def run(self):
        # check for the current menu depending on the status
        while self.running:
            if self.status == INTRO:
                Intro(self)

