# ===============CLASE 07 - MARTES-27/09/2022===============

# Ejercicio 05: Convertidor de temperaturas. Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa. Investigar las fórmulas.

def convertFahrenheitToCelsius(temperatura):
    return (temperatura * 1.8) + 32


def convertCelsiusToFahrenheit(temperatura):
    return (temperatura - 32) / 1.8

numeroUsuario = int(input("Ingrese temperatura: "))
print(f'"Temperatura en Farhenheit: {convertFahrenheitToCelsius(numeroUsuario)}°F')

print(f"Temperatura en Celsius: {convertCelsiusToFahrenheit(numeroUsuario)}°C")



# SOLUCIÓN CLASE
# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia: multiplicación, división y suma

# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respetar la presedencia utilizando parentesís

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C a F -> {resultado:.2f}") #{resultado:.2f} para darle un formato al resutlado y que se muestren solo 2 dígitos después de la coma/punto

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado:.2f}")