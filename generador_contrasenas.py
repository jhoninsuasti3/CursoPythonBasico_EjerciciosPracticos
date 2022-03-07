# @Jhon Insuasti 
#Finalizando muchas practicas de python
import random

MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']


def generate_password(tamano):
  caracteres = MAYUS + MINUS + NUMS + CHARS
  contrasena = []

  for i in range(tamano):
    string_random = random.choice(caracteres)
    contrasena.append(string_random)
  
  #convertir de lista a string
  contrasena = "".join(contrasena)
  return contrasena


es_estudiante = True
es_profesor = False

print(es_estudiante or es_profesor )

print(round(10.3456, 2))