import pyxel

class App():
    def __init__(self):
        pyxel.init( 
            width      = 192,              
            height     = 128,              
            caption    = "ParabolicShot",   
            fps        = 200,              
            fullscreen = False,             
            scale      = 4)   
        pyxel.run(self.update, self.draw)
    def update(self):
        pass
    def draw(self):
        pass