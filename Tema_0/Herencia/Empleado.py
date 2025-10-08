class Empleado:

    def __init__(self, name = ""):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def __str__(self):
        return f"Empleado {self.name}"
class Operario(Empleado):
    def __str__(self):
        return f"{super().__str__()} -< Operario"

class Tecnico(Operario):
    def __str__(self):
        return f"{super().__str__()} -< Tecnico"

class Oficial(Operario):
    def __str__(self):
        return f"{super().__str__()} -< Oficial"

class Directivo(Empleado):
    def __str__(self):
        return f"{super().__str__()} -< Directivo"


