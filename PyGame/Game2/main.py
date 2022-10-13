# Imports externes
from operator import truediv
import pygame as pg
from pygame.locals import *
# Imports internes
from settings import *

pg.init()

class Fenetre:
    '''Generation de la fenetre '''
    def __init__(self,width,height,title):
        
        self.width = width
        self.height = height
        self.caption = title
    
    def build(self):
        pg.display.set_mode((self.width,self.height))
        pg.display.set_caption(self.caption)             # Définir le titre de la fenetre

screen1 = Fenetre(300,300,"screen1")
screen1.build()
screen2 = Fenetre(300,600,"screen2")
screen2.build()
run = True 
while run: #Tant que run = true le jeu marche

    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame



