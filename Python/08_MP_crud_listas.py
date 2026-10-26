equipos = [
    {"id": 1, "modelo": "Galaxy A55", "marca": "Samsung", "precio": 399.99, "estado": "Disponible"},
    {"id": 2, "modelo": "Moto G84", "marca": "Motorola", "precio": 249.99, "estado": "Disponible"},
]
id_publico = 3


def create():
    global id_publico
    print("\nAgregar equipo móvil")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    estado = input("Estado (Disponible, Reservado, Agotado): ")
    nuevo_equipo = {
        "id": id_publico,
        "modelo": modelo,
        "marca": marca,
        "precio": precio,
        "estado": estado,
    }
    equipos.append(nuevo_equipo)
    id_publico += 1
    print("Equipo agregado con éxito.")


def read():
    print("\nInventario de equipos móviles")
    if not equipos:
        print("No hay equipos registrados.")
        return

    for equipo in equipos:
        print(
            f"ID: {equipo['id']} | Modelo: {equipo['modelo']} | "
            f"Marca: {equipo['marca']} | Precio: ${equipo['precio']:.2f} | "
            f"Estado: {equipo['estado']}"
        )


def update():
    print("\nActualizar equipo móvil")
    id_update = int(input("ID del equipo que desea modificar: "))
    for equipo in equipos:
        if equipo["id"] == id_update:
            equipo["modelo"] = input("Nuevo modelo: ")
            equipo["marca"] = input("Nueva marca: ")
            equipo["precio"] = float(input("Nuevo precio: "))
            equipo["estado"] = input("Nuevo estado: ")
            print("Equipo actualizado.")
            return
    print("ID no encontrado.")


def delete():
    print("\nEliminar equipo móvil")
    id_delete = int(input("ID del equipo que desea eliminar: "))
    for equipo in equipos:
        if equipo["id"] == id_delete:
            equipos.remove(equipo)
            print("Equipo eliminado.")
            return
    print("ID no encontrado.")


def menu():
    while True:
        print("\nTIENDA DE EQUIPOS MÓVILES")
        print("1. Agregar equipo")
        print("2. Listar equipos")
        print("3. Modificar equipo")
        print("4. Eliminar equipo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Cerrando el inventario.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
