import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.input import Input
from buffalo.option import Option

class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.labels.add(
            Label(
                (5, 5),
                "Hello, World!",
            )
        )
        self.inputs.add(
            Input(
                (50, 50),
                "I'm an Input. Edit me, please.",
            )
        )
        self.options.add(
            Option(
                (100, 100),
                ("Option 1", "Option 2"),
            )
        )
        self.buttons.add(
            Button(
                (200, 200),
                ("As a Button, I find this offensive."),
            )
        )

    def on_escape(self):
        exit()

    def update(self):
        pass

    def blit(self):
        pass
