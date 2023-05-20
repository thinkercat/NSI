# https://github.com/kitao/pyxel/blob/main/docs/README.fr.md
import pyxel as pxl
import random as rd

WINDOW_WIDTH = 140
WINDOW_HEIGHT = 130

class Props:
    def __init__(self) -> None:
        self.x = rd.randint(0,WINDOW_WIDTH-8)
        self.y = rd.randint(0,WINDOW_HEIGHT-8)
    
    def resetPos(self):
        self.x = rd.randint(0,WINDOW_WIDTH-8)
        self.y = rd.randint(0,WINDOW_HEIGHT-8)

    def update(self):

        self.x += rd.randint(-1,1)
        self.y += rd.randint(-1,1)
        
        if self.x >= WINDOW_WIDTH-8:
            self.x -= 1
        elif self.x <= 0:
            self.x += 1
        if self.y >= WINDOW_HEIGHT-8:
            self.y -= 1
        elif self.y <= 0:
            self.y += 1


    def draw(self):
        pxl.blt(self.x,self.y,0,0,0,8,8)

class Player:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.velocity = 2

    def movement(self):
        if pxl.btn(pxl.KEY_RIGHT) and self.x < WINDOW_WIDTH:
            self.x += self.velocity
        if pxl.btn(pxl.KEY_LEFT) and self.x > 0:
            self.x -= self.velocity
        if pxl.btn(pxl.KEY_DOWN) and self.y < WINDOW_HEIGHT:
            self.y += self.velocity
        if pxl.btn(pxl.KEY_UP) and self.y>0:
            self.y -= self.velocity

    def update(self):
        self.movement()

    def draw(self):
        pxl.blt(self.x,self.y,0,8,0,8,8)

class Game:
    def __init__(self) -> None:
        pxl.init(WINDOW_WIDTH,WINDOW_HEIGHT,"Game title")
        pxl.load("res.pyxres")
        
        self.player = Player()
        self.props01 = Props()



        self.score = 0

        pxl.run(self.update, self.draw)

    def schowScore(self):
        f_score = f'{self.score}'
        pxl.text(1,1,f_score,6)

    def isEat(self):
        if self.props01.x >= self.player.x and self.props01.x <= self.player.x+8 and self.props01.y >= self.player.y and self.props01.y <= self.player.y+8:
            self.score += 1
            self.props01.resetPos()

    def update(self):
        self.props01.update()
        self.player.update()
        self.isEat()


    def draw(self):
        pxl.cls(0) # Efface le contenu déjà présent
        self.props01.draw()
        self.player.draw()
        self.schowScore()

Game()
