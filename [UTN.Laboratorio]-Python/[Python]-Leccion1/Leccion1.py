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

# =====================================CLASE 4 - MIERCOLES-27/04/2022====================================='

'''operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f"El resultado de la suma es: {suma}")
resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación es: {multiplicacion}")
division = operandoA / operandoB
print(f"El resultado de la división es: {division}")
division = operandoA // operandoB
print(f"El resultado de la división (int) es: {division}")
modulo = operandoA%operandoB
print(f"El resultado de la división o residuo(modulo) es: {modulo}")
exponente=operandoA**operandoB
print(f"El resultado del exponente es: {exponente}")

# Ejercicio 1 de clase
alto=int(input("Ingrese alto: "))
ancho=int(input("Ingrese ancho: "))

print("El área es: ", alto*ancho)
print("El perímetro es: ", (alto+ancho)*2)

miVariable3=10
print(miVariable3)

# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 2
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

d = 4
b = 4 # Cambiar valor para alternar el resultado
resultado = d == b # Comprobamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador Mayor que
resultado = d > b
print(resultado)

# Operador Menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)

# Ejercicio 2 de clase
numero = int(input("Ingrese un número "))
print(f"El residuo de la división es: {numero%2}")
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

# Ejercicio 3 de clase
if numero >= int(input("Ingrese un número: ")) >= 18:
    print(f"Tienes {numero} eres mayor de edad")
else:
    print(f"Tienes {numero} eres menor de edad")'''

# =====================================CLASE 5 - MIERCOLES-04/05/2022=====================================
'''# Operadores lógicos

# Operador and
a = True
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)

# Ejercicio 1 de clase -> Operador and
numero = int(input("Ingrese un número "))
if numero > 0 and numero < 5: # 0 <= num <=5 || otra forma: num = int(input("Ingrese un numero : "))print(num>=0 and num<=5)
    print(f"El numero esta dentro del rango")
else:
    print(f"El numero esta fuera del rango")

# Ejercicio 2 de clase -> Operadores or y not
vacaciones = False # alternar valores para variar el resultado
diaDescanso = False
if not(vacaciones or diaDescanso):
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')

# Ejercicio 3 de clase
edad = int(input("Cuál es su edad? "))
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print(f"Esta dentro del rango")
else:
    print(f"Esta fuera del rango")

    # Solución 1 clase
edad = int(input("Digite su edad: "))
veinte = edad>=20 and edad<30
print(veinte)
treinta = edad >= 30 and edad < 30
print(treinta)
if veinte or treinta:
    print('Estas dentro del rango de los (20\'0) a (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")

    # Solución 2 clase
if veinte or treinta:
    if veinte:
        print('Esta dentro del rango de los (20\'0) años')
    elif treinta:
        print('Esta dentro del rango de los (30\'0) años')
    else:
        print('No estas dentro del rango')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")

    # Soluión 3 clase: sintaxis simplificada
if (20 <= edad < 30) or (30 <= edad < 40):
    print(f"Esta dentro del rango")
else:
    print(f"Esta fuera del rango")

# Ejercicio 4 de clase
num1 = int(input("Digite numero 1: "))
num2 = int(input("Digite numero 2: "))

if(num1 > num2):
    print(f"El número {num1} es el mayor")
elif ( num2 > num1 ):
    print(f"El número {num2} es el mayor")

# Ejercicio 5 clase: Tienda de libros
print("Ingrese los siguientes datos del libro")
nombre = input("Nombre del libro: ")
idLibro = int(input("ID del libro: "))
precioLibro = int(input("Precio del libro: "))
envioGratis = input("Envio gratis (S/N): ")
if (envioGratis == 'S'):
    envioGratis = True
elif (envioGratis == 'N'):
    envioGratis = False
else:
    envioGratis = "Dígito inválido"

print(f"Nombre: {nombre}\nID: {idLibro}\nPrecio: ${precioLibro}\nEnvio Gratis: {envioGratis}")

edad = 65

if edad < 18 or edad > 64:
    print('Tienes descuento')

if-else(and)

if-else(or)

if-else(not)

if-elif-else

if-if-elif-else-else

if(and)(or)(and)'''