import pyxel
import math

class Pitagoras():
    def __init__(self):
        self.dot = [[pyxel.mouse_x,pyxel.mouse_y],[0,0],[0,0]]
        self.state = False
    def reset(self):
        self.dot = [[pyxel.mouse_x,pyxel.mouse_y],[0,0],[0,0]]
    def update(self):
        self.dot[1] = [pyxel.mouse_x,self.dot[0][1]]
        self.dot[2] = [pyxel.mouse_x,pyxel.mouse_y]
    def CA(self):
        return abs(self.dot[1][0] - self.dot[0][0])
    def CO(self):
        return abs(self.dot[1][1] - self.dot[2][1])
    def H(self):
        return abs(math.sqrt(math.pow(self.CA(),2)+math.pow(self.CO(),2)))
    def draw(self):
        if (self.state): 
            pyxel.line(self.dot[0][0],self.dot[0][1],self.dot[1][0],self.dot[1][1],4)
            pyxel.line(self.dot[0][0],self.dot[0][1],self.dot[2][0],self.dot[2][1],4)
            pyxel.line(self.dot[1][0],self.dot[1][1],self.dot[2][0],self.dot[2][1],4)