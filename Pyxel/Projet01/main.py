import pyxel


class Game:
    def __init__(self):
        pyxel.caption("My Game Title")
    
    def update(self):
        pass
    def draw(self):
        pyxel.cls(0)
Game()