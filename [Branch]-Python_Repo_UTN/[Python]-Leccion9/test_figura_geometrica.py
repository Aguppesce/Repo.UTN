# ===============CLASE 12 - MARTES-01/11/2022===============

from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, "Azul")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Methos Resolution ORder
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(3, 8, "verde")
print(f"Calculo del área del rectangulo: {cuadrado1.calcular_area()}")
print(rectangulo1)