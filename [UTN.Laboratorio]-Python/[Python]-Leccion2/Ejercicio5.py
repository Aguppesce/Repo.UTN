# ===============CLASE 7 - MIERCOLES-01/06/2022===============
# EJERCICIO 3: Calcular estación del año

mes = int(input("Ingrese un mes del año: "))

if (mes >= 1 and mes <= 3):
    print('Es verano')
elif (mes > 3 and mes <= 6):
    print('Es otoño')
elif (mes > 6 and mes <= 9):
    print('Es invierno')
elif (mes > 9 and mes <= 12):
    print('Es primavera')
else:
    print('Mes incorrecto. Debe ser entre 1 y 12')