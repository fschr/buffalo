# buffalo

Buffalo is an extremely lightweight Python module to assist rapid Pygame development. The source includes labels, buttons, and basic utilities.

# Examples

To begin rapid Pygame development, use the example files as a basic template:

### main.py

Import necessary modules

```
import pygame

from buffalo import utils
import menu
```

Create the main loop

```
def main():

    while not utils.end:
        utils.logic()
        utils.update()
        utils.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )
```

Initialize everything

```
if __name__ == "__main__":
    
    if not utils.init( 
        logic_func=menu.logic, 
        update_func=menu.update, 
        render_func=menu.render,
        ):
        print('buffalo.utils failed to initialize')
        pygame.quit()
        exit()

    menu.init()
```

Call the main loop and destruct Pygame upon completion

```
    main()

    pygame.quit()
```

### menu.py

This file represents the main menu.

First, import necessary modules

```
import pygame

from buffalo import utils
from buffalo.label import Label
from buffalo.button import Button
```

Write the initialization code

```
def init():

    global buttons
    global labels 

    buttons = set([])
    labels = set([])
```

Add some labels and buttons here, too:

```
    label_version = Label(
        (5, utils.SCREEN_H - 5),
        "Buffalo Program 0.0 alpha + July 15th, 2015",
        invert_y_pos=True,
        )
    labels.add( label_version )

    button_exit = Button(
        (utils.SCREEN_W / 2, 3 * utils.SCREEN_H / 4),
        "Exit",
        x_centered=True,
        y_centered=True,
        feathering=10,
        func=exit,
        )
    buttons.add( button_exit )
```

Next, define the logic of the main menu. First, basic events and keyboard input

```
def logic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            utils.end = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                utils.end = True
```

Then, mouse input and button interaction

```
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.get_rect().collidepoint( mouse_pos ):
                    button.set_selected(True)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                button.set_selected(False)
                if button.get_rect().collidepoint( mouse_pos ):
                    if button.func is not None:
                        button.func()
```

Describe the update function (The update function is a function that gets called at a certain interval, independent of a user's frames per second. In this case, it's empty)

```
def update():
    pass
```

And finally, describe the render function

```
def render():
    utils.screen.fill( BACKGROUND_COLOR )

    for label in labels:
        label.blit( utils.screen )
    for button in buttons:
        button.blit( utils.screen )

    pygame.display.update()
```