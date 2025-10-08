class Libro:
    def __init__(self, titulo, autor, num_ejemplares, num_prestados=0):
        self.title = titulo
        self.author = autor
        self.num_ejemplares = num_ejemplares
        self.num_prestados = num_prestados

    def prestamo(self):
        if self.num_ejemplares > self.num_prestados:
            self.num_prestados += 1
            return True
        else:
            return False

    def devolucion(self):
        if self.num_prestados > 0:
            self.num_prestados -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"Libro: {self.title} - Autor: {self.author} - Ejemplares disponibles: {self.num_ejemplares - self.num_prestados}"

    def __eq__(self, otro):
        return self.title == otro.titulo and self.author == otro.autor

    def __lt__(self, otro):
        return self.author < otro.autor

