# =====================================CLASE 7 - MIERCOLES-01/06/2022=====================================

#Ejercicio 5: Sistema de calificaciones

nota = int(input('Ingrese calificación: '))
califcacion = None

if (nota >= 9 and nota <= 10):
    califcacion = 'A'
elif (nota >= 8 and nota < 9):
    califcacion = 'B'
elif (nota >= 7 and nota < 8):
    califcacion = 'C'
elif (nota >= 6 and nota < 7):
    califcacion = 'D'
elif (nota >= 0 and nota < 6):
    califcacion = 'F'
else:
    califcacion = 'No existe una calificación para esa nota'

print(f"La nota es: {nota} y la califación es: {califcacion}")