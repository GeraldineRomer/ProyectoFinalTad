import pygame
class line:
    #crear una linea[donde se dibuja, color, (coorEmpieza x, coorEmpieza y), (coorTermina x, coorTermina y), ancho]
    def __init__(self,display,color,ix,iy,fx,fy):
        self.display = display
        self.line_color = color
        self.ix = ix
        self.iy = iy
        self.fx = fx
        self.fy = fy
        self.coordenada_inicio = self.ix, self.iy
        self.coordenada_final = self.fx, self.fy
        
    def crear (self):
        linea = pygame.draw.line(self.display,self.line_color,self.coordenada_inicio,self.coordenada_final,1)
        
