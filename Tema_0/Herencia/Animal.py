class Animal:
    def __init__(self, nombre, num_patas):
        self.nombre = nombre
        self.num_patas = num_patas

    def habla(self):
        return ''

    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.num_patas} patas y sueno así: {self.habla()}"


class Gato(Animal):
    def habla(self):
        return 'Miau'

    def __str__(self):
        return f"Soy un gato. {super().__str__()}"


class Perro(Animal):
    def habla(self):
        return 'Guau'

    def __str__(self):
        return f"Soy un perro. {super().__str__()}"