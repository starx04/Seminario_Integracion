class EquipoMovil:
    modelo: str
    marca: str

    def __init__(self, modelo: str, marca: str):
        self.modelo = modelo
        self.marca = marca

    def mostrar_informacion(self):
        print("Modelo:", self.modelo)
        print("Marca:", self.marca)


galaxy = EquipoMovil("Galaxy A55", "Samsung")
moto = EquipoMovil("Moto G84", "Motorola")
redmi = EquipoMovil("Redmi Note 13", "Xiaomi")
iphone = EquipoMovil("iPhone 15", "Apple")

galaxy.mostrar_informacion()
moto.mostrar_informacion()
redmi.mostrar_informacion()
iphone.mostrar_informacion()
