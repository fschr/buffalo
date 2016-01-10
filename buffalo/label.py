__author__ = "Thomas Fischer"

import pygame
import pygame.font
from buffalo import utils

class Label(object):

    DEFAULT_ANTIALIASING = True
    DEFAULT_COLOR        = (255, 255, 255, 255)
    DEFAULT_FONT         = "default"
    DEFAULT_INVERT_X_POS = False
    DEFAULT_INVERT_Y_POS = False
    DEFAULT_X_CENTERED   = False
    DEFAULT_Y_CENTERED   = False
    
    def __init__(
            self,
            pos,
            text,
            antialiasing = None,
            color        = None,
            font         = None,
            invert_x_pos = None,
            invert_y_pos = None,
            x_centered   = None,
            y_centered   = None,
    ):
        self.pos          = pos
        self.text         = text
        self.antialiasing = antialiasing if antialiasing is not None else Label.DEFAULT_ANTIALIASING
        self.color        = color if color is not None else Label.DEFAULT_COLOR
        self.font         = font if font is not None else Label.DEFAULT_FONT
        invert_x_pos      = invert_x_pos if invert_x_pos is not None else Label.DEFAULT_INVERT_X_POS
        invert_y_pos      = invert_y_pos if invert_y_pos is not None else Label.DEFAULT_INVERT_Y_POS
        x_centered        = x_centered if x_centered is not None else Label.DEFAULT_X_CENTERED
        y_centered        = y_centered if y_centered is not None else Label.DEFAULT_Y_CENTERED
        self.surface      = None
        self.render()
        if invert_y_pos:
            self.pos = (self.pos[0], self.pos[1] - self.surface.get_size()[1])
        if invert_x_pos:
            self.pos = (self.pos[0] - self.surface.get_size()[0], self.pos[1])
        if x_centered:
            self.pos = (self.pos[0] - self.surface.get_size()[0] / 2, self.pos[1])
        if y_centered:
            self.pos = (self.pos[0], self.pos[1] - self.surface.get_size()[1] / 2)
    
    def render(self):
        self.surface = utils.fonts[self.font].render(
            self.text,
            self.antialiasing,
            self.color,
        ).convert_alpha()
    
    def blit(self, dest):
        dest.blit(self.surface, self.pos)
