# Colecciones de datos para una tienda de equipos móviles
print("COLECCIONES DE DATOS")

print("\nListas")
marcas = ["Samsung", "Motorola", "Xiaomi"]
print(f"Marcas: {marcas}")
print(f"Tipo: {type(marcas)}")

print("\nTuplas")
especificaciones_equipo = (8, 256, 50)
print(f"Especificaciones (RAM GB, almacenamiento GB, cámara MP): {especificaciones_equipo}")
print(f"Tipo: {type(especificaciones_equipo)}")

print("\nDiccionarios")
equipo = {
    "modelo": "Galaxy A55",
    "marca": "Samsung",
    "precio": 399.99,
    "disponible": True,
}
print(f"Equipo: {equipo}")
print(f"Tipo: {type(equipo)}")

print("\nConjuntos")
colores_disponibles = {"negro", "azul", "verde"}
print(f"Colores disponibles: {colores_disponibles}")
print(f"Tipo: {type(colores_disponibles)}")

print("\nCRUD de inventario")
inventario = [
    {"id": 1, "modelo": "Galaxy A55", "marca": "Samsung", "precio": 399.99, "stock": 5},
    {"id": 2, "modelo": "Moto G84", "marca": "Motorola", "precio": 249.99, "stock": 8},
    {"id": 3, "modelo": "Redmi Note 13", "marca": "Xiaomi", "precio": 199.99, "stock": 10},
]
id_publico = 4


def create():
    global id_publico
    print("\nAgregar equipo al inventario")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad en stock: "))
    nuevo_equipo = {
        "id": id_publico,
        "modelo": modelo,
        "marca": marca,
        "precio": precio,
        "stock": stock,
    }
    inventario.append(nuevo_equipo)
    id_publico += 1
    print("Equipo agregado con éxito.")


def read():
    print("\nInventario de equipos móviles")
    if not inventario:
        print("No hay equipos registrados.")
        return

    for equipo in inventario:
        print(
            f"ID: {equipo['id']} | Modelo: {equipo['modelo']} | "
            f"Marca: {equipo['marca']} | Precio: ${equipo['precio']:.2f} | "
            f"Stock: {equipo['stock']}"
        )


def update():
    print("\nActualizar equipo")
    id_update = int(input("ID del equipo que desea modificar: "))
    for equipo in inventario:
        if equipo["id"] == id_update:
            equipo["modelo"] = input("Nuevo modelo: ")
            equipo["marca"] = input("Nueva marca: ")
            equipo["precio"] = float(input("Nuevo precio: "))
            equipo["stock"] = int(input("Nuevo stock: "))
            print("Equipo actualizado.")
            return
    print("ID no encontrado.")


def delete():
    print("\nEliminar equipo")
    id_delete = int(input("ID del equipo que desea eliminar: "))
    for equipo in inventario:
        if equipo["id"] == id_delete:
            inventario.remove(equipo)
            print("Equipo eliminado.")
            return
    print("ID no encontrado.")


def menu():
    while True:
        print("\n1. Agregar equipo")
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
            print("Saliendo del inventario...")
            break
        else:
            print("Opción no válida.")


menu()
