__author__ = "Thomas Fischer"
from math import pi

import pygame
import pygame.draw

from buffalo.label import Label

class Button:
    def __init__(self,
                 pos,
                 text,
                 antialiasing=True, 
                 color=(255, 255, 255, 255),
                 bg_color=(0, 100, 200, 255),
                 sel_color=(0, 50, 100, 255),
                 font="default",
                 invert_y_pos=False,
                 invert_x_pos=False,
                 x_centered=False,
                 y_centered=False,
                 feathering=15,
                 func=None,
                 ):
        self.label = Label(
            (feathering, feathering),
            text,
            antialiasing=antialiasing,
            color=color,
            font=font,
            invert_y_pos=False,
            invert_x_pos=False,
            x_centered=False,
            y_centered=False,
            )
        self.pos = pos
        self.bg_color = bg_color
        self.sel_color = sel_color
        self.feathering = feathering
        self.func = func
        self.selected = False
        self.size = (
            self.label.surface.get_size()[0] + self.feathering * 2,
            self.label.surface.get_size()[1] + self.feathering * 2,
            )
        self.render()
        if invert_y_pos:
            self.pos = (self.pos[0], self.pos[1] - self.size[1])
        if invert_x_pos:
            self.pos = (self.pos[0] - self.size[0], self.pos[1])
        if x_centered:
            self.pos = (self.pos[0] - self.size[0] / 2, self.pos[1])
        if y_centered:
            self.pos = (self.pos[0], self.pos[1] - self.size[1] / 2)
    
    def set_selected( self, value ):
        if not self.selected == value:
            self.selected = value
            self.render()

    def get_rect(self):
        return pygame.Rect( self.pos, self.size )

    def render(self):
        self.surface = pygame.Surface( self.size ).convert_alpha()
        self.surface.fill( (0, 0, 0, 0) )
        if self.selected:
            color = self.sel_color
        else:
            color = self.bg_color
        self.surface.fill( 
            color,
            pygame.Rect(
                self.feathering, 0,
                self.size[0] - 2 * self.feathering, self.size[1]
                )
            )
        self.surface.fill( 
            color,
            pygame.Rect(
                0, self.feathering,
                self.size[0], self.size[1] - 2 * self.feathering
                )
            )
        pygame.draw.arc(
            self.surface,
            color,
            pygame.Rect(
                0, 0,
                self.feathering * 2, self.feathering * 2
                ),
            pi, pi / 2,
            self.feathering
            )
        pygame.draw.arc(
            self.surface,
            color,
            pygame.Rect(
                self.size[0] - self.feathering * 2, 0,
                self.feathering * 2, self.feathering * 2
                ),
            pi / 2, 0,
            self.feathering
            )
        self.label.blit(self.surface)
        pygame.draw.arc(
            self.surface,
            color,
            pygame.Rect(
                0, self.size[1] - self.feathering * 2,
                self.feathering * 2, self.feathering * 2
                ),
            3 * pi / 2, pi,
            self.feathering
            )
        pygame.draw.arc(
            self.surface,
            color,
            pygame.Rect(
                self.size[0] - self.feathering * 2,
                self.size[1] - self.feathering * 2,
                self.feathering * 2, self.feathering * 2
                ),
            3 * pi / 2, 0,
            self.feathering
            )
        self.label.blit(self.surface)

    def blit(self, dest):
        dest.blit(self.surface, self.pos)
