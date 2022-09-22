# ===============CLASE 05 - MARTES-13/09/2022===============

# Ejercicio 05: Hace un programa para calcular el factorial de un número positivo

numero = int((input("Ingrese un número: ")))
factorial = 0
for i in range(numero,1):
    print(f'Factorial de {i} * {i-1}={i*(i+1)}')

print(f"Total={factorial}")

# SOLUCIÓN CLASE
numero = int(input("Digite un número: "))
while numero < 0: #Mientras el número sea negativo
    print("Error -> El número tiene que ser positivo")
    numero = int(input("Dígite un número: "))
factorial = 0 # la variable para calcular el factorial
for i in range(1, numero +1):
    factorial *= i
print(f"\nEl factorial del número {numero} positivo ingresado es: {factorial}")

# OTRA SOLUCIÓN
num = int(input())
f = 1
for i in range(2, num + 1):
    f += i

print(f)

#OTRA SOLUCIÓN
numero = int(input("Ingrese un número positivo: "))
factorial = 1
if numero < 0:
    print("Error: el número debe ser positivo.")
else:
    for i in range(1, numero+1):
        factorial = factorial * i
    print("El factorial de: ", numero, " es ", factorial)

# OTRA SOLUCIÓN
numero = (input("Ingrese un número: "))
factorial = 0

for i in range(numero-1):
    i += 1
    numero *= i
    print(numero)

print(f"Total={factorial}")



