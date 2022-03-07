
def  menu_table_multiplication():
  print("""
        *** TABLA DE MULTIPLICACION ***
        -> Seleccion la opcion correcta
          Opcion 1. Marque numero correspondiente para mostrar el resultado de para la tabla (ejemplo 1 para la tabla del 1)
          Opcion 2. Despues se le solicitara marcar el limite para el resultado
          . La seleccion solo permite numeros enteros (el programa terminara si marca otra opcion del teclado)
        """)
  num_tb = int(input("\n (Opcion 1.) Digite la tabla: "))
  validation_ints(num_tb)
  lim_nm = int(input("   (Opcion 2.) Digite la cantidad de numeros a multiplicar \n"))
  validation_ints(lim_nm)
  
  return {'numtb':num_tb,'limnm':lim_nm}

def example_table_multiplication():
  values_input = menu_table_multiplication()
  num_tabla = values_input['numtb']
  limi_num = values_input['limnm']
  for a in range(1, limi_num): 
    print(f"La multiplicacion de la tabla del {num_tabla} --> {num_tabla} * {a} es: {num_tabla * a} ")

def validation_ints(num):
    try:
      int(num)
      pass
    except ValueError:
      print("Digite un numero valido para poder realizar la operacion")
      quit()
  