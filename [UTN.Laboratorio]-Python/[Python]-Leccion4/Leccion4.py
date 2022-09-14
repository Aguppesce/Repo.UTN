# ===============CLASE 01 - MARTES-16/08/2022===============
# COLECCIONES-LISTAS: Listas corresponden a "Colecciones" en Python. Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

# lista = Ariel, Liliana, Natalia, Osvaldo
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']

print(nombres)  # Muestra la lista completa

print(nombres[0])  # Muestra un elemento según la posición indicada
print(nombres[1])
print(nombres[2])
print(nombres[3])

print(nombres[-1])  # Muestra solo el último elemento de la lista
print(nombres[-2])  # Muestra el ante penúltimo elemento de la lista

print(nombres[0:2])  # Solo muestra el índice 0, 1 pero no el índice 2

print(nombres[:3])  # Ir al inicio de la lista al indice (sin incluirlo)

print(nombres[1: 0])  # Desde el indice indicado hasta el final

nombres[2] = 'Liliana'  # Modificamos un valor
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista
for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres))  # len es una función que nos devuelve la cantidad de elementos que tiene una lista

# Agregar un elemento
nombres.append('Marcelo')
nombres.append([1, 2,
                3])  # Dentro de una lista pueden haber diferentes tipos de datos, también dentro de una lista puede haber otras listas
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Insertar un elemento en un índice específico
nombres.insert(1, 'Alberto')  # Primero es la posición del índice y luego el elemento
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un índice esepecífico
del nombres[2]  # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres)  # Nos devolverá un error, el cual nos dice que la lista "nombres" no está declarada.

# TUPLAS
# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamoche corchetes no paréntesis
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:1])

# Ejemplo
verduras = (
    'papa',)  # Una tupla necesita aunque sea de un elemento: la coma, de lo contrario solo sería un tipo string cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar,
          end=' ')  # Print esta usando \n para saltos de línea, si ponemos "end=' '" en lugar de hacer un salto de línea se escribirá un espacio entre cada elemento y en una sola línea

cocinaLista = list(cocina)  # Conversión de una tupla a una lista
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)  # Conversión de una list a una tupla
print('\n', cocina)

# "del cocina" #esto es para eliminar la tupla

# ===============CLASE 02 - MARTES-23/08/2022===============
# COLECCIONES-CONJUNTOS PARTE 2

# Tipo set
planetas = {"Martes", "Jupiter", "Venus"}
print(len(planetas))  # Usamos la función len = length significa "largo"

# Revisar si un elemento existe dentro de set
print("marte" in planetas)  # Nos devuelve falso
print("Marte" in planetas)  # Nos devuelve true

# Agregar un elemento
planetas.add("Tierra")  # "add" es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Jupiter")  # Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("Tierra")  # Está función no nos presenta ningún tipo de error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
# print(planetas)  # Al eliminar nos muestra un error

# "Maradona":10 Un diccionario está compuesto por dos elementos: Una LLAVE y un VALOR
# dict(key,value)

diccionario = {
    "IDE": "Integrated Development Environment",
    "POO": "Programación Orientada a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"
}

# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:  # Recorremos mostrando solo las llaves
    print(termino)

# KEY AND VALUE
# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# KEY
# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():  # Estamos usando una función
    print(termino)  # Muestra solo las llaves

# VALUE
for valor in diccionario.values():  # Usamos una función para acceder al valor
    print(valor)

# Comprobar la existencia de algún elemento
print("IDE" in diccionario)  # Devuelve un booleano

# Agrega un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario  # el diccionario se borró

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

# Función extend
lista3.extend([7, 8, 9, 1])  # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # Función para ubicar en que índice esta el valor ingresado
# print(lista3.index(0)) # Nos da un error por no ser el elemento de la lista

# En una lista pueden haber errores repetidos. Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(
    1))  # Cuenta cuantos valores iguales hay dentro de la lista. Nos devolverá 4, ya que el 1 se repite 4 veces

# Para poner al revés una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
# Método Sort: ordena los elementos de forma ascendente
lista3.sort()
print(lista3)

lista3.sort(reverse=True)  # Ordena descendentemente
print(lista3)

# Repaso tuplas
# LAS TUPLAS SON LISTAS INMUTABLES(NO SE PUEDEN MODIFICAR)
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, "Hola")  # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)  # Acción booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentor de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# ===============CLASE 03 - MARTES-30/08/2022===============
# COLECCIONES-CONJUNTOS PARTE 3

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()  # Con set es la única manera de inicializarlo vacío
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(
    3 not in conjunto1)  # Preguntamos si el número 3 está en el conjunto (esto nos devolverá un valor booleano: true o false)

# Como hacer la igualdad de dos conjuntos
print(
    conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano ( nos devuelve false ya que conj1 no es igual a conj)

# Operaciones en conuntos
conjunto3 = conjunto1 | conjunto2  # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # Que elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # Asigna el valor que está en el conjunto 1 no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))  # Saber si el conjunto2 es un subconjunto del conjunto3
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(
    conjunto1))  # Preguntamos si los elementos del conjunto1 están dentro del conjunto3. Si es verdadero quiere decir que el conjunto 3 es un superconjunto
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2))  # No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Tuplas son inmutables. Para crearlas usamos parentesís. Son desordeandas
# Listas son mutables. Para crearlas usamos corchetes. Son ordenadas(es decir quitan los elementos que están repetidos)
# Conjunto o tipo set son mutables. para crearlas utilizamos llaves. Son desordenadas
# Diccionarios. Son ordenados

# Repaso diccionarios
diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde": "Green", "Amarillo": "Yellow"}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Ariel": {"Edad": 40, "Altura": 1.83}, "Osvaldo": [45, 1.85], "Natalia": [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di María", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    21: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    27: {"Nombre": "Julián Álvarez", "Edad": 22, "Altura": 1.73, "Precio": "51 Millones", "Posicion": "Delantero"},
    25: {"Nombre": "Lisandro Martínez", "Edad": 24, "Altura": 1.75, "Precio": "65 Millones", "Posicion": "Defensa"},
    5: {"Nombre": "Rodrigo De Paul", "Edad": 28, "Altura": 1.80, "Precio": "40 Millones", "Posicion": "Centrocampista"},
    22: {"Nombre": "Lautaro Martínez", "Edad": 25, "Altura": 1.74, "Precio": "25 Millones", "Posicion": "Delantero"}
}
print(seleccionArgentina)
print(seleccionArgentina[10])

# Recorremos el Diccionario seleccionArgentina
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end="")
print(len(seleccionArgentina))


# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()
elementoBorrado = pila() # Quita el elemento y lo guarda en la variable
print(pila)

print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila quedo así {pila}')

# Colas con listas
# Estructuras de datos de tipo fifo(first input / first output)
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]

# Agregamos elementos al final de la cola
cola.append("Natalia")
cola.append("José")
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# ===============CLASE 04 - MARTES-06/09/2022===============

for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")