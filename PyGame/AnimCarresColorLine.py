
from operator import truediv
from turtle import position
import pygame as pg
from pygame.locals import *
import random

pg.init()

# Génération de la fenetre
pg.display.set_caption("ColorLine")             # Définir le titre de la fenetre 
height = 50
widht = 50*20
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()




run = True 
while run: #Tant que run = true le jeu marche
    

    rectangle = [0,0,50,50] # [position de la gauche, position du haut, largeur, hauteur] => "Rect" type from pygame


    for carres in range(20):

        color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
        pg.draw.rect(screen,(color),(rectangle))
        rectangle[0] += 50
        pg.display.flip()
        pg.time.delay(250)    
    
    
    
    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
