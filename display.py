from cProfile import run
import sys
from turtle import window_height, window_width
import pygame
from pygame.locals import *
from bynaryTree import treeNodes
from line import line
import time

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
pygame.mixer.music.play(100)

#texto de teclas para recorridos
fuente = pygame.font.SysFont("Arial",20)
texto_teclas_preorder = fuente.render("Presione a -> preorder",0,BLACK,WHITE)
texto_teclas_inorder = fuente.render("Presione w -> inorder",0,BLACK,WHITE)
texto_teclas_postorder = fuente.render("Presione d -> postorder",0,BLACK,WHITE)
texto_teclas_amplitud = fuente.render("Presione s -> amplitud",0,BLACK,WHITE)
texto_teclas_reinicio = fuente.render("Presione espacio -> reiniciar",0,BLACK,WHITE)
#crear una variable que va a mantener el display activo

display_game.fill(BLACK)
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
    tree.add(60,500,60)
    tree.add(41,215,138) 
    tree.add(16,115,245)
    tree.add(25,160,373)
    tree.add(53,314,245)
    tree.add(46,224,373)
    tree.add(42,300,493)
    tree.add(55,384,373)
    tree.add(74,714,138)
    tree.add(65,601,245)
    tree.add(63,491,373)
    tree.add(62,426,493)
    tree.add(64,555,493)
    tree.add(70,680,373)
    
def color_linea (list,color):
    for i in range (len(list)):
        tree.find(list[i],color)
    
index_preorder = 0
index_inorder = 0
index_postorder = 0
index_amplitud = 0

agregar()

container_preorder = tree.preorder()
container_inorder = tree.inorder()
container_postorder = tree.postorder()
container_amplitud = tree.breadth_first_search()

preorder = False
inorder = False
postorder = False
amplitud = False

segundos = 0.5

running = True
while running:
    #la pantalla será visible en todo momento
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_a:
                preorder = True
            elif i.key == K_w:
                inorder = True
            elif i.key == K_d:
                postorder = True
            elif i.key == K_s:
                amplitud = True
            elif i.key == K_SPACE:
                time.sleep(segundos)
                agregar()
                color_linea(container_preorder,GREEN)
                index_preorder = 0
                index_inorder = 0
                index_postorder = 0
                index_amplitud = 0
                preorder = False
                inorder = False
                postorder = False
                amplitud = False
    try:
        if preorder == True:
            tree.find(container_preorder[index_preorder],BLUE)
            index_preorder += 1
            time.sleep(segundos)
        elif inorder == True:
            tree.find(container_inorder[index_inorder],YELLOW)
            index_inorder += 1
            time.sleep(segundos)
        elif postorder == True:
            tree.find(container_postorder[index_postorder],PURPLE)
            index_postorder += 1
            time.sleep(segundos)
        elif amplitud == True:
            tree.find(container_amplitud[index_amplitud],ORANGE)
            index_amplitud += 1
            time.sleep(segundos)
    except IndexError:
        time.sleep(segundos)
        agregar()
        color_linea(container_preorder,GREEN)
        index_preorder = 0
        index_inorder = 0
        index_postorder = 0
        index_amplitud = 0
        preorder = False
        inorder = False
        postorder = False
        amplitud = False
    display_game.blit(texto_teclas_preorder,(10,0))  
    display_game.blit(texto_teclas_inorder,(10,20))
    display_game.blit(texto_teclas_postorder,(10,40))
    display_game.blit(texto_teclas_amplitud,(10,60))
    display_game.blit(texto_teclas_reinicio,(10,80))       
    pygame.display.update()