"""
    Ejemplos extra para el curso PI-25,
    en el tema: variables.
"""

# Dato: String
# Mostrar un mensaje personalizado
print("Hola, soy un mensaje personalizado")

# Guardar un mensaje en una varible
mensaje = "Hola, soy un mensaje guardado en una variable"

print("Mostrando contenido de la variable mensaje:",mensaje)
print(f'Mostrando contenido de la variable mensaje: {mensaje}')

# Crear dos variables numéricas
numero1 = 5
numero2 = "2" # str: texto
numero3 = "5.6"

print(type(numero1))
print(type(numero2))

suma = numero1 + int(numero2) + float(numero3)
print(f'Resultado suma: {suma}')

resta = numero1 - int(numero2) - float(numero3)
print(f'Resultado resta: {resta}')

multiplicacion = numero1 * int(numero2) * float(numero3)
print(f'Resultado multiplicacion: {multiplicacion}')

division = numero1 / int(numero2) 
print(f'Resultado division: {division}')

division_parte_entera = numero1 // int(numero2) 
print(f'Resultado division: {division_parte_entera}')

potencia = numero1 ** int(numero2) 
print(f'Resultado division: {potencia}')

resto = numero1 % int(numero2) 
print(f'Resultado division: {resto}')

# Datos booleanos
# Operador de comparación

edad = 47

es_mayor = edad >= 18
print(f'Es mayor? {es_mayor}')


# Operadores para strings
texto1 = "Primer clase de"
texto2 = "Python"

concatenando = texto1 + " " + texto2
print(concatenando)

print(concatenando * 5)

texto3 = "Python"
       #  012345
       #      -1

print(texto3[2])

print(texto3[-4])

print(texto3[4])
print(texto3[-2])

texto4 = "Es un ejemplo para acceder a una letra de una cadenA"
print(texto4[-1])

