
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("Labyrinthe")             # Définir le titre de la fenetre 
height = 400
width = 400
screen = pg.display.set_mode((width,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()

laby = [[2, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 3, 1, 0]]

class labyrinthe:
    def __init__(self,tableau:list) -> None:
        
        self.tableau = tableau
        self.x = len(self.tableau[0])
        self.y = len(self.tableau)
    

        








pg.display.flip()
run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
