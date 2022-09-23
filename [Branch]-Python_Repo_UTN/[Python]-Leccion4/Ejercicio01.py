# ===============CLASE 04 - MARTES-06/09/2022===============
# Ejercicio 01: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for, los elementos deben mostrarse de la siguiente forma: 1-2-3-4-5-...50

lista = []
for i in range(0, 50 + 1):
    lista.append(i)
print(lista)

# SOLUCIÓN CLASE
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i, end="-")

# Solución 2 en Clase
lista = list(range(1,51)) #Algoritmo eficaz, resultado en 5 líneas a una
for i in lista:
    print(i, end="-")