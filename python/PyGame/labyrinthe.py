
import pygame as pg
from pygame.locals import *

laby = [[2, 1, 0, 0, 0, 1, 1, 1, 1, 1], 
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [1, 3, 1, 1, 0, 0, 0, 1, 1, 1]]



pg.init()


# Génération de la fenetre
pg.display.set_caption("Labyrinthe")             # Définir le titre de la fenetre 
height = 600
width = 600
screen = pg.display.set_mode((width,height))   #Dimensions de la fenetre
screen.fill([000,000,000])
pg.display.flip()



class labyrinthe:
    def __init__(self,tableau:list) -> None:
        
        self.tableau = tableau
        self.x = len(self.tableau[0])
        self.y = len(self.tableau)

                        # [x, y,     width       ,      height ]
        self.squareSize = [0, 0, width//self.x, width//self.x]

    def generate(self):
        x = 10
        y = 10




    def draw(self):

        for y in self.tableau:
            
            for x in y:
                
                if x == 0:
                    color = [255,255,255]
                elif x == 1:
                    color = [0,0,0]
                elif x == 2 :
                    color = [0,255,0]
                elif x == 3:
                    color = [255,0,0]
                else:
                    color = [0,0,255]

                pg.draw.rect(screen,(color),(self.squareSize))
                self.squareSize[0] += width//self.x
                print(x)
            self.squareSize[1] += width//self.x
            self.squareSize[0] = 0

lab = labyrinthe(laby) 

        








pg.display.flip()
run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
