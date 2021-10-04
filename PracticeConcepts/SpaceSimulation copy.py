import pyxel
import time
import math

class App():
    def __init__(self):
        pyxel.init( 
            width      = 192,              
            height     = 128,              
            caption    = "ParabolicShot",   
            fps        = 60,              
            fullscreen = False,             
            scale      = 4) 
        self.planet1 = {
            "pos" : [130,64],
            "vel" : [0,0],
            "a" : [0,0],
            "m" : 5
            }
        self.planet2 = {
            "pos" : [96,60],
            "vel" : [1,0],
            "a" : [0,0],
            "m" : 10
            }
        self.last_time = time.time()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.dt = time.time() - self.last_time
        if (self.dt >= 0.016):
            self.planet1["pos"][0] += self.planet1["vel"][0] * self.dt
            self.planet1["pos"][1] += self.planet1["vel"][1] * self.dt
            dx = math.pow(self.planet1["pos"][0] - self.planet2["pos"][0],2) 
            dy = math.pow(self.planet1["pos"][1] - self.planet2["pos"][1],2)
            self.planet1["a"][0] = self.planet2["m"] / dx *-1
            self.planet1["a"][1] = self.planet2["m"] / dy *-1
            self.planet1["vel"][0] += self.planet1["a"][0] * self.dt
            self.planet1["vel"][1] += self.planet1["a"][1] * self.dt
            # print(dy)
            # print(planet)
            self.last_time = time.time()
        
    def draw(self):
        pyxel.cls(0)
        
        pyxel.circ(self.planet1["pos"][0], self.planet1["pos"][1], 2, 7)
        pyxel.circ(self.planet2["pos"][0], self.planet2["pos"][1], 5, 7)
App()