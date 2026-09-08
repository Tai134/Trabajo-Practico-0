# - - - - - A - - - - - #
# Ingresar un mes por input e informar por consola:
# Si es Enero: "Que comiences bien el año!"
# Si es Marzo: "A clases!"
# Si es Julio: "Se vienen las vacaciones!"
# Si es Diciembre: "Felices fiesta!"

mes = input("Ingrese el mes a consultar: ")

match mes:
    case "Enero":
        print("Que comiences bien el año!")

    case "Marzo":
        print("A clases!")

    case "Julio":
        print("Se vienen las vacaciones!")

    case "Diciembre":
        print("Felices Fiestas!")

    case _:
        print("Es un mes más!")

# # - - - - - B - - - - - #
# Ingresar un mes por input e informar por consola:
# Si estamos en Invierno: "Abrigate que hace frio."
# Si aún no llego el Invierno: "Falta para el invierno."
# Si ya paso el Invierno: "Ya pasamos el frio, ahora calor!"
# Aclaración: Se debe tomar a Julio y Agosto como los meses de invierno. 

mes = input("Ingrese el mes a consultar: ")

match mes:
    case "Enero" | "Febrero" | "Marzo" | "Abril" | "Mayo" | "Junio":
        print("Falta para el invierno.")

    case "Julio" | "Agosto":
        print("Abrigate que hace frio.")

    case "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
        print("Ya pasamos el frio, ahora calor!")

    case _:
        print("La palabra ingresada NO es un mes.")

# - - - - - C - - - - - #
# Ingresar un mes por input e informar:
# Si es Febrero: " Este mes no tiene más de 29 días."
# Si no es Febrero: "Este mes tiene 30 o más días.

mes = input("Ingrese el mes a consultar: ")

match mes:
    case "Enero" | "Marzo" | "Abril" | "Mayo" | "Junio" | "Julio" | "Agosto" | "Septiembre" | "Octubre" | "Noviembre" | "Diciembre":
        print("Tiene 30 días o más.")

    case "Febrero":
        print("Tiene 28 días")

    case _:
        print("La palabra ingresada NO es un mes.")

# - - - - - D - - - - - #
# Ingresar un mes por input e informar:
# Si tiene 28 días.
# Si tiene 30 días.
# Si tiene 31 días.

mes = input("Ingrese el mes a consultar: ")

match mes:
    case "Abril" | "Junio" | "Septiembre" | "Noviembre":
        print("El mes tiene 30 días.")

    case "Enero" | "Marzo" | "Mayo" | "Julio" | "Agosto" | "Octubre" | "Diciembre":
        print("El mes tiene 31 días.")

    case "Febrero":
        print("El mes tiene 28 días.")

    case _:
        print("El valor ingresado no es un mes.")


# - - - - - E - - - - - #
# Ingresar un numero entero que represente una hora del día e informar:
# Si está entre las 7 y las 11 : "Es de mañana."

hora = int(input("Ingresa un horario: "))

match hora:
    case 7 | 8 | 9 | 10 | 11:
        print("Es de mañana")
    case _:
        pass

# - - - - - F - - - - - # 
#  Ingresar un número entero que represente una hora del día e informar:
# Si está entre las 7 y las 11 : "Es de mañana."
# Si está entre las 12 y las 19 : "Es de tarde."
# Si está entre las 20 y las 23 o entre las 0 y las 6 : "Es de noche."
# Si no está entre las 0 y las 23 : "la hora no existe."

hora = int(input("Ingresa un horario: "))

match hora:
    case 7 | 8 | 9 | 10 | 11:
        print("Es de mañana.")
    case 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19:
        print("Es de tarde.")
    case 20 | 21 | 22 | 23 | 00 | 0 | 1 | 2 | 3 | 4 | 5 | 6:
        print("Es de noche.")
    case _:
        print("La hora no existe.")


# - - - - - G - - - - - #
#  Ingresar dos números por input, transformarlos a entero (int).
# Luego seleccionar la opción:
# Sumar
# Restar
# Multiplicar
# Dividir (numero_uno / numero_dos)
# Mostar el resulto por consola.
# Ejemplo: "la suma es 750"

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

print("Operaciones posibles:\nSumar\nRestar\nMultiplicar\nDividir")

operacion = input("Operación a realizar: ")
match operacion:
    case "Sumar":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    case "Restar":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    case "Multiplicar":
        print(f"{num_1} x {num_2} = {num_1 * num_2} ")
    case "Dividir":
        print(f"{num_1} / {num_2} = {num_1 / num_2} ")
    case _:
        print("El valor ingresado no es una operación permitida.")
