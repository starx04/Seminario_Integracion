#input
print("Incluir Datos con Input")
nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "Bienvenido a Python")
print("Bienvenido a Springfield"+ nombre)

cantidad = int(input("Ingrese la cantidad de rosquillas que hay: "))
total= cantidad + 2
print("El total de rosquillas es: ", total)

print("CONVERSIONES")
print("=========TIENDA DE APU==========")
nombre_cliente = input("Ingrese su nombre: ")
precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese la cantidad de productos: "))
total= precio * cantidad
print("El total a pagar es: ", total)
print("Total a pagar (round):", round(total, 2))
print(f"Total a pagar (f): {total:.2f}")

