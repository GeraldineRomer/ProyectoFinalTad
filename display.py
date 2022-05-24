from cProfile import run
import sys
from turtle import window_height, window_width
import pygame
from pygame.locals import *
from bynaryTree import treeNodes
from line import line

#inicializar el módulo pygame
pygame.init()
#crear dimensiones del display
window_width = 1000
window_height = 600
#crear variable que recibe el ancho y el alto establecido en la pantalla
display_game = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Árboles Binarios: Geraldine Urrea Romero")

'''Código binario (R,G,B)'''
PINK = (238, 206, 231 )
BLACK = (0,0,0)
WHITE = (252, 252, 252)
GREEN = (149, 243, 108)
BLUE = (10, 233, 243)
YELLOW = (243, 240, 10)
RED = (244, 27, 10)
BROWN = (131, 117, 87)
PURPLE = (148, 82, 222)
ORANGE = (236, 145, 5)

#sonido
pygame.mixer.music. load("./assets/audio/music.wav")
pygame.mixer.music.play(3)

#texto de teclas para recorridos
fuente = pygame.font.SysFont("Arial",20)
texto_teclas_preorder = fuente.render("Presione a -> preorder",0,BLACK,WHITE)
texto_teclas_inorder = fuente.render("Presione w -> inorder",0,BLACK,WHITE)
texto_teclas_postorder = fuente.render("Presione d -> postorder",0,BLACK,WHITE)
texto_teclas_amplitud = fuente.render("Presione s -> amplitud",0,BLACK,WHITE)
texto_teclas_reinicio = fuente.render("Presione espacio -> reiniciar",0,BLACK,WHITE)
#crear una variable que va a mantener el display activo

display_game.fill(PINK)
tree = treeNodes(display_game)

#crear una linea[donde se dibuja, color, (coorEmpieza x, coorEmpieza y), (coorTermina x, coorTermina y), ancho]
'''pygame.draw.line(display_game,BROWN,(480,51),(326,144),10)
pygame.draw.line(display_game,BROWN,(326,144),(200,248),10)
pygame.draw.line(display_game,BROWN,(326,144),(356,261),10)
pygame.draw.line(display_game,BROWN,(200,248),(221,346),10)
pygame.draw.line(display_game,BROWN,(356,261),(431,346),10)
pygame.draw.line(display_game,BROWN,(356,261),(318,346),10)
pygame.draw.line(display_game,BROWN,(318,346),(300,443),10)
pygame.draw.line(display_game,BROWN,(480,51),(657,140),10)
pygame.draw.line(display_game,BROWN,(623,231),(657,140),10)
pygame.draw.line(display_game,BROWN,(623,231),(570,304),10)
pygame.draw.line(display_game,BROWN,(623,231),(718,301),10)
pygame.draw.line(display_game,BROWN,(570,304),(525,387),10)
pygame.draw.line(display_game,BROWN,(570,304),(604,397),10)'''

def agregar ():
    #crear un circulo[lugar,color,(puntoCentral x, puntoCentral y),radio]
    tree.add(60,480,51,480,51,319,137)
    tree.add(41,326,144,326,144,200,248)
    tree.add(16,200,248,326,174,356,261)
    tree.add(25,221,346,200,278,221,346)
    tree.add(53,356,261,356,261,431,346)
    tree.add(46,318,346,356,291,318,346)
    tree.add(42,300,443,318,376,300,443)
    tree.add(55,431,346,510,51,657,140)
    tree.add(74,657,140,623,231,657,140)
    tree.add(65,623,231,623,231,570,304)
    tree.add(63,570,304,650,241,718,301)
    tree.add(62,525,387,560,330,525,387)
    tree.add(64,604,397,580,330,604,397)
    tree.add(70,718,301,0,0,0,0)

index_preorder = 0
index_inorder = 0
index_postorder = 0
index_amplitud = 0

agregar()
running = True
while running:
    #la pantalla será visible en todo momento
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            try:
                if i.key == K_a:
                    container_preorder = tree.preorder()
                    tree.find(container_preorder[index_preorder],BLUE)
                    index_preorder += 1
                elif i.key == K_w:
                    container_inorder = tree.inorder()
                    tree.find(container_inorder[index_inorder],YELLOW)
                    index_inorder += 1
                elif i.key == K_d:
                    container_postorder = tree.postorder()
                    tree.find(container_postorder[index_postorder],PURPLE)
                    index_postorder += 1
                elif i.key == K_s:
                    container_amplitud = tree.breadth_first_search()
                    tree.find(container_amplitud[index_amplitud],ORANGE)
                    index_amplitud += 1
                elif i.key == K_SPACE:
                    agregar()
                    index_preorder = 0
                    index_inorder = 0
                    index_postorder = 0
                    index_amplitud = 0
            except IndexError:
                agregar()
                index_preorder = 0
                index_inorder = 0
                index_postorder = 0
                index_amplitud = 0
    display_game.blit(texto_teclas_preorder,(10,0))  
    display_game.blit(texto_teclas_inorder,(10,20))
    display_game.blit(texto_teclas_postorder,(10,40))
    display_game.blit(texto_teclas_amplitud,(10,60))
    display_game.blit(texto_teclas_reinicio,(10,80))       
    pygame.display.update()
    