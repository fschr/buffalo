__author__ = "Thomas Fischer"
import pygame
import pygame.font
from buffalo import utils

class Label:
    def __init__(self,
                 pos,
                 text,
                 antialiasing=True, 
                 color=(255, 255, 255, 255),
                 font="default",
                 invert_y_pos=False,
                 invert_x_pos=False,
                 x_centered=False,
                 y_centered=False,
                 ):
        self.pos = pos
        self.text = text
        self.antialiasing = antialiasing
        self.color = color
        self.font = font
        self.surface = None
        self.render()
        if invert_y_pos:
            self.pos = (self.pos[0], self.pos[1] - self.surface.get_size()[1])
        if invert_x_pos:
            self.pos = (self.pos[0] + self.surface.get_size()[0], self.pos[1])
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
