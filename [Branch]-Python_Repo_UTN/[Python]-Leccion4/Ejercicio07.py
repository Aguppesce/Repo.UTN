# ===============CLASE 05 - MARTES-13/09/2022===============
# Ejercicio 07: Juego adivina el número: Realizar un juego par adivinar un número. Para ello se debe generar un número aleatorio entre 1 - 100, y luego ir pidiendo número indicando "es mayor" o "es menor" según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta y allí se debe mostrar el número de intentos.
import random

numeroAleatorio = random.randint(0, 100)
contador = 0
numeroUsuario = int(input("Ingrese su número: "))

while numeroUsuario != numeroAleatorio:
    if (numeroUsuario < numeroAleatorio):
        print("Es menor")
        contador += 1
        numeroUsuario = int(input("Vuelva a ingresar un número: "))
    else:
        print("Es mayor")
        contador += 1
        numeroUsuario = int(input("Vuelva a ingresar un número: "))

print(f"Ha ganado. Número de intento {contador}")

# SOLUCIÓN CLASE
print("\t.:Juego Adviniva el número:.")
aleatorio = random.randint(0, 100)  # Toma de 0 a 100 literal, generamos un número aleatorio
contador = 0
while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, digite un número menor")
    elif numero > aleatorio:
        print("\tNo es el número, digite un número mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el número {aleatorio}")
        break # Rompe el ciclo y el bucle
print(f"\nNúmero de intentos: {contador}")