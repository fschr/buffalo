__author__ = "Thomas Fischer"
import pygame
import pygame.font

def init(
        caption='Pygame',
        fullscreen=True,
        frames_per_second=60,
        cap_frame_rate=True,
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

    global scene
    scene = None

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
        'default': pygame.font.SysFont(DEFAULT_FONT, 12),
        'droidsans18': pygame.font.SysFont("droidsans", 18),
        'droidsans24': pygame.font.SysFont("droidsans", 24),
        'droidsans14': pygame.font.SysFont("droidsans", 14),
        }
    
    return True

def set_scene( other_scene ):
    global scene
    scene = other_scene

def empty_surface( size ):
    surface = pygame.Surface( size ).convert_alpha()
    surface.fill( (0, 0, 0, 0) )
    return surface
