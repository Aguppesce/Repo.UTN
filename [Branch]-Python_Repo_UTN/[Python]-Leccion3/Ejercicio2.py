# ===============CLASE 9 - MIERCOLES-15/06/2022===============
# EJERCICIO 2
# Calcular la suma de N primeros números

num = int(input("Ingrese un número: "))
suma = 0
for i in range(1, num+1):
    print(f'La suma de {i} + {suma} es: {suma+i}')
    suma = suma + i

print(f'Suma final = {suma}')
