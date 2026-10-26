class Guerrero():
    nombre: str
    __poder: int
    
    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.__poder = poder

    def mostrar_inf(self):
        print("Nombre:", self.nombre)
        print("Poder:", self.__poder)

    def get_poder(self):
        return self.__poder

goku = Guerrero("Goku", 9000)
vegeta = Guerrero("Vegeta", 8000)
piccolo = Guerrero("Piccolo", 10000)
andres = Guerrero("Andres", 600000)

goku.mostrar_inf()
vegeta.mostrar_inf()
piccolo.mostrar_inf()
andres.mostrar_inf()
print(goku.nombre)
print(vegeta.nombre)