
from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("Cadrillage 20px")             # Définir le titre de la fenetre 
height = 300
widht = 300
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()

PointA = [0,0]
PointB = [0,height]
for i in range(0,height//20+1):   
    pg.draw.line(screen,(0,99,99),PointA,PointB,3)
    PointA[0] += 20
    PointB[0] += 20


PointA = [0,0]
PointB = [widht,0]
for i in range(0,widht//20+1):   
    pg.draw.line(screen,(0,99,99),PointA,PointB,3)
    PointA[1] += 20
    PointB[1] += 20


pg.display.flip()



run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
