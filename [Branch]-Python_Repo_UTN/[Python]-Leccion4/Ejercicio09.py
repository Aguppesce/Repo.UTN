# ===============CLASE 05 - MARTES-13/09/2022===============
# Ejercicio 09: Mostrar una frase sin espacios y contar su longitud. Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma frase pero sin espacios en blanco, y además un contandor de cuántos caracteres tiene la frase (sin contar los espacios en blanco)

# Ejemplo frase = vivir por siempre en paz
#        frasefinal = vivirporsiempreenpaz
#        N° de caracteres = 20

frase = input("Escriba su frase: ")
fraseSinEspacios = ""
espacioEnBlanco = " "
contador=0
print(f"Su frase es: {frase}")
fraseSinEspacios=frase.replace(" ", "")
print(f"Su frase sin espacios quedo así: {fraseSinEspacios}")

for i in fraseSinEspacios:
    contador += 1
print(f"La frase sin espacios tiene {contador} caracteres")

# SOLUCIÓN CLASE
frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"N° de caracteres: {len(frase1)}")
