import math

def accelerationNormal(v,r): 
    return (math.pow(v,2)/r)

def forceNormal(m,a):
    return m*a

def distanceCircles(dx,dy):
    return math.sqrt(dx*dx + dy*dy)