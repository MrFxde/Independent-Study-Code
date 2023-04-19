import pygame
import numpy as np
import pickle
import time
#TIPS AND TRICKS
#SHIFT + OPTION + DOWN 
#to copy current line down
#OPTION + UP or DOWN
#to move line around

#initizlize pygame and pygame font
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (20,20,20)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

#define frame rate
FPS = 60

WIDTH, HEIGHT = 617, 697

ROWS = COLS = 28

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

button_pressed = False

SGD = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)


