import pygame

from buffalo import utils
from buffalo.label import Label
from buffalo.button import Button

def init():

    global buttons
    global labels 

    buttons = set([])
    labels = set([])

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

def logic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            utils.end = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                utils.end = True
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

def update():
    pass

def render():
    utils.screen.fill( BACKGROUND_COLOR )

    for label in labels:
        label.blit( utils.screen )
    for button in buttons:
        button.blit( utils.screen )

    pygame.display.update()
    
