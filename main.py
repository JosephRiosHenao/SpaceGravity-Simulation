from planet import Planet
from pitagoras import Pitagoras
import pyxel
import mouse
import pitagoras

planets = []

class App():
    def __init__(self):
        pyxel.init( 
            width      = 192,              
            height     = 128,              
            caption    = "ParabolicShot",   
            fps        = 200,              
            fullscreen = False,             
            scale      = 4)   
        self.mouse = mouse.Mouse()
        self.pitagoras = pitagoras.Pitagoras()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.keybinding()
        self.mouse.update()
        self.pitagoras.update()
        for planet in planets: 
            for planetPos in planets:
                planet.detectOrbit(planetPos.pos, planetPos.orbitStrength)
        
    def draw(self):
        pyxel.cls(0)
        self.mouse.draw()
        self.pitagoras.draw()
        for planet in planets: planet.draw()
        
    def keybinding(self):
        if (pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON)): 
            self.pitagoras.reset() 
            self.pitagoras.state = True
        if (self.pitagoras.state and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): 
            self.pitagoras.state = False
            planets.append(Planet(self.pitagoras.CA(), self.pitagoras.H(), self.pitagoras.dot[0]))
        if (pyxel.btnp(pyxel.KEY_SPACE)): print(self.pitagoras.H())

App()