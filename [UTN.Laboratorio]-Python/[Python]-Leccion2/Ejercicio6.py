# =====================================CLASE 7 - MIERCOLES-01/06/2022=====================================

# Ejercicio 4: Etapas de Vida

 etapaVida = int(input("Ingrese su edad: "))

 if (etapaVida >= 0 and etapaVida < 10):
     print('La infancia es increíble y bella')
 elif (etapaVida >= 10 and etapaVida <= 19):
     print('Tienes muchos cambios, mucho que estudiar')
 elif (etapaVida >= 20 and etapaVida <= 29):
     print('Amor y comienza el trabajo')
 elif (etapaVida >= 30 and etapaVida <= 39):
     print('Trabajo y familia')
 elif (etapaVida >= 40 and etapaVida <= 49):
     print('Divorcio y crisis existencial')
 elif (etapaVida >= 50 and etapaVida <= 59):
     print('Nuevo casamiento')
 elif (etapaVida >= 60 and etapaVida <= 69):
     print('Jubilación y viaje por el mundo')
 elif (etapaVida >= 70 and etapaVida <= 109):
     print('Posible fin del viajecito')
 else:
     print('No existe humano que haya llegado a esa edad')
