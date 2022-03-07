import random as rnd


def play():
  
  num_random_pc = rnd.randint(1, 30)
  num_input_user = int(input("Digite un numero entre el 1 y el 100"))
  cant_intents = 0
  
  while num_input_user != num_random_pc:
    cant_intents += 1
    if num_input_user < num_random_pc:
      print("Debes elegir un numero mayor")
    else :
      print("Debes elegir un numero mas pequeño")
    num_input_user = int(input("Elige otro numero entre el 1 y el 100"))
  print(f"""Felicidades ganaste, encontraste el numero {num_random_pc}
        que fue generado por la compu, y la cantidad de intentos fueron {cant_intents}  """)  


