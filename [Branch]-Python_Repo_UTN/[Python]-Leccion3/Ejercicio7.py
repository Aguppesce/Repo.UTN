# ===============CLASE 10 - MIERCOLES-22/06/2022===============
# EJERCICIO 7
# Dadas las horas trabajadas de 5 personas y la tarifa de pago, calcular el salario, y la sumatoria de todos
# los salarios

print("Programa que calcula el salario de 5 personas y la sumatoria de sus salarios")

salario, suma = 0, 0

for i in range(1, 5+1):
    print(f'======>PERSONA {i}<======')
    tarifa = int(input(f'Tarifa: '))
    hora = int(input(f'Horas: '))
    salario = tarifa*hora
    suma = suma+salario
    print(f'Salario: {salario}')

print(f'\nLa suma de todos los salarios es: {suma}')