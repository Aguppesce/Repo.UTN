# ===============CLASE 06 - MARTES-20/09/2022===============

# Ejercicio 11: Hacer un programa que simule una agenda de contactos. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono, el programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

# SOLUCIÓN CLASE

agenda = {}

while True:
    print("1. Nuevo contacto\n2. Borrar contacto\n3. Ver contactos existentes\n4. Salir")
    opcion = (int(input("Ingrese su opcion: ")))
    if opcion == 1:
        nombre = (input("Nombre: "))
        telefono = (input("Telefono: "))
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente!")
        else:
            print("Este nombre de contacto ya existe")
    elif opcion == 2:
        nombre = (input("Nombre del contacto a borrar: "))
        if nombre in agenda:
            del(agenda[nombre])
            print("Se ha eliminado el contacto requerido")
        else:
            print("Este contacto no existe en la agenda")
    elif opcion == 3:
        print("Agenda de contactos: ")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Teléfono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos!")
        break
    else:
        print("Se equivoco de opción de menú")
    print()
