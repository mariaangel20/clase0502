# Ejercicio 1 - Parte B
gastos = [500,500,500,500,500]

total = 0
for gasto in gastos:
    total = total + gasto 

print(f"Total:  Q{total}")

#Ejercicio 1 - Parte C
gastos = [1200, 350, 450, 875, 600]

total = 0
for gasto in gastos:
    total = total + gasto
    print(f"Sumando Q{gasto}... Total ahora: Q{total}")
    
print(f"Total:  Q{total}")

# Ejercicio 2 - Parte A
for numero in range(5):
    print(numero)

for numero in range(1, 6):
    print(numero)

for numero in range (0, 10, 2):
    print(numero)

# Ejercicio 2 - Parte B
precio_por_pagina = 2.5
for paginas in range(1,6):
    total = paginas * precio_por_pagina
    print(f"{paginas} página(s): Q{total : .2f}")

# Ejercicio 2 - Parte C

tipo_cambio = 7.80
for usd in range (10,101, 10):
    total = usd * tipo_cambio
    print(f"{usd} Cambio: Q{total}")

# Ejercicio 3 - Parte A
ventas = [15000 , 22000 , 18000 , 25000]

for posicion , venta in enumerate ( ventas ):
    print (f"{ posicion + 1} lugar : Q{ venta }")

# Ejercicio 3 - Parte B
productos = [" Laptop ", " Mouse ", " Teclado "]
for n , p in enumerate ( productos , start =1) :
    print(f"#{n}: {p}")

# Ejercicio 3 - Parte C
prod = [" Papel ", " Lapiceros ", " Cuadernos "]
stock = [45 , 120 , 85]
for n , p in enumerate ( prod , start =1) :
    cant = stock [n-1]
    print (f"[{n}] {p}: { cant }")
    if cant < 50:
        print("!Bajo stock")

