import pyxel

class Mouse():
    def __init__(self):
        self.pos = [0,0]
    def update(self):
        self.pos = [pyxel.mouse_x, pyxel.mouse_y]
    def draw(self):
        pyxel.pset(self.pos[0],self.pos[1],2)
        
        