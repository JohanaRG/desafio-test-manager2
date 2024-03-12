""" Ejemplos de funciones en Python """

# Crear una función que se encargue 
# sumar dos números

def suma(num1, num2):
    """ Entrada: Dos números
        Objetivo: Sumar los números que reciba
        Salida: El valor resultante de la sumatoria.
    """

    sumatoria = num1 + num2
    return sumatoria


def saludo_personalizado(nombre="Amigo"):
    """ Entrada: Nombre
        Objetivo: Es mostrar un saludo en consola
     s   Salida: No tiene.
    """
    if nombre != "":
        print(f'Hola {nombre}')
    else:
        print("El nombre ingresado es vacío.")


# Bloque principal
if __name__ == "__main__":
    print("Bienvenido al programa \n Sumar")
    nombre = str(input("Ingrese un nombre: "))

    saludo_personalizado(nombre)

    numero_1 = float(input("Ingrese un número: "))
    numero_2 = float(input("Ingrese otro número: "))

    # Invocar a la función sumar
    resultado = suma(numero_1,numero_2)
    print(f'El resultado de sumar {numero_1} + {numero_2} es {resultado}')