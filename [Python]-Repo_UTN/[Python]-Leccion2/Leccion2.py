# ===============CLASE 6 - MIERCOLES-11/05/2022===============
# SENTENCIAS DE CONTROL: SENTENCIA IF/ELSE + EJECUCIÓN DEBUG EN IF/ELSE

condicion = True
if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condición sin especificar')

# EJERCICIO: CONVERSIÓN DE NÚMERO A TEXTO
num = int(input('Digite un número en el rango del 1 al 3: '))
numTexto = ' '
if num == 1:
    numTexto = 'Número uno'
elif num == 2:
    numTexto = 'Número dos'
elif num == 3:
    numTexto = 'Número tres'
else:
    numTexto = 'Has ingresado un número fuera de rango'
print(f'El número ingresado es: {num} - {numTexto}')

# SINTAXIS SIMPLIFICADA (OPERADOR TERNARIO). Solo se recomienda usar si el código es muy pequeño, si hubise más lineas de código no es recomendable. En la sintaxis simplificada solo se utiliza el IF/ELSE (no se debe utilizar el ELIF)

condicion = False
if condicion:
    print('Condición Verdadera')
else:
    print('Condición Falsa')
print('Condicion Verdadera') if condicion else print('Condicion Falsa')

# ===============CLASE 7 - MIERCOLES-01/06/2022===============
# EJERCICIOS: 5,6 Y 7
