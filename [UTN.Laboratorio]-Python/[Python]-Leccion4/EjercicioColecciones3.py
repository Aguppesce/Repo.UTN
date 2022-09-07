# ===============CLASE 04 - MARTES-06/09/2022===============

# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Humano

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos una lista

# Creamos diccionarios
P = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del Norte"}
personajes.append(P)
P = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P)
P = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P)
P = {"Nombre": "Galadriel", "Clase": "Hechicera", "Raza": "Elfo Noldor"}
personajes.append(P)
P = {"Nombre": "Frodo", "Clase": "Guerrero", "Raza": "Hobbit"}
personajes.append(P)
P = {"Nombre": "Eowyn", "Clase": "Guerrera", "Raza": "Rohir"}
personajes.append(P)

print(personajes)
