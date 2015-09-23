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
