# ===============CLASE 12 - MARTES-01/11/2022===============

from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

print("Creación de objeto clase Cuadrado".center(50,'_'))
cuadrado1 = Cuadrado(8, "Azul")
cuadrado1.alto = 7
cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Methos Resolution ORder
# print(Cuadrado.mro())

print(cuadrado1)
print("Creación de objeto clase Rectangulo".center(50,'_'))
rectangulo1 = Rectangulo(3, 9, "verde")
rectangulo1.ancho = 8
print(f"Calculo del área del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

# figura1 = FiguraGeometrica() # No se puede instanciar, es abstracta
print(Cuadrado.mro())