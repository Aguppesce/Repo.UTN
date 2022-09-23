# ===============CLASE 9 - MIERCOLES-15/06/2022===============
# EJERCICIO 3
# Leer 10 números e imprimir cuantos son positivos, cuantos negativos
# y cuantos neutros.

print("Programa que cuenta numéros negativos, positivos y neutro")

positivo = 0
negativo = 0
neutro = 0

for i in range(10):
    num = int(input("Ingrese un número: "))
    if(num > 0):
        positivo += 1
    if(num < 0):
        negativo += 1
    if(num == 0):
        neutro += 1
    else:
        print("Ingrese solo números")

print(f'Cantidad de números positivos: {positivo}'
      f'\nCantidad de números negativos: {negativo}'
      f'\nCantidad de números neutros: {neutro}')

