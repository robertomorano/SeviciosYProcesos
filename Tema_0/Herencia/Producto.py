class Producto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

        def calculate(self, quantity):
            return self.price*quantity

class Perecedero(Producto):
    def __init__(self, name, price, decay):
        super().__init__(name, price)
        self.decay  = decay
    
    def calculate(self, quantity):
        return super().calculate(self, quantity) / (5-self.decay)


class No_Perecedero(Producto):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type


        