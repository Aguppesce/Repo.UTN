# ===============CLASE 07 - MARTES-27/09/2022===============

# Ejercicio 03: Función Recursiva. Imprimir números de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir: 5,4,3,2,1. En caso de ser el número 3 debe imprimir: 3,2,1. Si se ingresan números negativos no imprime nada.

def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

imprimir_numeros_recursivos(5) # Tarea: que el número lo ingrese el usuario

numeroUsuario = int(input("\n\nIngrese un número: "))
imprimir_numeros_recursivos(numeroUsuario)