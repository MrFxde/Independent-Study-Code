#in init.py import everything from settings
#* means import everything
#dot? it is a relevant import, 
from .settings import *
import pygame
from .button import Button
#TIPS AND TRICKS
#SHIFT + OPTION + DOWN 
#to copy current line down
#OPTION + UP or DOWN
#to move line around

#initizlize pygame and pygame font
pygame.init()
pygame.font.init()