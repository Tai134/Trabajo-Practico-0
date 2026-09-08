# A) Mostrar por consola 10 repeticiones con números de manera ascendente, desde el 1
# hasta el 10.

for i in range(1,11):
    print(i)

# B) Mostrar por consola 10 repeticiones con números de manera descendente, desde el
# 10 hasta el 1.

for i in range(10,0,-1):
    print(i)

# C) Ingresar por input un número, convertirlo a entero (int), y repetir el mensaje "Hola
# UTN FRA" tantas veces como el número ingresado.

repes = int(input("Indique cuantas veces repetira el mensaje: "))

for i in range(repes):
    print("Hola UTN FRA")

# D) Ingresar por input un número, convertirlo a entero (int), y mostrar por consola todos
# los números pares desde 1 hasta el número ingresado.

num = int(input("Indica el número hasta el cual queres ir: "))
pares = 0
for i in range(1,num + 1):
    if i % 2 == 0:
        print(i)

# E) Ingresar por input un número, convertirlo a entero (int), y mostrar por consola todos
# los números impares desde 1 hasta el número ingresado.

num = int(input("Indica el número hasta el cual queres ir: "))
pares = 0
for i in range(1,num + 1):
    if i % 2 != 0:
        print(i)

