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
        pyxel.mouse(True)
        self.planet1 = {
            "pos" : [30,0],
            "vel" : [0,0.56],
            "a" : [0,0],
            "m" : 0.000001
            }
        self.planet2 = {
            "pos" : [0,0],
            "vel" : [0,0],
            "a" : [0,0],
            "m" : 10
            }
        self.last_time = time.time()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        # self.dt = time.time() - self.last_time
        self.dt = 1
        # if (self.dt >= 0.016):
            # dx = math.pow(self.planet2["pos"][0] - self.planet1["pos"][0] ,2)
            # dy = math.pow(self.planet2["pos"][1] - self.planet1["pos"][1] ,2)
            # dx = dx * -1 if self.planet2["pos"][0] - self.planet1["pos"][0] <= 0 else dx
            # dy = dy * -1 if self.planet2["pos"][1] - self.planet1["pos"][1] <= 0 else dy
        dx = self.planet2["pos"][0] - self.planet1["pos"][0]
        dy = self.planet2["pos"][1] - self.planet1["pos"][1]
        
        d2 = math.pow(dx,2) + math.pow(dy,2)
        
        d = math.sqrt(math.pow(self.planet2["pos"][0] - self.planet1["pos"][0],2) + math.pow(self.planet2["pos"][1] - self.planet1["pos"][1],2))
                    
        ux = dx/d
        uy = dy/d
        
        a1 = 1 * self.planet2["m"] / d2
        a2 = 1 * self.planet1["m"] / d2
        
        self.planet1["a"][0] = ux * a1
        self.planet1["a"][1] = uy * a1
        
        self.planet1["pos"][0] += self.planet1["vel"][0] * self.dt
        self.planet1["pos"][1] += self.planet1["vel"][1] * self.dt
        
        self.planet1["vel"][0] += self.planet1["a"][0] * self.dt
        self.planet1["vel"][1] += self.planet1["a"][1] * self.dt
        
        # print("A:"+str(self.planet1["a"])+" V:"+str(self.planet1["vel"])+" P:"+str(self.planet1["pos"]))
        # self.last_time = time.time()
        
    def draw(self):
        pyxel.cls(0)
        
        pyxel.circ(self.planet1["pos"][0]+96, 64-self.planet1["pos"][1], 2, 7)
        if (self.planet2["pos"][1]>=0):
            pyxel.circ(self.planet2["pos"][0]+96, 64-self.planet2["pos"][1], 5, 7)
        else:
            pyxel.circ(self.planet2["pos"][0]+96, 64+self.planet2["pos"][1], 5, 7)
App()