# ===============CLASE 04 - MARTES-06/09/2022===============
# Ejercicio 02: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor ingresado por el usuario

# Solucion 1
lista = []
numero = int(input("Digite un número: "))

for i in range(0, 10 + 1):
    lista.append(numero * i)
for i in range(0, 10 + 1):
    print(f"{numero}*{i}={lista[i]}")

# Solución 2
print(f"La tabla de multiplicar del {numero} es: ")
for i in range(0, 10 + 1):
    print(f"{numero}*{i}={numero*i}")

# Solución Clase
lista = list(range(1,11))
print("Lista Original")
for i in lista:
    print(i, end="-")
valor = int(input("\nDigite un valor a multiplicar: "))
for indice, i in enumerate(lista): #Función para modificar los indices de la lista
    lista[indice] *= valor # El iterador solo recorre los índices, en esta línea se multiplica

print(f"Lista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i, end='-')