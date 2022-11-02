# ===============CLASE 12 - MARTES-01/11/2022===============

from FiguraGeometrica import FiguraGeometrica # Primero indicamos de donde (from) vamos a importar módulo o archivo (FiguraGeometrica) luego que es lo que vamos a importar la calse de ese módulo (FiguraGeometrica)
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado) # Esto puede generar confunsión
        FiguraGeometrica.__init__(self, lado, lado) # Esta es la forma correcta
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"