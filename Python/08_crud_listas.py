avengers = [
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitan Amércia", "estado": "A"},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": "A"}
]
id_publico = 4

def create():
    global id_publico
    print("Reclutar advenger")
    nombre = input("Nombre heroe: ")
    heroe = input("Heroe: ")
    estado = input("Estado (Activo, Retirado, Desaparecido)")
    nuevo_advenger = {
        "id": id_publico,
        "nombre": nombre,
        "heroe": heroe,
        "estado": estado
    }
    avengers.append(nuevo_advenger)
    print("Creado")

def read():
    print("Lista de avengers")
    for avenger in avengers:
        print(f"{avenger["id"]} - nombre : {avenger["nombre"]}")

def update():
    print("Actualizar avenger")
    id_update = int(input("id a modificar"))
    for avenger in avengers:
        if (avenger["id"] == id_update):
            avenger["nombre"] = input("Nuevo nombre")
            avenger["heroe"] = input("Nuevo heroé")
            avenger["estado"] = input("Nuevo estado")
            print("Actualizado")

def delete():
    print("Eliminar avenger")
    id_delete = int(input("id a borrar"))
    for avenger in avengers:
        if (avenger["id"] == id_delete):  
            avengers.remove(avenger)
            print("Avenger eliminado")

def menu():
    while True:
        print("Avengers")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Seleccione 1 al 5")
        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Cerrando sistema")
            break
        else:
            print("intente nueva opcion")

if __name__ == "__main__":
    menu()