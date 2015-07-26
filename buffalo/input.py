__author__ = "Thomas Fischer"
import pygame

from buffalo import utils
from buffalo.label import Label

class Input(object):
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
                 func=None,
                 ):
        self.label = Label(
            pos,
            text,
            antialiasing=antialiasing,
            color=color,
            font=font,
            invert_y_pos=invert_y_pos,
            invert_x_pos=invert_x_pos,
            x_centered=x_centered,
            y_centered=y_centered,
            )
        self.func = func
        self.selected = False

    def get_rect(self):
        return pygame.Rect( self.label.pos, self.label.surface.get_size() )

    def select(self):
        if not self.selected:
            self.selected = True
            self.label.text = self.label.text + '|'
            self.label.render()

    def deselect(self):
        if self.selected:
            self.selected = False
            self.label.text = self.label.text[:-1]
            self.label.render()
            if self.func is not None:
                self.func()

    def process_char(self, c):
        if c == pygame.K_ESCAPE:
            self.deselect()
        elif c == pygame.K_RETURN:
            self.deselect()
            if self.func is not None:
                self.func()
        elif c == pygame.K_BACKSPACE:
            self.label.text = self.label.text[:-2] + '|'
            self.label.render()
        elif (c >= pygame.K_a and c <= pygame.K_z) or c == pygame.K_SPACE:
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                c -= 32
            self.label.text = self.label.text[:-1] + chr(c) + '|'
            self.label.render()

    def blit(self, dest):
        self.label.blit( dest )
