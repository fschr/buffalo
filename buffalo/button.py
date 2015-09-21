__author__ = "Thomas Fischer"

from math import pi

import pygame
import pygame.draw

from buffalo.label import Label

class Button(object):

    DEFAULT_ANTIALIASING = True
    DEFAULT_COLOR        = (255, 255, 255, 255)
    DEFAULT_BG_COLOR     = (0, 100, 200, 255)
    DEFAULT_SEL_COLOR    = (0, 50, 100, 255)
    DEFAULT_FONT         = "default"
    DEFAULT_INVERT_X_POS = False
    DEFAULT_INVERT_Y_POS = False
    DEFAULT_X_CENTERED   = False
    DEFAULT_Y_CENTERED   = False
    DEFAULT_FEATHERING   = 15
    DEFAULT_FUNC         = None

    def __init__(
            self,
            pos,
            text,
            antialiasing = True, 
            color        = (255, 255, 255, 255),
            bg_color     = (0, 100, 200, 255),
            sel_color    = (0, 50, 100, 255),
            font         = "default",
            invert_y_pos = False,
            invert_x_pos = False,
            x_centered   = False,
            y_centered   = False,
            feathering   = 15,
            func         = None,
    ):
        antialiasing = antialiasing if antialiasing is not None else Button.DEFAULT_ANTIALIASING
        color = color if color is not None else Button.DEFAULT_COLOR
        font = font if font is not None else Button.DEFAULT_FONT
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
        invert_x_pos = invert_x_pos if invert_x_pos is not None else Button.DEFAULT_INVERT_X_POS
        invert_y_pos = invert_y_pos if invert_y_pos is not None else Button.DEFAULT_INVERT_Y_POS
        x_centered = x_centered if x_centered is not None else Button.DEFAULT_X_CENTERED
        y_centered = y_centered if y_centered is not None else Button.DEFAULT_Y_CENTERED
        self.pos = pos
        self.bg_color = bg_color if bg_color is not None else Button.DEFAULT_BG_COLOR
        self.sel_color = sel_color if sel_color is not None else Button.DEFAULT_SEL_COLOR
        self.feathering = feathering if feathering is not None else Button.FEATHERING
        self.func = func if func is not None else Button.DEFAULT_FUNC
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
