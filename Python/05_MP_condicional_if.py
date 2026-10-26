print("CONDICIONAL IF")

print("Condicional simple")
dinero_disponible = 400
precio_equipo = 300

if dinero_disponible >= precio_equipo:
    print("El cliente puede comprar el equipo móvil")
print("Programa finalizado")

print("\nCondicional if - else")
credito_disponible = float(input("Ingrese el crédito disponible: "))
precio_equipo = float(input("Ingrese el precio del equipo móvil: "))

if credito_disponible >= precio_equipo:
    print("Compra autorizada")
else:
    print("Crédito insuficiente para comprar el equipo")
    print("Puede elegir un equipo de menor precio")

print("\nCondicional if - elif - else")
porcentaje_bateria = int(input("Ingrese el porcentaje de batería del equipo usado: "))

if porcentaje_bateria >= 75:
    print("Estado de batería: óptimo")
elif porcentaje_bateria >= 50:
    print("Estado de batería: bueno")
elif porcentaje_bateria >= 20:
    print("Estado de batería: bajo")
else:
    print("Estado de batería: crítico")
    print("Se recomienda revisar o reemplazar la batería")

print("\nCondicional anidada")
nombre_cliente = input("Ingrese el nombre del cliente: ")
equipo_disponible = input("¿El equipo está disponible? (SI/NO): ").strip().upper()
dinero_disponible = float(input("Ingrese el dinero disponible: "))
precio_equipo = float(input("Ingrese el precio del equipo: "))

if equipo_disponible == "SI":
    print("Equipo disponible")
    if dinero_disponible >= precio_equipo:
        print(f"Compra autorizada para {nombre_cliente}")
    else:
        print("Dinero insuficiente; puede consultar opciones de financiamiento")
else:
    print(f"El equipo no está disponible para {nombre_cliente}")
    print("Puede consultar otros modelos de nuestro catálogo")