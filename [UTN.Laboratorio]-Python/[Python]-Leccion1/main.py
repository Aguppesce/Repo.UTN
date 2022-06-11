# =====================================CLASE 1 - MIERCOLES-06/04/2022====================================='

"""print("Hola Mundo")"""

# =====================================CLASE 2 - MIERCOLES-13/04/2022====================================='

'''miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2 # Literal de tipo numérico
z = x + y
# Las literales se escriben x240, la variable y=x984, la variable z=x304
print(id(x)) # Para ver la dirección de memoria
print(id(y))
print(id(z))'''

# =====================================CLASE 3 - MIERCOLES-20/04/2022====================================='

'''a = False # Esta es una variable literal de tipo booleana
print(type(a))
#Tipos int, float, String, Bool
print(x)
print(type(x))
x=14.5
print(x)
print(type(x))
x="Hola Alumnos"
print(type(x))
x=True
print(type(x))
x=False
print(type(x))
#Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black"+" "+"The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito)

# Otra forma de concatenar
miGrupoFavorito = "The Letter Black: ""The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito)

miGrupoFavorito = "The Letter Black: "
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito+" "+caracteristicas)

# Otra forma de concatenar
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(numero1+numero2)

# Convertimos String a Int
print(int(numero1) + int(numero2))
# Nota: Solo puede sumar si los números declarados como String son números.
#       Por ejemplo si escribimos "siete" no se podrá sumar.

# Tipos de datos Boole
miBooleano = True # Valor literal para true
print(miBooleano)

miBooleano = 1 > 2
print(miBooleano)
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# función input

resultado = input("Digite un número: ")  # La función input regresa un dato tipo string
print(resultado)

# Conversión de la entrada de datos (de input)
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2

print("El resultado de la suma es: ", resultado)

Ejercicio 1
puntuacionDia = int(input("¿Cómo estuvo tu día? (1 al 10): "))
if puntuacionDia <= 10 and puntuacionDia >= 1:
    print("El día estuvo de ", puntuacionDia)
else:
    print("La puntuación tiene que ser entre 1 y 10")

#Ejercicio 2
titulo = input("Proporcione el título: ")
autor = input("Proporcione el autor: ")
print(titulo + " fue escrito por "+ autor)'''