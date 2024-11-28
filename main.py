import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)

while True:
    atualizar()
    desenhar()