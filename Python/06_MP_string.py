"""
Manejo de cadenas de caracteres en una tienda de equipos móviles.
"""

print("MANEJO DE CADENAS")

nombre_cliente = "Camila Torres"
print(f"Cliente: {nombre_cliente}")
print(f"Tipo de dato: {type(nombre_cliente)}")

nombre_equipo = "Galaxy A55"
print(f"Equipo: {nombre_equipo}")
print(f"Tipo de dato: {type(nombre_equipo)}")

print("\nFunciones comunes de texto")
marca_1 = "Samsung"
marca_2 = "Motorola"
longitud_marca_1 = len(marca_1)
longitud_marca_2 = len(marca_2)
print(f"Marca 1: {marca_1}")
print(f"Longitud de la marca 1: {longitud_marca_1}")
print(f"Marca 2: {marca_2}")
print(f"Longitud de la marca 2: {longitud_marca_2}")

print("\nConversión de mayúsculas y minúsculas")
mensaje = "tenemos equipos móviles en promoción"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print(f"Mensaje en mayúsculas: {mensaje_mayuscula}")
print(f"Mensaje en minúsculas: {mensaje_minuscula}")

print("\nReemplazo de una parte del texto")
mensaje = "El equipo seleccionado es un Samsung"
print(f"Mensaje original: {mensaje}")
nuevo_mensaje = mensaje.replace("Samsung", "Motorola")
print(f"Mensaje modificado: {nuevo_mensaje}")

print("\nSeparación de cadenas")
marcas = "Samsung, Motorola, Xiaomi, Apple"
print(f"Marcas disponibles: {marcas}")
lista_marcas = marcas.split(", ")
print(lista_marcas)
print(f"Primera marca: {lista_marcas[0]}")

print("\nExtracción de subcadenas")
codigo_equipo = "MOV-2026-A55"
prefijo = codigo_equipo[0:3]
modelo = codigo_equipo[8:11]
print(f"Código del equipo: {codigo_equipo}")
print(f"Prefijo: {prefijo}")
print(f"Modelo: {modelo}")

print("\nComprobaciones útiles")
codigo = "A55PRO"
numero = "2026"
nombre = "Camila"
identificador = "EQUIPO2026"

print(f"El código es alfanumérico: {codigo.isalnum()}")
print(f"El año contiene solo dígitos: {numero.isdigit()}")
print(f"El nombre contiene solo letras: {nombre.isalpha()}")
print(f"El identificador es alfanumérico: {identificador.isalnum()}")
print(f"El identificador contiene solo dígitos: {identificador.isdigit()}")
