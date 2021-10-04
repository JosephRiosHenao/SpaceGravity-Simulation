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
        self.planets = [
            {
            "pos" : [48,64],
            "vel" : [0,0],
            "a" : [0,0],
            "m" : 0.000001
            },
            {
            "pos" : [96,64],
            "vel" : [0,0],
            "a" : [0,0],
            "m" : 10000
            },
            # {
            # "pos" : [130,64],
            # "vel" : [0,0],
            # "a" : [0,0],
            # "m" : 0
            # }
            ]
        self.last_time = time.time()
        pyxel.run(self.update, self.draw)
    def update(self):
        self.dt = time.time() - self.last_time
        if (self.dt >= 0.016):
            for i, planet in enumerate(self.planets): 
                for j, planetPos in enumerate(self.planets):
                    if(j==i): continue 
                    dx = math.pow(planet["pos"][0] - planetPos["pos"][0],2) 
                    dy = math.pow(planet["pos"][1] - planetPos["pos"][1],2)
                    # print(str(dx)+" "+str(dy) )
                    planet["a"][0] = planetPos["m"] / dx 
                    planet["a"][1] = planetPos["m"] / dy 
                    
                planet["vel"][0] += planet["a"][0] * self.dt
                planet["vel"][1] += planet["a"][1] * self.dt
                planet["pos"][0] += planet["vel"][0] * self.dt
                planet["pos"][1] += planet["vel"][1] * self.dt
                # print(planet)
                self.last_time = time.time()
        
    def draw(self):
        pyxel.cls(0)
        for planet in self.planets:
            pyxel.circ(planet["pos"][0], planet["pos"][1], 5, 7)
App()