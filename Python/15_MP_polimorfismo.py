class EquipoMovil:
    modelo: str
    marca: str

    def __init__(self, modelo: str, marca: str):
        self.modelo = modelo
        self.marca = marca

    def mostrar_informacion(self):
        print(f"Equipo: {self.marca} {self.modelo}")


class Smartphone(EquipoMovil):
    def __init__(self, modelo: str, marca: str, precio: float):
        super().__init__(modelo, marca)
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Celular: {self.marca} {self.modelo} - ${self.precio:.2f}")


class EquipoReacondicionado(EquipoMovil):
    def __init__(self, modelo: str, marca: str, precio: float, meses_garantia: int):
        super().__init__(modelo, marca)
        self.precio = precio
        self.meses_garantia = meses_garantia

    def mostrar_informacion(self):
        print(
            f"Reacondicionado: {self.marca} {self.modelo} - "
            f"${self.precio:.2f} - Garantía: {self.meses_garantia} meses"
        )


catalogo = [
    EquipoMovil("Moto G84", "Motorola"),
    Smartphone("Galaxy A55", "Samsung", 399.99),
    EquipoReacondicionado("iPhone 13", "Apple", 429.99, 6),
]

for equipo in catalogo:
    equipo.mostrar_informacion()
