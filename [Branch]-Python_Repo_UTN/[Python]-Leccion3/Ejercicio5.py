# ===============CLASE 10 - MIERCOLES-22/06/2022===============
# EJERCICIO 5
# Calcular el factorial de un número mayor o igual a 0

print("Programa que calcular el factorial de un número")

num = int(input("Ingrese un número mayor o igual a 0: "))

while num < 0:
    print('El número tiene que ser mayor a 0')
    num = int(input("Ingrese un número mayor o igual a 0: "))

factorial = 1

if num >= 0:
    for i in range(1, num+1):
        factorial = factorial*i
        i = i + 1

print(f'El factorial es {factorial}')
