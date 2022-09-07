import math # Importamos la clase math para hacer uso de la función sqrt(raíz cuadrada)

# ===============CLASE 01 - MARTES-16/08/2022===============
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla

# Crear una lista que solo incluya los números menores a 5 e imprima por consola [1, 3, 2]

lista = [] # Deifnimos la lista
for i in tupla:
    if i < 5:
        lista.append(i)

print(lista)

# ===============CLASE 04 - MARTES-06/09/2022===============

# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input("Digite un número positivo: "))
while numero<0:
    print("Error -> Debería ser un número positivo")
    numero = int(input("Díigte un número positivo: "))

print(f"\nSu raíz cuadrada es: {math.sqrt(numero)}")

print(f"\nSu raíz cuadrada es: {math.sqrt(numero):.2f}")
