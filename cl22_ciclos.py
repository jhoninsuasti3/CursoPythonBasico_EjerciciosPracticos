def ciclo_while():
  LIMITE = 100
  contador = 0
  potencia = 2**contador
  while potencia < LIMITE:
    print('2 elevado a ' + str(contador) + 'es igual a: ' + str(potencia))
    contador+= 1
    potencia+=potencia

def otroCicloWhile():
  contador = 1
  print(contador)
  while contador < 10:
    contador+= 1
    print(contador)

def cicloFor():
  for a in range(30):
    print(a)

def cicloForDos():
  # el range funcion podemos pasarle el parametro de inicio hasta el fin, siempres en fin -1
  for a in range(1, 11): 
    print(a)

def ciclo_tres(num_tabla):
  for a in range(11): 
    print(f"La multiplicacion de la tabla del {num_tabla} --> {num_tabla} * {a} es: {num_tabla * a} ")
