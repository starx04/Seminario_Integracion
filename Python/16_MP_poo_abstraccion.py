from abc import ABC, abstractmethod


class ProductoTienda(ABC):
    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass


class EquipoMovil(ProductoTienda):
    def __init__(self, modelo: str, marca: str, precio: float):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio

    def mostrar_detalle(self) -> str:
        return f"{self.marca} {self.modelo} - ${self.precio:.2f}"


class Accesorio(ProductoTienda):
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"


catalogo: list[ProductoTienda] = [
    EquipoMovil("Galaxy A55", "Samsung", 399.99),
    Accesorio("Cargador USB-C", 19.99),
]

for producto in catalogo:
    print(producto.mostrar_detalle())
