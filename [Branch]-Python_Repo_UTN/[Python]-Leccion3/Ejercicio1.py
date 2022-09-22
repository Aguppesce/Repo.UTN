# ===============CLASE 9 - MIERCOLES-15/06/2022===============
# EJERCICIO 1
# Diseñar un programa que ingresando un año, nos devuelva por consola
# si es un año bisiesto o no, repetir la acción hasta que el usuario
# lo desida.

print("Programa que determina si un año es bisiesto")
print("Para salir ingrese 0")

anio = int(input("Ingrese un anio: "))

while anio != 0:
    if anio < 0:
        print("Error! Debe ingresar un año mayor a 0")
        anio = int(input("Ingrese un anio: "))
    else:
        if(anio % 4 == 0) and (not(anio % 100 == 0) or (anio % 400 == 0)):
            print(f'El año {anio} es bisiesto')
        else:
            print(f'El año {anio} no es bisiesto')

    anio = int(input("Ingrese un anio: "))


