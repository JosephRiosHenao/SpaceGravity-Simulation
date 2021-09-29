import pyxel
import mathGravity

class Planet():
    def __init__(self,r,m,pos):
        self.m = m
        self.r = r
        self.orbitStrength = (m * r)
        self.pos = pos
    def draw(self):
        pyxel.circ(self.pos[0], self.pos[1], self.r, 4)
        pyxel.circb(self.pos[0], self.pos[1], self.orbitStrength, 4)
    def detectOrbit(self,pos,orbit):
        pass