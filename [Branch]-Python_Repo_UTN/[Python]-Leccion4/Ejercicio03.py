# ===============CLASE 04 - MARTES-06/09/2022===============
# Ejercicio 03: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario introduzca un número 0, nuestro programa dejaría de insertar. Por último, mostrar los números ordenados de menor a mayor

# SOLUCIÓN CLASE
lista = []
banderaSalir = False
while not banderaSalir:  # Al poner el operador "not" estamos cambiando el valor de banderaSalir a "True"
    numero = int(input("Ingrese un número: "))
    if numero == 0:
       banderaSalir = True
    else:
       lista.append(numero)

print(lista)

print("Lista con la función sort() aplicada")
lista.sort() # La lista está ordenada con esta función
print(lista)
