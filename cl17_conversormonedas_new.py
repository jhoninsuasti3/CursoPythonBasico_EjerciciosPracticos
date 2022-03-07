## Copy @jhoninsuasti3

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?")
    pesos = float(pesos)
    valor_dolar = 3956
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")

def conversor_menu():
    menu = """
    Bienvenido al conversor de monedas $$$$

    1- Pesos colombianos
    2- Pesos argentinos
    3- Pesos mexicanos
    """

    opcion = int(input(menu))

    if opcion == 1:
        conversor("Colombiano",3980)
    elif opcion == 2:
        conversor("Argentino",65)
    elif opcion == 3:
        conversor("Mexicanos",24)
    else:
        print("Ingrese una opcion correcta")
