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
        
    def draw(self):
        pyxel.cls(0)
        self.mouse.draw()
        self.pitagoras.draw()
        
    def keybinding(self):
        if (pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON)): 
            self.pitagoras.reset() 
            self.pitagoras.state = True
        if (self.pitagoras.state and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)): self.pitagoras.state = False
App()