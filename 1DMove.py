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
            "pos" : [0,90],
            "v" : [30,0], 
            "a" : [0,0], 
        }        
        self.player2 = {
            "pos" : [0,60],
            "v" : [30,0], 
            "a" : [0,0], 
        }
        self.player3 = {
            "pos" : [0,30],
            "v" : [30,0], 
            "a" : [0,0], 
        }
        self.timeInit = time.time()
        self.dt = 0
        self.timeInit2 = time.time()
        self.dt2 = 0
        self.timeInit3 = time.time()
        self.dt3 = 0
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.dt = time.time() - self.timeInit
        if (self.dt >= 0.016):
            self.player["pos"][0] = self.player["pos"][0] + self.player["v"][0] * self.dt 
            self.timeInit = time.time()
            
        self.dt2 = time.time() - self.timeInit2
        if (self.dt2 >= 0.25):
            self.player2["pos"][0] = self.player2["pos"][0] + self.player2["v"][0] * self.dt2
            self.timeInit2 = time.time()
        
        self.dt3 = time.time() - self.timeInit3
        if (self.dt3 >= 1):
            self.player3["pos"][0] = self.player3["pos"][0] + self.player3["v"][0] * self.dt3
            self.timeInit3 = time.time()
            
    def draw(self):
        pyxel.cls(0)
        pyxel.pset(self.player["pos"][0],self.player["pos"][1],5)
        pyxel.pset(self.player2["pos"][0],self.player2["pos"][1],5)
        pyxel.pset(self.player3["pos"][0],self.player3["pos"][1],5)

App()