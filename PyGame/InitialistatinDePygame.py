from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("Game")           # Définir le titre (et une icone(titre,fichier_icone))de la fenetre 
display = pg.display.set_mode((1080,720))  #Dimensions de la fenetre
display.fill([000,000,000])
pg.display.flip


run = True 
while run: #Tant que run = true le jeu marche

    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
