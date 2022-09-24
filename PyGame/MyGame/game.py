from operator import truediv
import pygame as pg
from pygame.locals import *
import random

pg.init()



# Génération de la fenetre
icon = pg.image.load('NSI\PyGame\MyGame\Assets\gameboy_icon.png')
dish = pg.image.load('NSI\PyGame\MyGame\Assets\dish.png')
strawberrycake_dish = pg.image.load('NSI\PyGame\MyGame\Assets\strawberrycake_dish.png')
strawberrycake = pg.image.load('NSI\PyGame\MyGame\Assets\strawberrycake.png')

pg.display.set_icon(icon)
pg.display.set_caption("Game")             # Définir le titre de la fenetre 
height = 720
widht = 1080
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre



pg.mixer.music.load('NSI\PyGame\MyGame\Assets\Musiques\chill.mp3')
pg.mixer.music.play(loops = -1)



cakePos = (0,0)
def cake():
    RandomX = random.randint(10,1070)
    RandomY = random.randint(10,760) 
    global cakePos 
    cakePos= (RandomX,RandomY)
    screen.blit(strawberrycake, cakePos)   


    
    

run = True 
while run: #Tant que run = true le jeu marche
    screen.fill([221, 190, 169])
    
    MousePosition = pg.mouse.get_pos()
    screen.blit(dish,MousePosition)
    
    if cakePos == MousePosition :
        cake()
    
    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
    pg.display.flip()
