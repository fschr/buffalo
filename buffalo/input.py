__author__ = "Thomas Fischer"

import pygame

from buffalo import utils
from buffalo.label import Label

class Input(object):

    DEFAULT_ANTIALIASING = True
    DEFAULT_COLOR        = (255, 255, 255, 255)
    DEFAULT_FONT         = "default"
    DEFAULT_INVERT_X_POS = False
    DEFAULT_INVERT_Y_POS = False
    DEFAULT_X_CENTERED   = False
    DEFAULT_Y_CENTERED   = False
    DEFAULT_FUNC         = None

    def __init__(
            self,
            pos,
            text,
            antialiasing = None,
            color        = None,
            font         = None,
            invert_y_pos = None,
            invert_x_pos = None,
            x_centered   = None,
            y_centered   = None,
            max_chars    = None,
            func         = None,
    ):
        antialiasing = antialiasing if antialiasing is not None else Input.DEFAULT_ANTIALIASING
        color        = color if color is not None else Input.DEFAULT_COLOR
        font         = font if font is not None else Input.DEFAULT_FONT
        invert_x_pos = invert_x_pos if invert_x_pos is not None else Input.DEFAULT_INVERT_X_POS
        invert_y_pos = invert_y_pos if invert_y_pos is not None else Input.DEFAULT_INVERT_Y_POS
        x_centered   = x_centered if x_centered is not None else Input.DEFAULT_X_CENTERED
        y_centered   = y_centered if y_centered is not None else Input.DEFAULT_Y_CENTERED
        self.label = Label(
            pos,
            text,
            antialiasing = antialiasing,
            color        = color,
            font         = font,
            invert_y_pos = invert_y_pos,
            invert_x_pos = invert_x_pos,
            x_centered   = x_centered,
            y_centered   = y_centered,
            )
        self.max_chars = max_chars if max_chars is not None else Input.DEFAULT_MAX_CHARS
        self.func     = func if func is not None else Input.DEFAULT_FUNC
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
        elif len(self.label.text) - 1 < self.max_chars and \
        (
        (c >= pygame.K_a and c <= pygame.K_z) or \
        (c >= pygame.K_0 and c <= pygame.K_9) or \
        (c == pygame.K_SPACE)
        ):
            if (c >= pygame.K_a and c <= pygame.K_z) and \
               (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                c -= 32
            self.label.text = self.label.text[:-1] + chr(c) + '|'
            self.label.render()

    def blit(self, dest):
        self.label.blit( dest )
