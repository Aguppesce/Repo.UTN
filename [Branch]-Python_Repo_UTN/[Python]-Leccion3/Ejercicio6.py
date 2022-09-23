# ===============CLASE 10 - MIERCOLES-22/06/2022===============
# EJERCICIO 6
# Ingresar N enteros, visualizar la suma de los números pares de la lista, cuántos números
# pares existen y cuál es el promedio de los números impares.

print("Programa que suma números pares y calcula el promedio de los impares")

sumaPares, sumaImpares, contadorPares, contadorImpares = 0, 0, 0, 0

num = int(input("Ingrese un número: "))

while num > 0:
    if num <= 0:
        break
    if num % 2 == 0:
        sumaPares = sumaPares + num
        contadorPares = contadorPares + 1
    else:
        sumaImpares = sumaImpares + num
        contadorImpares = contadorImpares + 1
    num = int(input("Ingrese un número: "))

print(f'El promedio de los números impares es: {sumaImpares/contadorImpares}\n'
      f'La cantidad de números pares ingresados son: {contadorPares}\n'
      f'La suma de todos los números pares ingresados es: {sumaPares}')
