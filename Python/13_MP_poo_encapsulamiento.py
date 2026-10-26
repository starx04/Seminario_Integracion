class EquipoMovil:
    modelo: str
    __precio: float

    def __init__(self, modelo: str, precio: float):
        self.modelo = modelo
        self.__precio = precio

    def mostrar_informacion(self):
        print("Modelo:", self.modelo)
        print("Precio:", self.__precio)

    def get_precio(self) -> float:
        return self.__precio


galaxy = EquipoMovil("Galaxy A55", 399.99)
moto = EquipoMovil("Moto G84", 249.99)
redmi = EquipoMovil("Redmi Note 13", 199.99)
iphone = EquipoMovil("iPhone 15", 899.99)

galaxy.mostrar_informacion()
moto.mostrar_informacion()
redmi.mostrar_informacion()
iphone.mostrar_informacion()
print("Precio del Galaxy A55:", galaxy.get_precio())
print("Precio del Moto G84:", moto.get_precio())
