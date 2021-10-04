import pyxel
import time
class App():
    def __init__(self):
        pyxel.init( 
            width      = 192,              
            height     = 128,              
            caption    = "ParabolicShot",   
            fps        = 60,              
            fullscreen = False,             
            scale      = 4)   
        self.player = {
            "pos" : [0,0],
            "vel" : [5,5]
        }
        self.timeInit = time.time() 
        self.dt = 0
        pyxel.run(self.update, self.draw)
    def update(self):
        self.dt = time.time() - self.timeInit
        if (self.dt >= 0.016):
            self.player["pos"][0] += self.player["vel"][0] * self.dt
            self.player["pos"][1] += self.player["vel"][1] * self.dt
            self.timeInit = time.time()
    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.player["pos"][0],self.player["pos"][1],3,7)
App()   