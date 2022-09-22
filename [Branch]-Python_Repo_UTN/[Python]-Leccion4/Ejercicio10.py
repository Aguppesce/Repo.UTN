# ===============CLASE 06 - MARTES-20/09/2022===============

# Ejercicio 10: No repetir caracteres: Hacer un programa que pida una cadena por teclado, luego meter en una lista sin repetir caracteres

# SOLUCIÓN CLASE

cadena = (input("Introduzca una palabra: "))
lista = []

for i in cadena:
    if i not in lista: # Si el caracter aun no esta en la lista
        lista.append(i) # Lo agregamos a la lista

print(f"\nLista de caracteres sin repetir ningun: \n {lista}")

# SOLUCIÓN 1
cadena = input("Ingrese una cadena: ")
cadena = list(set(list(cadena)))
print(cadena)

# SOLUCIÓN 2
print(list(set(list(input("Ingrese una cadena: ")))))
