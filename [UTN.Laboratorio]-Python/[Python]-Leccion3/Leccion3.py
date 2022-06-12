# =====================================CLASE 8 - MIERCOLES-01/06/2022=====================================

'''#CICLO WHILE (MIENTRAS O DURANTE)
contador = 0
while contador < 78:
    print('Ejecutando nuestro ciclo while ', contador)
    contador += 1
else:
    print('Fin del ciclo while')

#IMPRIMIR NÚMERO DEL 0 AL 5 CON EL CICLO WHILE
maximo = 5
contador = 0

while contador <= maximo:
    print(contador)
    contador += 1

# CICLO WHILE DESCENDENTE
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

# CILCO FOR
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

# PALABRA RESERVADA BREAK
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
    else:
        print('Fin del ciclo for')'''

# PALABRA RESERVADA CONTINUE
for i in range (6):
    if i % 2 == 0:
        print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
        print(f'Valora: {i}')


