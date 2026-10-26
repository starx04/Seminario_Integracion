class Guerrero():
    nombre: str
    raza: str
    
    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_inf(self):
        print("Nombre:", self.nombre)
        print("Raza:", self.raza)

goku = Guerrero("Goku", "SSJ")
vegeta = Guerrero("Vegeta", "SSJ")
piccolo = Guerrero("Piccolo", "Namekiano")
andres = Guerrero("Andres", "Human")

goku.mostrar_inf()
vegeta.mostrar_inf()
piccolo.mostrar_inf()
andres.mostrar_inf()