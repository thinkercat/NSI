from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("(⊙o⊙)")             # Définir le titre de la fenetre 
height = 300
widht = 300
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()

color1 = [181, 151, 246]
color2 = [150, 198, 234]
circleCenter = [widht/2,height/2]
circleRadius = (widht-20)/2
circleWidht = 8

for circle in range(1000):
    pg.draw.circle(screen,color1,circleCenter,circleRadius)
    pg.draw.circle(screen,color2,circleCenter,circleRadius-circleWidht)
    circleRadius -= circleWidht*2

pg.display.flip()


run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
