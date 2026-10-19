print("Condicional If")
print("Condicional Simple")
dinero = 10
if dinero>=5:
    print("Homero puede comprar rosquillas")
print("Programa finalizado")


print("Condicional if - else")
print("Condicional dos caminos")
creditos = float(input("Cantidad de creditos disponibles"))
precio_repuestos = float(input("Precio repuestos"))

if (creditos >= precio_repuestos):
    print("Compra autorizada")
else:
    print("Credito insuficiente")
    print("Buscar solucion o trueque")

print("Condicional If - elif - else")
print("COndicional Condicional Anidada")

combustible = float(input("Combustible de la nave"))
if (combustible>=75):
    print("Optimo")
elif (combustible>=50):
    print("Suficiente")
elif (combustible>=20):
    print("Bajo")
else:
    print("Critico")
    print("Localizar base mas cercana")


piloto = input("Nombre del piloto")
motor_funciona = input("El motor funciona (SI/NO)")
combustible = int(input("Combustible disponible"))

if (motor_funciona=="SI"):
    print("Motor verificado")
    if combustible>=50:
        print("Combustible suficiente")
        print("Participacion autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede participar")
    print("EL motor necesita reparacion")