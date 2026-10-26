print("Incluir datos con input")
nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "Bienvenido a Móvil Center")
print("Bienvenido a nuestra tienda", nombre)

cantidad_inicial = int(input("Ingrese la cantidad de equipos móviles: "))
total_equipos = cantidad_inicial + 2
print("El total de equipos es:", total_equipos)

print("CONVERSIONES")
print("========= MÓVIL CENTER =========")
nombre_cliente = input("Ingrese el nombre del cliente: ")
precio_equipo = float(input("Ingrese el precio del equipo: "))
cantidad_productos = int(input("Ingrese la cantidad de equipos: "))
total_pagar = precio_equipo * cantidad_productos
print("Total a pagar para", nombre_cliente, ":", total_pagar)
print("Total a pagar (round):", round(total_pagar, 2))
print(f"Total a pagar (f): {total_pagar:.2f}")