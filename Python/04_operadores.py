print("OPERADORES")
print("Operadores Aritmeticos")
print(" + Suma:", 5, "+", 5, "=", 5+5)
print(" - Resta:", 10, "-", 3, "=", 10-3)
print(" * Multiplicacion:", 4, "*", 6, "=", 4*6)
print(" / Division:", 15, "/", 3, "=", 15/3)
print(" // Division Entera:", 15, "//", 4, "=", 15//4)
print(" % Modulo:", 10, "%", 3, "=", 10%3)
print(" ** Potencia:", 2, "**", 3, "=", 2**3)

print("Tabla de multiplicar del 5")
print("5 x 1 =", 5*1)
print("5 x 2 =", 5*2)
print("5 x 3 =", 5*3)
print("5 x 4 =", 5*4)
print("5 x 5 =", 5*5)
print("5 x 6 =", 5*6)
print("5 x 7 =", 5*7)
print("5 x 8 =", 5*8)
print("5 x 9 =", 5*9)
print("5 x 10 =", 5*10)

print("OPERADORES DE COMPARACION")
print(" == Igual:", 5, "==", 5, "=", 5==5)
print(" == Igual:", 5, "==", 2, "=", 5==2)
print(" != Diferente:", 5, "!=", 3, "=", 5!=3)
print(" != Diferente:", 3, "!=", 3, "=", 3!=3)
print(" < Menor:", 5, "<", 10, "=", 5<10)
print(" > Mayor:", 10, ">", 5, "=", 10>5)
print(" <= Menor o igual:", 5, "<=", 5, "=", 5<=5)
print(" >= Mayor o igual:", 10, ">=", 5, "=", 10>=5)

print("OPERADORES LOGICOS")
print("operador and : (5==5)and (10>5) =", (5==5)and (10>5))
print("operador or : (5==5)or (10<5) =", (5==5)or (10<5))
print("operador not : not (5==5) =", not (5==5))

tiene_dinero = True
tienda_abierta = False

puede_comprar = tiene_dinero and tienda_abierta
print("Puede comprar:", puede_comprar)

es_cliente_vip = True
tiene_dinero = False
aceeso_credito = es_cliente_vip or tiene_dinero
print("Acceso a credito:", aceeso_credito)
