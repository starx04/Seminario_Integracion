stock = 0
while stock < 10:
    stock += 2
    print("Ingresaron equipos a la tienda. Stock actual:", stock)
print("Se alcanzó el stock objetivo.")

unidades_disponibles = 3
while unidades_disponibles > 0:
    print("Vendiendo un equipo. Unidades restantes:", unidades_disponibles - 1)
    unidades_disponibles -= 1

print("Se agotó el inventario de este modelo.")
