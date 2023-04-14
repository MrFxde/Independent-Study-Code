import pygame
#TIPS AND TRICKS
#SHIFT + OPTION + DOWN 
#to copy current line down
#OPTION + UP or DOWN
#to move line around

#initizlize pygame and pygame font
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

#define frame rate
FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)


