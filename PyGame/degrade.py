
from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("Dégradé linéaire")             # Définir le titre de la fenetre 
height = 100
widht = 256
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])



color = 0
for x in range(widht):
    
    pg.draw.line(screen, (color,color,color), [x, 0], [x,100])
    color += 1
    
pg.display.flip()





run = True 
while run: #Tant que run = true le jeu marche

    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
