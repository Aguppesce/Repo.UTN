# ===============CLASE 1 - MARTES-16/08/2022===============
# COLECCIONES-LISTAS
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
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento: la coma, de lo contrario solo sería un tipo string cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') #Print esta usando \n para saltos de línea, si ponemos "end=' '" en lugar de hacer un salto de línea se escribirá un espacio entre cada elemento y en una sola línea

cocinaLista = list(cocina) #Conversión de una tupla a una lista
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista) #Conversión de una list a una tupla
print('\n', cocina)

#del cocina #esto es para eliminar la tupla