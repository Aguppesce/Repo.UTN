# ===============CLASE 05 - MARTES-13/09/2022===============
# Ejercicio 06: Tabla de multiplicar: Hacer un programa que pida un número por teclado y guarde en una lista su tabla de multiplicar hasta el 10. Por ejemplo: Si digita el 5 la lista tendrá, 5, 10 , 15, 20, 25, 30, 35, 40, 45, 50

numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"La tabla de multiplicar del {numero} es: ")
for i in range(0, 10 + 1):
    print(f"{numero}*{i}={numero*i}")

# OTRA SOLUCIÓN
lista = list(range(1,11))
print("Lista Original")
for i in lista:
    print(i, end=",")
valor = int(input("\nDigite un valor a multiplicar: "))
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f"Lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i, end=',')

# SOLUCIÓN CLASE
numero = int(input("Digite un número: "))
lista = [] # Creamos una lista vacía
for i in range(1, 11):
    lista.append(i*numero)

print(f"\nTabla de multiplicar del {numero}: \n {lista}")

for indice, i in enumerate(lista):
    print(f"{numero} x {i} = {lista[indice]}") # Este ciclo es oara ver el formato de una tabla de multiplicar