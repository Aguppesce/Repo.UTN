# ===============CLASE 9 - MIERCOLES-15/06/2022===============
# EJERCICIO 4
# Suponga que se tiene un conjunto de calificaciones de un grupo de 10
# alumnos. Realizar un algoritmo para calcular la calificación promedio
# y la calificación más baja de toodo el grupo.

print("Programa para calcular el promedio")

promedio = 0
calBaja = 99999999

for i in range(10):
    num = int(input(f"Ingrese nota {i+1}/10: "))
    promedio = promedio + num
    if(num < calBaja):
        calBaja = num

print(f'Promedio de la clase: {promedio/10}'
      f'\nNota más baja: {calBaja}')

8















# OTRA SOLUCIÓN
# print("Programa para calcular el promedio")
#
# promedio = 0
# calBaja = 0
# anterior = 0
#
# for i in range(10):
#     num = int(input(f"Ingrese nota {i+1}/10: "))
#     if(num >= anterior):
#         promedio = promedio + num
#     else:
#         calBaja = num
#         promedio = promedio + num
#     anterior = num
#
# print(f'Promedio de la clase: {promedio/10}'
#       f'\nNota más baja: {calBaja}')
