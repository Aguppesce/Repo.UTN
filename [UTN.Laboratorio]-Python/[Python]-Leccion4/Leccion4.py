# ===============CLASE 1 - MARTES-16/08/2022===============
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

# ===============CLASE 2 - MARTES-23/08/2022===============
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
