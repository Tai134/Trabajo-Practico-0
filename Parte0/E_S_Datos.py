# - - - - - A - - - - - #

print("Esto funciona de maravilla.")

# - - - - - B - - - - - #

dato = input("Ingrese un dato: ")
print(dato)

# - - - - - C - - - - - #

name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))

print(f"Usted se llama {name} y tiene {age} años.")

# - - - - - D - - - - - #

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

suma = (num_1 + num_2)

print(f"La suma es {suma}")

# - - - - - E - - - - - #

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

division = (num_1 % num_2)

print(f"El resto es {division}")

# - - - - - F - - - - - #

importe = float(input("Ingrese el importe deseado: "))

porcentaje = 0.10

calculo_porcentaje = (importe * porcentaje)

incremento = (importe + calculo_porcentaje)

print(f"Su importe es: {importe}\nEl 10% de su importe es: {calculo_porcentaje}\nSu importe final es: {incremento}")

# - - - - - G - - - - - #

importe = float(input("Ingrese el importe deseado: "))

porcentaje = 0.25

calculo_porcentaje = (importe * porcentaje)

descuento = (importe - calculo_porcentaje)

print(f"Su importe es: {importe}\nEl 10% de su importe es: {calculo_porcentaje}\nSu importe final es: {descuento}")
