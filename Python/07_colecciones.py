#Colecciones de datos
print("Colecciones de datos")

print("listas")
naves=["n-1","transporte","naboo"]
print(f"tipo: {type(naves)}")

print("tuplas")
coordenadas=(15,30,45)
print(f"tipo: {type(coordenadas)}")

print("diccionario")
droide={
    "modelo": "R2-D2",
    "tipo": "Astromecanico",
    "activo": True
}
print(f"droide: {droide}")
print(f"tipo: {type(droide)}")

print("conjunto")
planetas={
    "pluton",
    "marte",
    "mercurio"
}
print(f"planetas: {planetas}")
print(f"tipo: {type(planetas)}")

print("Crud de listas en python")
avergers=[
    {"id":1, "nombre": "Toni stark", "heroe":"Iron man", "estado":"Activo"},
    {"id":2, "nombre": "Steve rogers", "heroe":"Capitan America", "estado":"Activo"},
    {"id":3, "nombre": "Thor odinson", "heroe":"Thor", "estado":"Activo"},
]

#Creacion de un crud con pyhton
id_publico = 4
def create():
    global id_publico
    print("Reclutar avenger")
    nombre = input("nombre del heroe: ")
    heroe = input("HEROE: ")
    estado = input("Estado(Activo, Retirado, Desaparecido): ")
    nuevo_averger = {
        "id": id_publico,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    avergers.append(nuevo_averger)
    id_publico += 1
    print("Avenger agregado con éxito.")

def read():
    print("listar avenger")
    if not avergers:
        print("No hay avengers registrados.")
    for i in avergers:
        print(f"ID: {i['id']} | Nombre: {i['nombre']} | Héroe: {i['heroe']} | Estado: {i['estado']}")

def update():
    print("Actualizar avenger")
    id_update = int(input("id a modificar: "))
    for avenger in avergers:
        if avenger["id"] == id_update:
            avenger["nombre"] = input("nuevo nombre: ")
            avenger["heroe"] = input("nuevo heroe: ")
            avenger["estado"] = input("nuevo estado: ")
            print("actualizado")
            return
    print("ID no encontrado.")

def delete():
    print("eliminar avenger")
    id_delete = int(input("id de avenger a eliminar: "))
    for avenger in avergers:
        if avenger["id"] == id_delete:
            avergers.remove(avenger)
            print("eliminado")
            return
    print("ID no encontrado.")

def menu():
    while True:
        print("\n1.crear")
        print("2.listar")
        print("3.modificar")
        print("4.eliminar")
        print("5.salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            create()
        if opcion == "2":
            read()
        if opcion == "3":
            update()
        if opcion == "4":
            delete()
        if opcion == "5":
            print("Saliendo del programa...")
            break

menu()