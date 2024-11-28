import pygame
from pygame.locals import *
from OpenGL.GL import *

# Declarando variaveis e tamanhos
LARGURA_JANELA = 640
ALTURA_JANELA = 480

xDaBola = 0
yDaBola = 0
tamanhoDaBola = 20
velocidadeDaBolaEmX = 0.05
velocidadeDaBolaEmY = 0.05

yDoPlayer1 = 0
yDoPlayer2 = 0

# declarando funções de desenho, altura, largura
def bolaDesenho():
    desenharRetangulo(xDaBola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 1, 0)

def p1Desenho():
    desenharRetangulo(xDoPlayer1(), yDoPlayer1, larguraDosPlayers(), alturaDosPlayers(), 1, 0, 0)
    
def p2Desenho():
    desenharRetangulo(xDoPlayer2(), yDoPlayer2, larguraDosPlayers(), alturaDosPlayers(), 0, 0, 1)

def xDoPlayer1():
    return -LARGURA_JANELA / 2 + larguraDosPlayers() / 2

def xDoPlayer2():
    return LARGURA_JANELA / 2 - larguraDosPlayers() / 2

def larguraDosPlayers():
    return tamanhoDaBola

def alturaDosPlayers():
    return 3 * tamanhoDaBola

# funçoes para o laço while
def atualizar():
    global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoPlayer1, yDoPlayer2

    xDaBola = xDaBola + velocidadeDaBolaEmX
    yDaBola = yDaBola + velocidadeDaBolaEmY

    if (xDaBola + tamanhoDaBola / 2 > xDoPlayer2() - larguraDosPlayers() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoPlayer2 + alturaDosPlayers() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoPlayer2 - alturaDosPlayers() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if (xDaBola - tamanhoDaBola / 2 < xDoPlayer1() + larguraDosPlayers() / 2
    and yDaBola - tamanhoDaBola / 2 < yDoPlayer1 + alturaDosPlayers() / 2
    and yDaBola + tamanhoDaBola / 2 > yDoPlayer1 - alturaDosPlayers() / 2):
        velocidadeDaBolaEmX = -velocidadeDaBolaEmX

    if yDaBola + tamanhoDaBola / 2 > ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if yDaBola - tamanhoDaBola / 2 < -ALTURA_JANELA / 2:
        velocidadeDaBolaEmY = -velocidadeDaBolaEmY

    if xDaBola < -LARGURA_JANELA / 2 or xDaBola > LARGURA_JANELA / 2:
        xDaBola = 0
        yDaBola = 0

# key do teclado
    keys = pygame.key.get_pressed()

    if keys[K_w]:
        yDoPlayer1 = yDoPlayer1 + .2

    if keys[K_s]:
        yDoPlayer1 = yDoPlayer1 - .2

    if keys[K_i]:
        yDoPlayer2 = yDoPlayer2 + .2

    if keys[K_k]:
        yDoPlayer2 = yDoPlayer2 - .2

# desenhando players (IMPLEMENTAR COLISÃO DE BORDAS DOS PADDLES)
def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)
    
    bolaDesenho()
    p1Desenho()
    p2Desenho()
    
    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)

# Laço para rodar jogo
while True:
    atualizar()
    desenhar()
    pygame.event.pump()