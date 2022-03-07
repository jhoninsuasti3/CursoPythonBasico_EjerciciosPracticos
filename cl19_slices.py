def slices():
  nombre = "Alejandro"
  print(nombre[0])
  print(nombre[1])
  sacar_rebanada = nombre[0:2]
  dos_sacar_rebanada = nombre[:3]
  tres_sacar_rebanada = nombre[3:]
  sacar_porcion_en_pasos = nombre[1:7:2] # inicia en el indice 1 hasta el 7 de a dos en dos
  completo_porcion = nombre[::]
  variacion_porcion = nombre[1::3]
  de_atras_adelante = nombre[::-1]
  
  print("""      
        sacando rebanada de cero a dos [0:2]  {}  
        desde blanco o cero a posicion tres [:3] {}
        desde tres hasta la ultima posicion [3:] {}
        dese la pos 1 hasta la pos 7 en pasos de dos en dos [1:7:2] {}
        imprimo completo la cadena [::] {}
        Inicio en la pos 1 hasta el final de a pasos de tres [1::3] {}
        Importante como devolverme en una cadena en python, indico la opcion de paso como -1 [::-1] {} 
        
        """.format(sacar_rebanada, dos_sacar_rebanada, tres_sacar_rebanada,
                   sacar_porcion_en_pasos, completo_porcion, variacion_porcion,
                   de_atras_adelante))
  