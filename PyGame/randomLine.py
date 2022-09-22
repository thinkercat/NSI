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



for tours in range(10):

    randomx = [random.randint(0,300),random.randint(0,300)]
    randomy = [random.randint(0,300),random.randint(0,300)]
    randomcolor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

    pg.draw.line(screen, (randomcolor[0],randomcolor[1],randomcolor[2]),[randomx[0],randomy[0]],[randomx[1],randomy[1]],5)
    print("LIGNE",tours,"\nX =",randomx[0],randomx[1],"\nY =",randomy[0],randomy[1],"\nCouleur =",randomcolor[0],randomcolor[1],randomcolor[2],"\n")

pg.display.flip()




run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame