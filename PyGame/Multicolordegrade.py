
from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("(。_。)")             # Définir le titre de la fenetre 
height = 256
widht = 256
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()

pointA = [0,0]
pointB = [0,0]
color = [0,0,0]

for line in range(256):
    pointA[0] = 0
    pointB[0] = 0
    color[0] = 0
    for pixelPerLine in range(256):
        pg.draw.line(screen, (color),pointA,pointB)

        pointA[0] += 1
        pointB[0] += 1

        if color[0] < 255:
            color[0] += 1
        else:
            color[0] = 255

    if color[1] < 255:
        color[1] += 1
    else:
        color[1] += 1

    pointA[1] += 1
    pointB[1] += 1
        


pg.display.flip()


run = True 
while run: #Tant que run = true le jeu marche

    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
