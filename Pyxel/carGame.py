# https://github.com/kitao/pyxel/blob/main/docs/README.fr.md
import pyxel as pxl
import random as rd
from datetime import time

WINDOW_WIDTH = 64
WINDOW_HEIGHT = 128

class Props:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    
    def resetPos(self):
        self.x = rd.randint(0,WINDOW_WIDTH-8)
        self.y = 0

    def update(self):
        self.y += rd.randint(1,3)

    def draw(self):
        pxl.blt(self.x,self.y,0,0,0,8,8)

class Player:
    def __init__(self) -> None:
        self.x = WINDOW_WIDTH//2-4
        self.y = 3*(WINDOW_HEIGHT//4)-4
        self.velocity = 1

    def movement(self):
        if pxl.btn(pxl.KEY_RIGHT) and self.x < WINDOW_WIDTH-8:
            self.x += self.velocity
        if pxl.btn(pxl.KEY_LEFT) and self.x > 0:
            self.x -= self.velocity

    def update(self):
        self.movement()

    def draw(self):
        pxl.blt(self.x,self.y,0,0,0,8,8,13)

class Game:
    def __init__(self) -> None:
        pxl.init(WINDOW_WIDTH,WINDOW_HEIGHT,"Car Race")
        pxl.load("car.pyxres")
        
        self.player = Player()
        

        self.score = 0

        pxl.run(self.update, self.draw)

    
    def update(self):
        self.player.update()



    def draw(self):
        pxl.cls(0) # Efface le contenu déjà présent
        pxl.bltm(0,0,0,0,0,64,128)
        self.player.draw()


Game()
