class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad

    def __lt__(self, other):
        if self.nombre == other.nombre:
            return self.edad < other.edad
        return self.nombre < other.nombre

    def __gt__(self, other):
        if self.nombre == other.nombre:
            return self.edad > other.edad
        return self.nombre > other.nombre
