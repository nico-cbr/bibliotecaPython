# Projeto finalizado  30/11/24 Horario 22:15
#  o placar nao foi colocado devido a dificuldades.

import pygame
from pygame.locals import *
from OpenGL.GL import *

# Declarando variaveis e tamanhos
LARGURA_JANELA = 640
ALTURA_JANELA = 480
pygame.display.set_caption("Jogo Pong")
tempo = pygame.time.Clock();

# declarando variaveis da bola
xDaBola = 0
yDaBola = 0
tamanhoDaBola = 20
raioBola = tamanhoDaBola / 2
velocidadeDaBolaEmX = 5
velocidadeDaBolaEmY = 5

# variaveis da raquete
yDoPlayer1 = 0
yDoPlayer2 = 0

# Placar
meusPontos = 0
pontosOp = 0
# declarando funções de desenho, altura, largura
    
# retangulo (bola)
def vBola():
    global xDaBola, yDaBola
    xDaBola += velocidadeDaBolaEmX
    yDaBola += velocidadeDaBolaEmY

def bolaDesenho():
    desenharRetangulo(xDaBola, yDaBola, tamanhoDaBola, tamanhoDaBola, 1, 1, 0)

# funçoes para players
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

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def movimentoPlayer():
    global xDaBola, yDaBola, yDoPlayer1, yDoPlayer2
    # key do teclado
    keys = pygame.key.get_pressed()

    if keys[K_w]:
        yDoPlayer1 = yDoPlayer1 + 8

    if keys[K_s]:
        yDoPlayer1 = yDoPlayer1 - 8

    if keys[K_i]:
        yDoPlayer2 = yDoPlayer2 + 8

    if keys[K_k]:
        yDoPlayer2 = yDoPlayer2 - 8

        # Prevenir que as raquetes saiam da tela
    if yDoPlayer1 + alturaDosPlayers() / 2 > ALTURA_JANELA / 2:
        yDoPlayer1 = ALTURA_JANELA / 2 - alturaDosPlayers() / 2
    if yDoPlayer1 - alturaDosPlayers() / 2 < -ALTURA_JANELA / 2:
        yDoPlayer1 = -ALTURA_JANELA / 2 + alturaDosPlayers() / 2

    if yDoPlayer2 + alturaDosPlayers() / 2 > ALTURA_JANELA / 2:
        yDoPlayer2 = ALTURA_JANELA / 2 - alturaDosPlayers() / 2
    if yDoPlayer2 - alturaDosPlayers() / 2 < -ALTURA_JANELA / 2:
        yDoPlayer2 = -ALTURA_JANELA / 2 + alturaDosPlayers() / 2

# funçoes para funcionamento do game
# def atualizarPlacar():
    
# def desenharPlacar():
#     fonte = pygame.font.Font(None, 36)
#     texto = f"Player 1: {meusPontos}  |  Player 2: {pontosOp}"
#     textoSurface = fonte.render(texto, True, (255, 255, 255), (0, 0, 0))
#     textoData = pygame.image.tostring(textoSurface, "RGB", True)
#     glWindowPos2d(LARGURA_JANELA // 2 - 200, ALTURA_JANELA - 40)
#     glDrawPixels(textoSurface.get_width(), textoSurface.get_height(), GL_RGB, GL_UNSIGNED_BYTE, textoData)


def verificarColisao():
    global xDaBola, yDaBola, velocidadeDaBolaEmX, velocidadeDaBolaEmY, yDoPlayer1, yDoPlayer2, meusPontos, pontosOp
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
                # Atualizando pontos quando a bola sai da tela
    if xDaBola < -LARGURA_JANELA / 2:
        pontosOp += 1
        # atualizarPlacar()
        xDaBola, yDaBola = 0, 0

    if xDaBola > LARGURA_JANELA / 2:
        meusPontos += 1
        # atualizarPlacar()
        xDaBola, yDaBola = 0, 0


# funçoes para o laço while
def atualizar():

    vBola()
    verificarColisao()
    movimentoPlayer()

# desenhando players

def desenhar():
    glViewport(0, 0, LARGURA_JANELA, ALTURA_JANELA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-LARGURA_JANELA / 2, LARGURA_JANELA / 2, -ALTURA_JANELA / 2, ALTURA_JANELA / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)
    
    bolaDesenho()
    p1Desenho()
    p2Desenho()
    # desenharPlacar()
    
    pygame.display.flip()

pygame.init()
pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA), DOUBLEBUF | OPENGL)
# atualizarPlacar()

# Laço para rodar jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
    tempo.tick(60)
    atualizar()
    desenhar()


pygame.quit()