# ===============CLASE 09 - MARTES-11/09/2022===============

class Rectangulo:
    """
    Crear una clase llama Rectangulo, debe tener 2 atributos: altura y base el nombre del método será calcular área utilizando la fórmula:
    area = base * altura. Pero la base y la altura deber ser ingresadas por el usuario y los objetos deben ser tres
    """

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

rectangulo1 = Rectangulo(0,0)
rectangulo2 = Rectangulo(0,0)
rectangulo3 = Rectangulo(0,0)

rectangulo1.altura = float(input(f"Ingrese altura del rectángulo 1: "))
rectangulo1.base = float(input(f"Ingrese base del rectángulo 1: "))
print(f"El área del rectángulo 1 es: {rectangulo1.calcular_area()}")

rectangulo1.altura = float(input(f"Ingrese altura del rectángulo 2: "))
rectangulo1.base = float(input(f"Ingrese base del rectángulo 2: "))
print(f"El área del rectángulo 2 es: {rectangulo1.calcular_area()}")

rectangulo1.altura = float(input(f"Ingrese altura del rectángulo 3: "))
rectangulo1.base = float(input(f"Ingrese base del rectángulo 3: "))
print(f"El área del rectángulo 3 es: {rectangulo1.calcular_area()}")

# SOLUCIÓN CLASE

class RectanguloClase:

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

base = int(input("Digite el número para la base del rectángulo: "))
altura = int(input("Digite el número para la altura del rectángulo: "))
rectangulo1 = RectanguloClase(base,altura)
print(f"El área del rectángulo es: {rectangulo1.calcular_area()}")