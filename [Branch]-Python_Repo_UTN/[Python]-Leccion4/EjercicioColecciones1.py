# ===============CLASE 04 - MARTES-06/09/2022===============

# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos una lista

lista = [13, 1, 8, 3, 2, 5, 8, 1, 2, 3, 5]
conjunto = set(lista) # Se convierte la lista a conjunto de tipo set
lista = list(conjunto) # Se convierte el conjunto a lista

# lista = list(set(lista)) # Ejercicio en una sola línea
# print(set[1,1,2,2]) # Otro método en una sola línea

print(lista)


# SOLUCIÓN CLASE
lsita = [1,2,3,"Ariel",7,7,3,"Alberto",1,"Ariel",2,"Alberto"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
# lista = lista(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversión hecha en una sola línea de código (eficiente)
print(lista)