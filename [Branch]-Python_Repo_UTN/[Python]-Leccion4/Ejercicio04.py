# ===============CLASE 05 - MARTES-13/09/2022===============

# Ejercicio 04: Sumar número pares dentro de un rango. Hacer un programa para sumar números pares dentro de un rango, por ejemplo:
# suma de números pares del 2 al 30 = suma = 240


sumaPares = 0;
for rango in range(31):
    if rango % 2 == 0:
        sumaPares+=rango

print(f'Suma = {sumaPares}')

# SOLUCIÓN CLASE

limiteInferior = (input('Ingrese límite inferior: '))
limiteSuperior = (input('Ingrese límite superior: '))
sumaPares = 0;
for i in range(limiteInferior, limiteSuperior + 1):
    if i % 2 == 0:
        sumaPares+=i

print(f'Suma = {sumaPares}')
