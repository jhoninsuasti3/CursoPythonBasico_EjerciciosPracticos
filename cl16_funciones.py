"""

def imprimiendo_mensaje():
    print("Mensjae")

imprimiendo_mensaje()
opcion = int(input('Elige una opcion (1, 2, 3): '))

def conversacion(mensaje):
    print('Hola')
    print('¿Como estas?')
    print(mensaje)
    print('Adios')

def eleccion_conversacion():
    if opcion == 1:
        conversacion('Elegiste la opcion 1')
    if opcion == 2:
        conversacion('Elegiste la opcion 2')
    if opcion == 3:
        conversacion('Elegiste la opcion 3')

"""


def suma(a, b):
    print('Se suman dos números')
    resultado = a + b
    return resultado

