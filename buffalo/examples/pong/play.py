import pygame

from buffalo import utils
from buffalo.scene import Scene

from slider import Slider
from square import Square

class Play(Scene):
    
    def __init__(self):
        Scene.__init__(self)

        self.BACKGROUND_COLOR = (0, 0, 0, 255)

        self.slider1 = Slider(
            (50, utils.SCREEN_H // 2 - Slider.HEIGHT),
            (pygame.K_w, pygame.K_s),
        )
        self.slider2 = Slider(
            (utils.SCREEN_W - Slider.WIDTH - 50, utils.SCREEN_H // 2 - Slider.HEIGHT),
            (pygame.K_UP, pygame.K_DOWN),
        )
        self.square  = Square(
            (utils.SCREEN_W // 2 - Square.WIDTH // 2, utils.SCREEN_H // 2 - Square.HEIGHT // 2),
        )

    def go_to_menu(self):
        from menu import Menu
        utils.set_scene( Menu() )

    def on_escape(self):
        self.go_to_menu()

    def update(self):
        keys = pygame.key.get_pressed()
        self.slider1.update(keys)
        self.slider2.update(keys)
        self.square.update( (self.slider1.fPos, self.slider2.fPos) )

    def blit(self):
        self.slider1.blit(utils.screen)
        self.slider2.blit(utils.screen)
        self.square.blit(utils.screen)
