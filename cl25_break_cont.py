def ejemplo_uno():
  for contador in range(100):
    if contador % 2 == 0:
      continue
    print(contador)

def ejemplo_dos():
  for i in range(100):
    print(i)
    if i == 50:
      break
    


def validate_num_prime(numero):
  contador = 0
  for i in range(1,numero + 1):
    if i == 1 or i == numero:
      if numero == 1:
        contador+= 1
      continue
    if numero % i == 0:
        contador+= 1
        break
  if contador == 0:
    return True
  else:
    return False
    
    
    