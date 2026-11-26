print("Funciones para la venta de equipos móviles")
print("Tienda Móvil Center")


def mostrar_bienvenida():
    print("Bienvenido a Móvil Center.")
    print("Encuentra el equipo móvil que necesitas.")


mostrar_bienvenida()
mostrar_bienvenida()


def mostrar_equipo(modelo):
    print("Equipo disponible:", modelo)


mostrar_equipo("Galaxy A55")
mostrar_equipo("Moto G84")
mostrar_equipo("Redmi Note 13")


def calcular_total(precio, cantidad):
    return precio * cantidad


total = calcular_total(399.99, 2)
print(f"Total por los equipos: ${total:.2f}")


def revisar_presupuesto(nombre_cliente, presupuesto, precio):
    if presupuesto >= precio:
        print(f"{nombre_cliente} puede comprar el equipo.")
    else:
        print(f"{nombre_cliente} necesita elegir un equipo de menor precio.")


revisar_presupuesto("Camila", 500, 399.99)
revisar_presupuesto("Andrés", 200, 399.99)

nombre_cliente: str = "Camila Torres"
edad_cliente: int = 28
presupuesto_cliente: float = 450.00
es_cliente_frecuente: bool = True


def calcular_descuento(precio: float, porcentaje: float) -> float:
    return precio * porcentaje / 100


descuento: float = calcular_descuento(399.99, 10)
print(f"Descuento para {nombre_cliente}: ${descuento:.2f}")
print("Cliente frecuente:", es_cliente_frecuente)
