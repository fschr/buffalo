__author__ = "Thomas Fischer"
import pygame
import pygame.draw

from buffalo import utils
from buffalo.label import Label

class Option(object):
    def __init__(
            self,
            pos,
            data,
            antialiasing=True,
            color=(255, 255, 255, 255),
            font="default",
            invert_y_pos=False,
            invert_x_pos=False,
            x_centered=False,
            y_centered=False,
            a_color=(0, 100, 200, 255),
            sel_color=(0, 50, 100, 255),
            padding=10,
            rfunc=None,
            lfunc=None,
    ):
        self.pos = pos
        self.data = data
        self.antialiasing = antialiasing
        self.color = color
        self.font = font
        self.index = 0
        self.left_selected = False
        self.right_selected = False
        self.a_color = a_color
        self.sel_color = sel_color
        self.padding = padding
        self.rfunc = rfunc
        self.lfunc = lfunc
        self.render()
        if invert_y_pos:
            self.pos = (self.pos[0], self.pos[1] - self.size[1])
        if invert_x_pos:
            self.pos = (self.pos[0] - self.size[0], self.pos[1])
        if x_centered:
            self.pos = (self.pos[0] - self.size[0] / 2, self.pos[1])
        if y_centered:
            self.pos = (self.pos[0], self.pos[1] - self.size[1] / 2)

    def go_right(self):
        self.index += 1
        self.index %= len(self.data)
        self.right_selected = False
        self.render()
        if self.rfunc is not None:
            self.rfunc()

    def go_left(self):
        self.index -= 1
        self.index %= len(self.data)
        self.left_selected = False
        self.render()
        if self.lfunc is not None:
            self.lfunc()

    def render_left_arrow(self):
        if self.left_selected:
            present_color = self.sel_color
        else:
            present_color = self.a_color
        pygame.draw.polygon(
            self.surface,
            present_color,
            (
                (0, self.size[1] / 2),
                (int(self.size[1] * 0.9), int(self.size[1] * 0.1)),
                (int(self.size[1] * 0.9), int(self.size[1] * 0.9))
            ),
        )

    def render_right_arrow(self):
        if self.right_selected:
            present_color = self.sel_color
        else:
            present_color = self.a_color
        pygame.draw.polygon(
            self.surface,
            present_color,
            (
                (self.size[0] - int(self.size[1] * 0.9), int(self.size[1] * 0.1)),
                (self.size[0] - int(self.size[1] * 0.1), self.size[1] / 2),
                (self.size[0] - int(self.size[1] * 0.9), int(self.size[1] * 0.9))
            ),
        )

    def set_left_selected( self, value ):
        if not self.left_selected == value:
            self.left_selected = value
            self.render_left_arrow()

    def set_right_selected( self, value ):
        if not self.right_selected == value:
            self.right_selected = value
            self.render_right_arrow()

    def get_left_rect(self):
        return pygame.Rect(
            self.pos,
            (self.size[1], self.size[1])
        )

    def get_right_rect(self):
        return pygame.Rect(
            (self.pos[0] + self.size[0] - self.size[1], self.pos[1]),
            (self.size[1], self.size[1])
        )

    def render(self):
        self.label = Label(
            (0, 0),
            self.data[self.index],
            antialiasing=self.antialiasing,
            color=self.color,
            font=self.font,
            invert_y_pos=False,
            invert_x_pos=False,
            x_centered=False,
            y_centered=False,
            )
        self.label.pos = (self.label.surface.get_size()[1] + self.padding, self.label.pos[1])
        self.size = (
            self.label.surface.get_size()[0] + \
            2 * self.label.surface.get_size()[1] + self.padding * 2,
            self.label.surface.get_size()[1]
        )
        self.surface = pygame.Surface( self.size ).convert_alpha()
        self.surface.fill( (0, 0, 0, 0) )
        self.label.blit( self.surface )
        self.render_left_arrow()
        self.render_right_arrow()

    def blit(self, dest):
        dest.blit(self.surface, self.pos)
