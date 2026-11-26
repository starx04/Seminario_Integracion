class EquipoMovil:
    modelo: str
    marca: str

    def __init__(self, modelo: str, marca: str):
        self.modelo = modelo
        self.marca = marca

    def mostrar_informacion(self):
        print("Modelo:", self.modelo)
        print("Marca:", self.marca)


class Smartphone(EquipoMovil):
    def __init__(self, modelo: str, marca: str, almacenamiento_gb: int):
        super().__init__(modelo, marca)
        self.almacenamiento_gb = almacenamiento_gb

    def mostrar_almacenamiento(self):
        print("Almacenamiento:", self.almacenamiento_gb, "GB")


galaxy = Smartphone("Galaxy A55", "Samsung", 256)
iphone = Smartphone("iPhone 15", "Apple", 128)

galaxy.mostrar_informacion()
galaxy.mostrar_almacenamiento()
iphone.mostrar_informacion()
iphone.mostrar_almacenamiento()