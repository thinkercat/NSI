
from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
pg.display.set_caption("Damier")             # Définir le titre de la fenetre 
height = 600
width = 600
screen = pg.display.set_mode((width,height))   #Dimensions de la fenetre
screen.fill([000,000,000])

nb_cases = 8
color = [0,0,0]
rectangle = [0,0,width//nb_cases,height//nb_cases] # [position de la gauche, position du haut, largeur, hauteur] => "Rect" type from pygame
colorn=0
for verticalsLines in range(nb_cases):
    
    for carresPerLine in range( nb_cases):
    

        if colorn%2 == 0:
            color = [255,255,255]
        else:
            color = [0,0,0]

        pg.draw.rect(screen,(color),(rectangle))
        rectangle[0] += width//nb_cases
        colorn+=1

    rectangle[0] = 0
    rectangle[1] += width//nb_cases
    colorn+= 1






pg.display.flip()
run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
