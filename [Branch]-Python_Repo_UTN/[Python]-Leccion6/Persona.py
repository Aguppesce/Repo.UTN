# ===============CLASE 08 - MARTES-04/09/2022===============

# En Python el constructor está oculto. Para poder inicializar los objetos depende del método __init__

class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, edad): # Se lo llama métdo Init Dunder. El (self) viene por default, a cotinuación escribimos los atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}") # Usamos self para acceder a los atributos de otro método

print(type(Persona))

persona1 = Persona("Ariel", "Betancud", 40) # Este es un constructor en Python
print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvaldo", "Giordadini", 45)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40

print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

# Los atributos son: características
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()
