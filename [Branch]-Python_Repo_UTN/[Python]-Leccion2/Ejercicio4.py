# ===============CLASE 6 - MIERCOLES-11/05/2022===============
# EJERCICIO 4:
# Área y longitud de un círculo
# Hacer un programa para ingresar el radio de un círculo y se reporte su área y la longitud de la circunferencia
# Área= Pi*2 | Longitud= 2*Pi*r
# En este ejercicio vamos a necesitar importar el módulo math porque tiene el valor de Pi
# Se escribe import math

import math

radio = float(input("Ingrese radio: "))
area = math.pi * (radio * radio)
longitud = 2 * math.pi * radio
print(f'El área del círculo con radio {radio} es: ', area)
print(f'La longitud del círculo con radio {radio} es: ', longitud)





