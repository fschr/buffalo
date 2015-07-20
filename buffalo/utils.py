import pygame
import pygame.font

def init( logic_func=None, 
          update_func=None, 
          render_func=None,
          caption='Pygame',
          fullscreen=True,
          frames_per_second=120,
          cap_frame_rate=False,
          clear_color=(0,0,0,0),
          ):

    global SCREEN_W, SCREEN_H
    global SCREEN_S, SCREEN_M
    global screen
    global clock
    global end
    
    if not pygame.init():
        print('Failed to initialize Pygame')
        return False

    if fullscreen:

        dinf = pygame.display.Info()
        SCREEN_S = SCREEN_W, SCREEN_H = (dinf.current_w, dinf.current_h)
        SCREEN_M = (SCREEN_W / 2, SCREEN_H / 2)
        screen = pygame.display.set_mode(SCREEN_S, pygame.FULLSCREEN)
        clock  = pygame.time.Clock()

    end = False

    pygame.display.set_caption(caption)
    
    global CLEAR_COLOR
    global CAP_FRAME_RATE
    global FRAMES_PER_SECOND    

    CLEAR_COLOR = clear_color
    CAP_FRAME_RATE = cap_frame_rate
    FRAMES_PER_SECOND = frames_per_second
    
    global logic
    global update
    global render    

    logic = logic_func
    update = update_func
    render = render_func

    global delta
    delta = 1000
    
    pygame.font.init()

    if not pygame.font.get_init():
        print('pygame.font failed to initialize')
        return False
    
    global DEFAULT_FONT
    global fonts
    DEFAULT_FONT = "arial"
    fonts = {
        'default': pygame.font.SysFont(DEFAULT_FONT, 18),
        'droidsans14': pygame.font.SysFont("droidsans", 18),
        }
    
    return True
