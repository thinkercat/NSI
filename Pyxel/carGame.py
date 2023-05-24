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
        self.velocity = rd.randint(1,3
                                   )
        self.resetPos()
    
    def resetPos(self):
        self.x = rd.randint(0,WINDOW_WIDTH-8)
        self.velocity = rd.randint(1,2)
        self.y = 0

    def update(self):
        self.y += self.velocity

    def draw(self):
        pxl.blt(self.x,self.y,0,16,0,8,8,13)

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
        self.props = []

        self.nbProps = 5
        for e in range(self.nbProps):
            self.props.append(Props())

        self.score = 0

        pxl.run(self.update, self.draw)

    def propsGeneration(self):
        for i in self.props:
            if i.y > WINDOW_HEIGHT:
                i.resetPos()


    def update(self):
        print(self.props)
        self.player.update()
        for i in self.props:
            i.update()
        self.propsGeneration()


    def draw(self):
        pxl.cls(0) # Efface le contenu déjà présent
        pxl.bltm(0,0,0,0,0,64,128)
        self.player.draw()
        for i in self.props:
            i.draw()


Game()
