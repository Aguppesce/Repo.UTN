# ===============CLASE 06 - MARTES-20/09/2022===============

# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo números, utilizando argumentos variables *args como parámetro de la función y agregar como resultado la suma de todos los valores pasados como argumentos.
def sumar(*args): # Recibimos una cantidad de parámetros indefinidos
    resultado = 0 # pass la utilizamos para no dejar vacía la función y que no nos dé un error
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado

# Llamamos a la función
print(sumar(3,5,9,2,1))
