class personaje:
    nombre: str
    raza: str

    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

class Saiyajin(personaje):
    def __init__(self, nombre: str, raza: str):
        super().__init__(nombre, raza)

    def muestra_nombre(self):
        print("Nombre: ", self.nombre)

goku = Saiyajin("Goku", "Saiyajin")
vegeta = Saiyajin("Vegeta", "Saiyajin")
goku.mostrar_info()
vegeta.mostrar_info()
goku.muestra_nombre()
vegeta.muestra_nombre()