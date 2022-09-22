# ===============CLASE 05 - MARTES-13/09/2022===============
# Ejercicio 08: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo inicial de 1000$ y tendrá el siguiente menú de opciones:
# 1. Ingresa dinero en la cuenta.
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible.
# 4. Salir

saldoActual = 1000
print("1. Ingresa dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Su opción: "))

while opcion != 4:
    if opcion == 1:
        agregarDinero = float(input(f"Su saldo actual es de {saldoActual}$. Cuánto dinero quiere agregar?: "))
        saldoActual = saldoActual + agregarDinero
        print(f'Su saldo actual es de {saldoActual}$')
    if opcion == 2:
        retirarDinero = float(input(f"Su saldo actual es de {saldoActual}$. Cuánto dinero quiere retirar?: "))
        while retirarDinero >= saldoActual:
            print("Monto que quiere retirar es superior a lo que tiene actualmente")
            retirarDinero = float(input(f"Ingrese una cantidad válida de dinero: "))
        saldoActual = saldoActual - retirarDinero
        print(f"Su saldo actual es de {saldoActual}$")
    if opcion == 3:
        print(f"Saldo Actual: {saldoActual}$")
    if opcion == 4:
        break
    else:
        print("Opción inválida. Vuelva a intentar")
    opcion = int(input("Su opción: "))

print("Vuelva pronto!")

# SOLUCIÓN CLASE
saldo = 1000
while True:
    print("1. Ingresa dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Su opción: "))
    print()
    if opcion == 1:
        extra = float(input("Cuánto dinero desea ingresar -> "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retirar = float(input("Cuánto dinero desea retirar ->"))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automático, hasta pronto")
        break
    else:
        print("Error, se equivoco de opción de menú")
        print()