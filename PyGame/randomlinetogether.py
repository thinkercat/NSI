from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
pg.display.set_caption("Ligne aleatoire")             # Définir le titre de la fenetre 
height = 300
widht = 300
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()

randomPointA = [random.randint(0,300),random.randint(0,300)]


for tours in range(9):

    randomPointB = [random.randint(0,300),random.randint(0,300)]
    randomcolor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
    line = pg.draw.line(screen, (randomcolor[0],randomcolor[1],randomcolor[2]),randomPointA,randomPointB,5)
    
    
    print("\nLIGNE",tours,"\nPoint A =",randomPointA,"\nPoint B =",randomPointB,"\nCouleur =",randomcolor[0],randomcolor[1],randomcolor[2])
    randomPointA = randomPointB
    print(randomPointA, randomPointB)
    print(line)
pg.display.flip()




run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame