from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
icon = pg.image.load('NSI\PyGame\MyGame\Assets\gameboy_icon.png')
pg.display.set_icon(icon)
pg.display.set_caption("Game")             # Définir le titre de la fenetre 
height = 720
widht = 1080
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()

pg.mixer.music.load('NSI\PyGame\MyGame\Assets\Musiques\chill.mp3')
pg.mixer.music.play(loops = -1)


run = True 
while run: #Tant que run = true le jeu marche

    MousePosition = pg.mouse.get_pos()
    


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame

