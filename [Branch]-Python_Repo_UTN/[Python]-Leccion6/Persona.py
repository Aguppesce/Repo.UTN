# ===============CLASE 08 - MARTES-04/09/2022===============

# En Python el constructor está oculto. Para poder inicializar los objetos depende del método __init__

class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama métdo Init Dunder. El (self) viene por default, a cotinuación escribimos los atributos
        self.__nombre = nombre
        self.apellido = apellido
        self._dni = dni # Con "_" encapsulamos el atributo. Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # El uso de "self" es igual a "this"
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}") # Usamos self para acceder a los atributos de otro método

print(type(Persona))

persona1 = Persona("Ariel", "Betancud", 32456987, 40) # Este es un constructor en Python
print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvaldo", "Giordadini", 30321456, 45)
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

# ===============CLASE 09 - MARTES-11/09/2022===============

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dará error
persona1.telefono = "44445555289"
print(f"Este es el teléfono de: {persona1.nombre} {persona1.telefono}")  # Hemos creado un atributo de un objeto

# print(persona2.telefono) # Nos da un error ya que el objeto 2 no tiene este atributo

persona3 = Persona("Rogelio", "Romero", 35789456, 22, "Teléfono", 2614445557, "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto="Citroen", Modelo=2021)

persona3.mostrar_detalle()

# print(persona3._dni) # Esto no se debe utilizar(esta encapsulado) en python, esto dice que lo desconocemos

# persona3.__nombre # Esta totalmente encapsulado