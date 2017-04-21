Installing Buffalo
==================

To install Buffalo, simply download a copy of the source via ssh
::

    git clone git@github.com:fschr/buffalo.git

or via https
::

    git clone https://github.com/fschr/buffalo

Navigate to cloned repository and install it (Buffalo is compatible with any version of Python greater than or equal to 2.5)
::

    python setup.py install 

Of course, Buffalo requires Pygame.

Testing Buffalo
===============

To test Buffalo, run the following command
::

    python -m buffalo.examples.main

A fullscreen Pygame program should appear with an horizontally-centered exit button and a label aligned with the lower left corner.

Examples
========

To begin rapid Pygame development, use the example files as a basic template:

main.py
-------

Import necessary modules
::

    import pygame
    
    from buffalo import utils
    
    from buffalo.examples.menu import Menu

Create the main loop
::

    def main():
    
        while not utils.end:
            utils.scene.logic()
            utils.scene.update()
            utils.scene.render()
            utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )

Initialize everything
::

    if __name__ == "__main__":
    
        if not utils.init(
                caption='Buffalo Project',
        ):
            print('buffalo.utils failed to initialize')
            pygame.quit()
            exit()
    
        utils.set_scene( Menu() )

Call the main loop and destruct Pygame upon completion
::

        main()
    
        pygame.quit()

menu.py
-------

This file represents the main menu.

First, import necessary modules
::

    import pygame
    
    from buffalo import utils
    from buffalo.scene import Scene
    from buffalo.label import Label
    from buffalo.button import Button
    from buffalo.input import Input
    from buffalo.option import Option

Write some initialization code
::

    class Menu(Scene):
    
        def __init__(self):
            Scene.__init__(self)

Add some Labels, Inputs, Options, and Buttons.
::

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

Define what happens when the escape key is pressed
::

        def on_escape(self):
            exit()

Define what needs to be updated independent of framrate. If Pong were made with Buffalo, the ball's position would be updated here. This way, the program's speed is not dependent on framerate.
::

        def update(self):
            pass

Finally, draw all non-Buffalo objects (Labels, Buttons, Options, and Inputs are drawn automatically).
::

        def blit(self):
            pass

License and Redistribution
==========================

This project licensed under the GNU GENERAL PUBLIC LICENSE version 2. Everyone is free to use, modify, or redistribute this code, as long as the names of the original authors are noted.

Original Authors
================

Thomas Fischer

Benjamin Congdon

