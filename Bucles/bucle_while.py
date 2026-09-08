# A) Mostrar por consola 10 repeticiones con números de manera ascendente, desde el 1
# hasta el 10.

num = 1
while num < 11:
    print(num)
    num += 1

# B) Mostrar por consola 10 repeticiones con números de manera descendente, desde el
# 10 hasta el 1.

num = 10
while num > 0:
    print(num)
    num -= 1

# C) Ingresar un número por input, y mostrarlo por consola. El número ingresado debe
# estar comprendido entre 0 y 9 inclusive, caso contrario volver a pedirlo hasta que el
# número ingresado esté dentro de ese rango.

num = int(input("Ingresa un número: "))
while num > 9:
    num = int(input("Ingresa un número:"))


# D) Ingresar una letra por input, validar que la misma sea „F‟ o „M‟, caso contrario
# volver a pedirla. Una vez validado el ingreso de la letra, mostrar por consola:
# Si la letra ingresada es „F‟: “FEMERNINO”
# Si la letra ingresa es „M‟: “MASCULINO”.

letra = input("Ingrese una letra M o F: ")

while letra != "M" and letra != "F" and letra != "m" and letra != "f":
    letra = input("Reingrese una letra M o F: ")

if letra == "F" or letra == "f":
    print("Femenino")

else:
    print("Masculino")

# E) Ingresar cinco (5) números por input, e informar por consola la suma y el promedio
# de los números ingresados.

contador = 0
suma = 0

while contador < 5:
    numero = int(input("Ingresá un número: "))
    suma = suma + numero
    contador = contador + 1

promedio = suma / 5

print("La suma es:", suma)
print("El promedio es:", promedio)

# F) Ingresar tantos números por input como el usuario desee, e informar por consola la
# suma y el promedio de los números ingresados.

#Para poder corregir y que no rompa el ejercicio F debe estar identado o superpone por la global "VUELTAS"

vueltas = int(input("Ingresá cuantas números usara: "))
contador = 0
suma = 0

while contador < vueltas:
    numero = int(input("Ingresá un número: "))
    suma = suma + numero
    contador += 1

promedio = suma / 5

print("La suma es:", suma)
print("El promedio es:", promedio)

# G) Ingresar tantos números por input como el usuario desee, e informar por consola la
# suma de los números positivos, y la multiplicación de los números negativos.


vueltas = int(input("Ingresá cuantas números usara: "))
contador = 0
suma = 0
multiplicacion = 1

while contador < vueltas:
    numero = int(input("Ingresá un número: "))
    if numero >= 0:
        suma = suma + numero
        contador += 1 

    else:
        multiplicacion = multiplicacion * numero
        contador += 1 

print(f"La suma es:{suma}")
print(f"La multiplicacion es: {multiplicacion}")