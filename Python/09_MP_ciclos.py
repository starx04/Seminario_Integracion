for unidad in range(1, 6):
    print("Equipo vendido:", unidad)

for cantidad in range(1, 11):
    print("Venta de", cantidad, "equipos a $250 cada uno:", cantidad * 250)

for cantidad in range(1, 11, 2):
    print("Venta de", cantidad, "equipos a $250 cada uno:", cantidad * 250)

equipos = [
    {"id": 1, "modelo": "Galaxy A55", "marca": "Samsung", "estado": "Disponible"},
    {"id": 2, "modelo": "Moto G84", "marca": "Motorola", "estado": "Disponible"},
    {"id": 3, "modelo": "Redmi Note 13", "marca": "Xiaomi", "estado": "Agotado"},
]

print("\nInventario de equipos")
for equipo in equipos:
    print(f"{equipo['id']} - {equipo['marca']} {equipo['modelo']}: {equipo['estado']}")

marcas = ["Samsung", "Motorola", "Xiaomi"]
for marca in marcas:
    print("Marca disponible:", marca)

stock_por_modelo = {
    "Galaxy A55": 8,
    "Moto G84": 4,
    "Redmi Note 13": 0,
}

for modelo, stock in stock_por_modelo.items():
    if stock > 0:
        print(modelo, "está disponible con", stock, "unidades")
    else:
        print(modelo, "no tiene unidades en stock")

print("\nRecorrido de modelos y colores")
colores = ["negro", "azul", "verde"]
for equipo in equipos:
    print("Colores para", equipo["modelo"])
    for color in colores:
        print("Color:", color)

print("\nUso de break y continue")
for modelo in stock_por_modelo:
    if modelo == "Redmi Note 13":
        print("Se encontró el modelo agotado; se detiene la búsqueda.")
        break
    if modelo == "Moto G84":
        continue
    print("Modelo disponible para revisar:", modelo)
