# ===============CLASE 10 - MARTES-18/10/2022===============

class Persona2:
    def __init__(self,nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property # decorador
    def nombre(self): # Método Getter
        # print("Estamos utilizando el método get del atributo nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # Método Setter
        # print("Estamos utilizando el método set del atributo nombre")
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Método Getter
        # print("Estamos utilizando el método get del atributo apellido")
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método Setter
        # print("Estamos utilizando el método set del atributo apellido")
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Método Getter
        # print("Estamos utilizando el método get del atributo edad")
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método Setter
        # print("Estamos utilizando el método set del atributo edad")
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

if __name__ == '__main__':
    persona1 = Persona2("Ariel", "Betancud", 41)
    print(persona1.nombre) # Llamamos al método getter
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = "Juan Pedro" # Llamamos el método setter
    print(persona1.nombre) #Otra vez con el método getter
    print(persona1.mostrar_detalles()) # Llamamos el método mostrar_detalles
    persona1._edad = 40
    #Atributo read-only(solo lectura) sería la edad porque no tiene el método set
    print(persona1.edad)

    # Tarea crear tres objetos más, utilizando los métodos getter and setter para modificar y mostrar los cambios con el méotod mostrar_detalles

    persona2 = Persona2("Pedro", "Pérez", 22)
    persona2.mostrar_detalles()
    persona2.nombre = "Marcos"
    persona2.apellido = "Quintana"
    persona2.edad = 15
    # Mostramos el objeto 2 modificado
    persona2.mostrar_detalles()

    persona3 = Persona2("Monica", "Alvarez", 30)
    persona3.mostrar_detalles()
    persona3.nombre = "Maria"
    persona3.apellido = "Cortez"
    persona3.edad = 25
    # Mostramos el objeto 3 modificado
    persona3.mostrar_detalles()

    persona4 = Persona2("Camila", "Ramirez", 10)
    persona4.mostrar_detalles()
    persona4.nombre = "Andrea"
    persona4.apellido = "Rojas"
    persona4.edad = 41
    # Mostramos el objeto 4 modificado
    persona4.mostrar_detalles()

    # SOLUCIÓN CLASE

    # Objeto número uno de la tarea
    persona2 = Persona2('Flor','Romero',23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22
    print(persona2.mostrar_detalles())

    # Objeto número dos de la tarea
    persona3 = Persona2('Caro','Felisa',21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 31
    print(persona3.mostrar_detalles())

    # Objeto número tres de la tarea
    persona4 = Persona2('Naty','Lucer',35)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 33
    print(persona4.mostrar_detalles())

    print(__name__)