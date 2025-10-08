class Articulo:

    IVA = 0.21
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def getPCVPV(self):
        return (self.price +self.price*Articulo.IVA)
    
    def getPVPDiscount(self, discount):
        return (self.getPCVPV - self.price*discount)
    
    def sell(self, quantity):
        possible = True
        if(self.stock-quantity<0):
            possible = False
            self.stock -= quantity
        return possible
    
    def store(self, quantity):
        self.stock += quantity
    
    
    
