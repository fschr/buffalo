from random import random

import pygame

from buffalo import utils

from slider import Slider

class Square(object):

    WIDTH, HEIGHT = 40, 40
    COLOR       = (255, 255, 255, 255)

    def __init__(self, pos):
        self.pos = pos
        x, y = self.pos
        self.fPos = float(x), float(y)

        rxv, ryv = random(), random()
        minimum, mult = 3.0, 8.0
        while abs(rxv) < minimum:
            rxv = (-mult / 2) + mult * random()
        while abs(ryv) < minimum:
            ryv = (-mult / 2) + mult * random()    

        self.xv, self.yv = rxv, ryv
        self.surface = utils.empty_surface( (Square.WIDTH, Square.HEIGHT) )
        self.surface.fill( Square.COLOR )

    def update(self, sliderPositions):
        x, y = self.fPos
        for sliderPosition in sliderPositions:
            sx, sy = sliderPosition
            if abs(x - (sx + Slider.WIDTH)) <= 5.0 or abs(sx - (x + Square.WIDTH)) <= 5.0:
                if y <= sy + Slider.HEIGHT and y + Square.HEIGHT >= sy:
                    ydiff = ((y + Square.HEIGHT / 2) - (sy + Slider.HEIGHT / 2))
                    ydmax = ydiff / (Slider.HEIGHT / 2)
                    boost = 0.005 * ydiff / ydmax
                    self.xv = -(self.xv + boost) if self.xv > 0.0 else -(self.xv - boost)
                    self.yv = self.yv + boost if self.yv > 0.0 else self.yv - boost
                    break
        if y <= 0.0 or y + Square.HEIGHT >= utils.SCREEN_H:
            self.yv = -self.yv
        x += self.xv
        y += self.yv
        self.fPos = x, y
        self.pos = int(x), int(y)

    def blit(self, dest):
        dest.blit(self.surface, self.pos)
