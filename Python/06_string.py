"""
Manejo de cadenas de caracteres
"""
nombre1="alejandra"
print(f"jedi 1:{nombre1}")
print(f"Tipo de dato: {type(nombre1)}")

nombre2="alba"
print(f"jedi 2:{nombre2}")
print(f"Tipo de dato: {type(nombre2)}")

#Funciones comunes de las variables string
print("fucniones comuns de texto")
droide_1="R2-D2"
droide_2="C3PO"
longitud_droide_1=len(droide_1)
longitud_droide_2=len(droide_2)
print("nombre droide 1: ",droide_1)
print("longitud droide 1: ",longitud_droide_1)

print("nombre droide 2: ",droide_2)
print("longitud droide 2: ",longitud_droide_2)

#Manipulacion de mayusculas y minusculas
print("conversion de mayusculas y minusculas")
mensaje="la federacion invade el planeta pluton"
mensaje_mayuscula=mensaje.upper()
mensaje_minuscula=mensaje.lower()
print(f"mensaje convertido a mayusculas: {mensaje_mayuscula}")
print(f"mensaje convertido a minusculas: {mensaje_minuscula}")

#Remplazo de substring
print("Remplazo de substring")

mensaje="la nave vijara a pluton"
print(f"el mensaje original es: {mensaje}")

nuevo_mensaje=mensaje.replace("pluton","mercurio")
print(f"el mensaje modificado es: {mensaje}")

#Sepaarcion de cadenas en arreglos
print("SEparaion de una cadena en arreglos")
planetas="pluton, marte, mercurio"

print(f"planetas registrados: {planetas}")
listar_planetas=planetas.split(",")
print(listar_planetas)
print(f"primer planeta: {listar_planetas[0]}")

#Extraccion de subcadenas
print("Extraccion de subcades")

mensaje="Que la fuerza te acompañe siempre"
adjetivo=mensaje[7:13]
verbo=mensaje[17:25]

print(f"el adjetivo es : {adjetivo}")
print(f"el verbo es: {verbo}")

#Comprobaciones
print("Comprobaciones utiles")

codigo="R2D2"
numero="2026"
nombre="Universidad UTE"
identificador="DROIDE1"

print(codigo.isalnum())
print(numero.isdigit())
print(nombre1.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())