import sys
import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.input import Input
from buffalo.option import Option

from play import Play

class Menu(Scene):
    
    def __init__(self):
        Scene.__init__(self)

        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        Button.DEFAULT_BG_COLOR = (100, 0, 0, 255)

        self.labels.add(
            Label(
                utils.SCREEN_M,
                "PONG",
                x_centered=True,
                y_centered=True,
                font="default48",
            )
        )

        def go_to_play():
            utils.set_scene( Play() )

        self.buttons.add(
                Button(
                    (utils.SCREEN_W // 2, utils.SCREEN_H // 2 + 100),
                    ("Play"),
		    x_centered=True,
		    y_centered=True,
                    func=go_to_play,
                )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W // 2, utils.SCREEN_H // 2 + 160),
                ("Exit"),
                x_centered=True,
                y_centered=True,
                func=sys.exit,
            )
        )

    def on_escape(self):
        exit()

    def update(self):
        pass

    def blit(self):
        pass
