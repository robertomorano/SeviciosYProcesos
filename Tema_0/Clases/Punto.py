import math


class Punto:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def setXY (self, otherX, otherY):
        self.x = otherX
        self.y = otherY
    
    def moveXY (self, otherX, otherY):
        self.x += otherX
        self.y += otherY

    def distance(self, other):
        return math.sqrt(math.pow(other.x)-math.pow(self.x) + math.pow(other.y)-math.pow(self.y))
        
