import pyxel
import mathGravity

class Planet():
    def __init__(self,r,m,pos):
        self.m = m
        self.r = r
        self.orbitStrength = m*r
        self.planetIndexLink = []
        if (self.orbitStrength > (r*4)): self.orbitStrength = r*4
        self.pos = pos
    def draw(self):
        pyxel.circ(self.pos[0], self.pos[1], self.r, 4)
        pyxel.circb(self.pos[0], self.pos[1], self.orbitStrength, 4)
    def detectOrbit(self,pos,orbit):
        dx = self.pos[0] - pos[0]
        dy = self.pos[1] - pos[1]
        distance = mathGravity.distanceCircles(dx,dy)
        if(distance < self.orbitStrength + orbit): print ("detectado")