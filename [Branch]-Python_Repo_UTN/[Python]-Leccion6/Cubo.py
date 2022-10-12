# ===============CLASE 09 - MARTES-11/09/2022===============

class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto, y profundidad, con un método calcular_volumen que tendrá la fórmula: volumen = ancho * altura * profunidad
    que el usuario ingrese los valores
    """

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Ingrese ancho: "))
altura = int(input("Ingrese altura: "))
profundidad = int(input("Ingrese profundidad: "))

cubo = Cubo(ancho,altura,profundidad)

print(f"El volumen del cubo es: {cubo.calcular_volumen()}")

# SOLUCIÓN CLASE

class CuboClase:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Digite el ancho del cubo: "))
altura = int(input("Digite la altura del cubo: "))
profundidad = int(input("Digite la profundidad del cubo: "))

cubo1 = Cubo(ancho,altura,profundidad)

print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")
