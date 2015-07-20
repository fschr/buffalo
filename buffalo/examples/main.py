__author__ = "Thomas Fischer"
import pygame

from buffalo import utils
from buffalo.examples import menu

def main():

    while not utils.end:
        utils.logic()
        utils.update()
        utils.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )

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
    main()

    pygame.quit()
