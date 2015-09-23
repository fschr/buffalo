import pygame

from buffalo import utils

class Slider(object):
    
    WIDTH, HEIGHT = 50, 250
    COLOR         = (255, 255, 255, 255)
    SPEED         = 10.0
    
    def __init__(self, pos, keybindings):
        self.pos = pos
        self.up, self.down = keybindings

        x, y = self.pos
        self.fPos = float(x), float(y)
        
        self.yv = 0.0
        self.surface = utils.empty_surface( (Slider.WIDTH, Slider.HEIGHT) )
        self.surface.fill( Slider.COLOR )

    def update(self, keys):
        self.yv = 0.0
        if keys[self.up]:
            self.yv += -Slider.SPEED
        if keys[self.down]:
            self.yv += Slider.SPEED
        if not keys[self.down] and not keys[self.up]:
            self.yv = 0.0
        x, y = self.fPos
        y = y + self.yv if y + self.yv + Slider.HEIGHT <= utils.SCREEN_H and y + self.yv >= 0 else y
        self.fPos = x, y
        self.pos = int(x), int(y)

    def blit(self, dest):
        dest.blit(self.surface, self.pos)
