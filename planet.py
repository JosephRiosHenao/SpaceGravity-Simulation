import pyxel
import mathGravity

VELOCITY = 1

class Planet():
    def __init__(self,r,m,pos):
        self.m = m
        self.r = r
        self.orbitStrength = m*r
        self.planetObjectLink = []
        self.planetPitagorasLink = []
        if (self.orbitStrength > (r*4)): self.orbitStrength = r*4
        self.pos = pos
        
    def update():
        pass
        
    def draw(self):
        pyxel.circ(self.pos[0], self.pos[1], self.r, 4)
        pyxel.circb(self.pos[0], self.pos[1], self.orbitStrength, 4)
        
    def detectOrbit(self,planet):
        self.planetObjectLink.append(planet)
        dx = self.pos[0] - planet.pos[0]
        dy = self.pos[1] - planet.pos[1]
        distance = mathGravity.distanceCircles(dx,dy)
        if(distance < self.orbitStrength + planet.orbitStrenght): pass
        