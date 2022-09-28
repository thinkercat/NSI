
from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
pg.display.set_caption("Random Color Circle")             # Définir le titre de la fenetre 
height = 300
widht = 300
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()


for circle in range(100):
   
    randomRadius = random.randint(10,50)
    circleCenter = [random.randint(0+randomRadius,300-randomRadius),random.randint(0+randomRadius,300-randomRadius)]

    color = [random.randint(0,255),random.randint(0,255),random.randint(0,255),]

    pg.draw.circle(screen, (color), circleCenter, randomRadius)

pg.display.flip()


run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
