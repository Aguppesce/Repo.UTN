# ===============CLASE 10 - MARTES-18/10/2022===============
from Persona2 import Persona2 # Al reemplazar "Persona2" después del import, por asterisco (*) estamos importando toodo

print('Creación de objetos'.center(50,'-'))
if __name__ == '__main__':
    persona5 = Persona2("Lionel", "Messi", 35)
    persona5.mostrar_detalles()

    print(__name__) # Nos muestra en consola desde donde se está ejecutando el código

print("Eliminación de Objetos".center(50,'-'))
del persona5