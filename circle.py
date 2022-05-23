import pygame
class circle:
    def __init__(self,display,color,value,x,y):
        self.display_game=display
        self.valor=value
        self.color=color
        self.x=x-11
        self.y=y-20
        self.coordenada=x,y
           
    def crear(self):
        textoNodo=str(self.valor)
        BLACK=(0,0,0)
        circulo=pygame.draw.circle(self.display_game,self.color,self.coordenada,30)
        fuente=pygame.font.SysFont("Arial",30)
        texto=fuente.render(textoNodo,0,BLACK)
        self.display_game.blit(texto,(self.x,self.y))