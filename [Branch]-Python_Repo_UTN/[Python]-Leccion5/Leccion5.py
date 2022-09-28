# ===============CLASE 05 - MARTES-13/09/2022===============

# Comenzamos con Funciones
# mi_funcion() # No se puede llamar antes de definir a una función
# Definimos una función
def mi_funcion():  # Para identificar a la función utilizamos paréntesis
    print("Saludos a todos los alumnos de la Tecnicatura")


mi_funcion()  # Estamos llamando a la función
mi_funcion()  # Se puede llamar a una función N cantidad de veces


# ===============CLASE 06 - MARTES-20/09/2022===============

# Desempaquetado de lsitas o list Unpacking
def show(name, lastName):
    print(name + " " + lastName)


person = ["Ariel", "Betancud"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la función
show(*person)  # Esto es lo mismo que lo anterior pero le pasamos toodo junto
person2 = ("Osvaldo", "Giordadini")  # Desempaquetado a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]  # Aun con el la lista vacía se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break  # Esta es la única manera para que no se ejecute el else
else:
    print("Esto se termina")

# List comprenhension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"]  # Esto regresa una nueva lista

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}, ]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)


# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a través del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")


mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")


# La palabra return en funiones
# Creamos una función para sumar
def sumar(a, b):
    return a + b


# resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")


# def sumar2(a:int = 0, b:int = 0)-> int: # Función redundante, se puede simplificar (Ver línea 72)
def sumar2(a=0, b=0):  # Le damos un valor por default
    return a + b


resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normlamente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres("Lucas","José","Claudia","Rosa","María")
listarNombres("Marcos","Daniel","Romina","Pepe","Marcela","Carlos")

# ===============CLASE 07 - MARTES-27/09/2022===============

def listarTerminos(**terminos): # Los más utilizado es **kwargs para recibir argumentos
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

listarTerminos() # Si pasamos una función vacía, no muestra nada ya que no le hemos pasado ningún argumento
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
# listarTerminos(10='Leonel Messi') # La key tiene que ser un String, ya que no permite
listarTerminos(Nombre='Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ["Tito","Pedro","Carlos"]
desplegarNombres(nombres2) # Muestra
desplegarNombres("Carla") # Muestra cada elemento por separado, es decir (C, a , r...)
# desplegarNombres(10,11) # Devolverá un error diciendo que no son objetos iterables

desplegarNombres((10,11)) # Al ser una tupla, cuando tenemos dos parentesís (()) estamos convirtiendolo a una tupla lo cual nos permite recorrerla con la función

desplegarNombres([22,55]) # Al ser una lista ( con corchetes [] estamos convirtiendolo a una lista, esto permite que la función funcione)

# Funciones Recursivas
def factorial(numero): #Para una función recursiva se necesitan dos faces: caso base y caso recursivo
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo

resultado = factorial(5) #Lo hacemos en código duro
print(f"El factorial del número 5 es: {resultado}")

# Como tarea: hacer que el usuario ingrese el número para calcular el factorial

def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo
numeroFactorial = int(input("Digite el número para calcular el factorial: "))
resultado = factorial(numeroFactorial)
print(f"El factorial del número 5 es: {numeroFactorial} es : {resultado}")