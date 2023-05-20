import pyxel as pxl
import json
WINDOW_HEIGHT = 64
WINDOW_WIDTH = 64

class Frog():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

        self.animation_frame = 0

        with open('versus_animations.json') as f:
            self.animations = json.load(f)
        
        

    def animate(self, animation:dict):
        
        self.u = animation[str(self.animation_frame)]['u']
        self.v = animation[str(self.animation_frame)]['v']
        
        if self.animation_frame < 30:
            self.animation_frame += 1
        else:
            self.animation_frame = 0



    def movement(self):
        if pxl.btn(pxl.KEY_RIGHT) and self.x < WINDOW_WIDTH:
            self.x += 1
        if pxl.btn(pxl.KEY_LEFT) and self.x > 0:
            self.x -= 1
        if pxl.btn(pxl.KEY_DOWN) and self.y < WINDOW_HEIGHT:
            self.y += 1
        if pxl.btn(pxl.KEY_UP) and self.y>0:
            self.y -= 1

    def attack(self):
        pass

    def update(self):
        self.animate()
        self.movement()

    
    def draw(self):
        pxl.blt(self.x,self.y,0,self.u,self.v,16,16)





class Game():
    def __init__(self) -> None:
        pxl.init(WINDOW_WIDTH,WINDOW_HEIGHT,"Versus")
        pxl.load('versus.pyxres')

        self.f = Frog()
        pxl.run(self.update, self.draw)
    def update(self):
        self.f.update()

    def draw(self):
        pxl.cls(0)
        self.f.draw()

Game()