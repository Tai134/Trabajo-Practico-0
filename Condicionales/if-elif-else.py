# ---------- Ejercicio A ---------- #

year = int(input("Ingrese un año: "))

if year == 1980:
    print("Este año se creó el videojuego Pac-Man")

else:
    print("Es un año normal")

#---------- Ejercicio B ---------- #   

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("El usuario es mayor de edad.")

#---------- Ejercicio C ---------- #

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("El usuario es mayor de edad.")

else:
    print("El usuario es menor de edad")

#---------- Ejercicio D ---------- #
    
edad = int(input("Ingrese su edad: "))

if edad >= 13 and edad <= 17:
    print("El usuario es adolescente.")

#---------- Ejercicio E ---------- #

edad = int(input("Ingrese su edad: "))

if edad < 13 or edad >= 17:
    print("El usuario no es adolescente.")

#---------- Ejercicio F ---------- #

edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("El usuario es niño.")

elif edad >= 13 and edad <= 17:
    print("El usuario es adolescente.")

else:
    print("El usuario es mayor de edad.")
