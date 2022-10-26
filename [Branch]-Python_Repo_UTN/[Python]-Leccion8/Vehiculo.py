# ===============CLASE 11 - MARTES-25/10/2022===============

class Vehiculo:
    '''
    Definir una clase padre llamada Vehículo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales hereda de la clase padre Vehículo. La clase padre debe tener los siguientes atributos y métodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -Métodos(__init__(color, ruedas) y __str__())

    Auto(clase hija de Vehículo)
    -Aitrubtos(velocidad (km/hr))
    -Métodos(__init__(color, ruedas, velocidad) y __str__())

    Bicicleta(clase hija de Vehículo)
    -Atributos(tipo(urbana/montaña/etc.)
    -Métodos(__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color " + self.color + " Ruedas: " + str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+", Velocidad(km/hr): "+ str(self.velocidad)

class Bicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+", Tipo: "+str(self.tipo)

# Primer objeto de la clase padre Vehículo
vehiculo = Vehiculo("Blanco", 4)
print(vehiculo)

# Segundo objeto, pero ahora de la clase Auto
auto = Auto("Amarillo", 4, 120)
print(auto)

# tercer objeto de la clase Bicicleta
bici = Bicleta("Azul", 2, "urbana")
print(bici)