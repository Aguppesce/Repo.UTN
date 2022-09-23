'''Sintaxis de range (inicio<opcional>, fin <requerido>, incremento<opcional>)

Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
#Ejemplo de ejecución: 0,3,6,9

Ejercicio 2: Crear un rango de números de 2 a 6 a imprimelos
#Ejemplo de ejecución: 2,3,4,5,6

Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
#Ejemplo de ejecución: 3,5,7,9
'''

# Ejercicio 1
print('Ejercicio 1: ')
for rango in range(11):
    if rango % 3 == 0:
        print(rango)

# Ejercicio 2
print('Ejercicio 2: ')
for rango in range(2,7):
    print(rango)

'''# Ejercicio 2: Solución profesor
print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2,7)
for i in rango:
    print(i)'''

# Ejercicio 3
print('Ejercicio 3: ')
rangos = [3, 4, 5, 6, 7, 8, 9, 10]
for rangos in range(3,10,2):
    print(rango)

'''# Ejercicio 3: Solución profesor
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
for i in range(3, 11, 2):
    print(i)'''