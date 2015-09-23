What is a Scene? (and how to make Pong)
=======================================

In Buffalo, it is necessary to work with ``Scene``. A ``Scene`` can be thought of as a state of your program. To help explain how to use ``Scene`` and what a ``Scene`` is, exactly, we will make Pong.

main.py (The boilerplate)
-------------------------

First, we need to define the entry point of our program. Here's the boilerplate code that you should always write when using Buffalo:
::

    import pygame
    
    from buffalo import utils
    
    def main():
        
        while not utils.end:
            utils.scene.logic()
            utils.scene.update()
            utils.scene.render()
            utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )
    
    if __name__ == "__main__":
        
        if not utils.init(
                caption="Pong Tutorial",
        ):
            print("buffalo.utils failed to initialize")
            pygame.quit()
            exit()
        
        from menu import Menu

        utils.set_scene( Menu() )
        
        main()
        
        pygame.quit()
    

One of the only two things that should ever change in ``main.py`` is the value you pass as the ``caption`` keyword argument in ``utils.init``. The second thing that should (rather, may) change in ``main.py`` is your imports. Notice where the line ``from menu import Menu`` is located. This is a nice thing about Python that allows users to easily workaround the classic A-imports-B-but-B-imports-A situation.

menu.py (our first Scene)
-------------------------

Now we need to make a main menu. Create a file called ``menu.py``. In this file, we'll do one thing: create a class called ``Menu`` that extends ``Scene``.

Since the source code is rather short, I'll just paste it all right here. We can talk about it afterwards.
::

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


The first thing we do is import standard library modules, ``pygame``, and all of the stuff we'll need from Buffalo. Then, our class begins. All ``Scene`` objects must contain four methods:

1. The constructor (``def __init__(self):``)
2. The ``on_escape`` method
3. The ``update`` method
4. The ``blit`` method

The constructor
---------------

The constructor is  where everything is initialized. First, the background color of this scene is set to black, and the default color of buttons is set to dark red. Next, we add a label that says "PONG" in the center of the screen. Finally, Two buttons are added: one that says "Play" and one that says "Exit".

The play button might seem a little bit complicated. It's positioned just below the center of the screen, so as not to over lap the "PONG" label, and its func (``go_to_play``) is defined just before the button is initialized.

The exit button is fairly straightforward if you understand how the play button works. When it is pressed, ``sys.exit()`` is called, exiting the program.

The ``on_escape`` method
------------------------

The contents of ``on_escape`` cause the program to exit when the ESCAPE key is pressed.

The ``update`` method and the ``blit`` method
---------------------------------------------

We don't need to update or blit anything other than Buffalo objects, so ``update`` and ``blit`` are empty.

play.py (our second scene)
--------------------------

Here's the source code for our second scene. I don't have time to document it just yet. You can expect more complete documentation within the next few weeks.
::
    
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

You can find the rest of the (undocumented) source code below.

slider.py
---------
::
    
    import pygame
    
    from buffalo import utils
    
    class Slider(object):
        
        WIDTH, HEIGHT = 50, 250
        COLOR         = (255, 255, 255, 255)
        SPEED         = 10.0
        
        def __init__(self, pos, keybindings):
            self.pos = pos
            self.up, self.down = keybindings
    
            x, y = self.pos
            self.fPos = float(x), float(y)
            
            self.yv = 0.0
            self.surface = utils.empty_surface( (Slider.WIDTH, Slider.HEIGHT) )
            self.surface.fill( Slider.COLOR )
    
        def update(self, keys):
            self.yv = 0.0
            if keys[self.up]:
                self.yv += -Slider.SPEED
            if keys[self.down]:
                self.yv += Slider.SPEED
            if not keys[self.down] and not keys[self.up]:
                self.yv = 0.0
            x, y = self.fPos
            y = y + self.yv if y + self.yv + Slider.HEIGHT <= utils.SCREEN_H and y + self.yv >= 0 else y
            self.fPos = x, y
            self.pos = int(x), int(y)
    
        def blit(self, dest):
            dest.blit(self.surface, self.pos)

square.py
---------
::

    from random import random
    
    import pygame
    
    from buffalo import utils
    
    from slider import Slider
    
    class Square(object):
    
        WIDTH, HEIGHT = 40, 40
        COLOR       = (255, 255, 255, 255)
    
        def __init__(self, pos):
            self.pos = pos
            x, y = self.pos
            self.fPos = float(x), float(y)
    
            rxv, ryv = random(), random()
            minimum, mult = 3.0, 8.0
            while abs(rxv) < minimum:
                rxv = (-mult / 2) + mult * random()
            while abs(ryv) < minimum:
                ryv = (-mult / 2) + mult * random()    
    
            self.xv, self.yv = rxv, ryv
            self.surface = utils.empty_surface( (Square.WIDTH, Square.HEIGHT) )
            self.surface.fill( Square.COLOR )
    
        def update(self, sliderPositions):
            x, y = self.fPos
            for sliderPosition in sliderPositions:
                sx, sy = sliderPosition
                if abs(x - (sx + Slider.WIDTH)) <= 5.0 or abs(sx - (x + Square.WIDTH)) <= 5.0:
                    if y <= sy + Slider.HEIGHT and y + Square.HEIGHT >= sy:
                        ydiff = ((y + Square.HEIGHT / 2) - (sy + Slider.HEIGHT / 2))
                        ydmax = ydiff / (Slider.HEIGHT / 2)
                        boost = 0.005 * ydiff / ydmax
                        self.xv = -(self.xv + boost) if self.xv > 0.0 else -(self.xv - boost)
                        self.yv = self.yv + boost if self.yv > 0.0 else self.yv - boost
                        break
            if y <= 0.0 or y + Square.HEIGHT >= utils.SCREEN_H:
                self.yv = -self.yv
            x += self.xv
            y += self.yv
            self.fPos = x, y
            self.pos = int(x), int(y)
    
        def blit(self, dest):
            dest.blit(self.surface, self.pos)
