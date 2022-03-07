## TIPOS DE DATOS
# Numeros enteros
# Numeros de punto flotantes (5.6)
# Texto o cadenas de caracteres(String = Cadena de chars)
# Booleanos (true or false)

### CONCEPTOS BASICOS PYTHON
#peso = input("¿Cual es tu edad?")
#print("Su peso es " + peso)


def tiposdatos():
    #Strings
    name = "Jhon Alejandro Insuasti"
    profesion = 'Ing de sistemas'
    # Enteros y flotantes
    x = 5
    y = 5.2
    print("arg1 =", type(x), "arg2 =", type(y))
    # Booleanos
    trabaja = True

    #CONVERSIONES DE TIPOS DE DATOS
    numero1 = int(input("Digita un numero: "))
    numero2 = int(input("Digita otro numero: "))
    resul_numer = numero1 + numero2
    print(resul_numer)

    str(resul_numer)  # Conversion a String
