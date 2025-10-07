class CuentaCorriente:
    
    def __init__(self, dni, salary):
        self.__dni = dni
        self.__salary = salary
        self.__name = ""
    
    def __init__(self, dni, name, salary):
        self.__dni = dni
        self.__salary = salary
        self.__name = name
    def __str__(self):
        return f"{self.__name}, con salario {self.__salary}"
    
    def __eq__(self, other):
        equals = False
        if (self.__dni == other.__dni):
            equals = True
        return equals
    def __lt__(self, other):
        res = False
        if(self.__dni < other.__dni):
            res = True
        return res
        
    def sacarDinero():
        pass
    #me da la risa

    def ingresar(increase):
        self.__salary += increase