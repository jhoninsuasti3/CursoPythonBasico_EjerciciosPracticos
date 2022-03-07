def caracteres():
    print("En esta clase me puse de coqueto y fui aprendiendo por mi mismo y otros temas ")
    nombre = "jhon"
    #tranformar a mayus 
    nombre.upper()
    #print(nombre)
    #transformar la primera en mayus
    nombre.capitalize()
    #print(nombre)
    #almacenando los resultados en la misma variable
    nombre = nombre.capitalize()
    #print(nombre)
    # Reemplazar o quitar los spacios de una cadena
    nombre = nombre.strip()
    # Convertir todo a minisculas 
    nombre = nombre.lower()
    # Remplazar un caracter por otro en una cadena
    nombre = nombre.replace("n", "a" )
    print(nombre)
    # aprendiendo ciclos en python 
    #str() funcion para convertir a string
    # ,end = " " -> se utiliza para expcificar el formato de impresion

    buenas = "INSUASTI"
    for cad in range(len(buenas)):
      print("El indice de la letra {} es ".format(cad, buenas[cad]))


  
    """
    
    for i in range(11):
      print("numero" , i , end=" ")

    print("\n")    
    #contando
    for let in nombre:
      print("# " + let)
    
    # Método 2, con índice
    for indice in range(len(nombre)):
        caracter = nombre[indice]
        print("En el índice {} tenemos a '{}'".format(indice, caracter))


    """