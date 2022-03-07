"""
___Propiedades que aplican a tuplas:
len
max
min
sum
any
all
sorted
______Métodos que aplican a tuplas:
index
count
"""
from timeit import timeit

def repaso_list_objects():
  #declaracion de una lista que tiene otra lista en ella
  objetos = ['Casa', 'Automovil',25,True, ['Thomas', 'Ronald']]
  #objetos.append('sistemas')
  return objetos
  
pasable = repaso_list_objects()

#Aqui si la lista tiene anidada otras listas
def recorrido_metodo_one(recibe):
  for element in recibe:
    if type(element) == list:
      for a in element:
        print( a)
        #continue
    else:
      print(f"{element}")
    #print(type(element))
  
#recorrido_metodo_one(pasable)

def recorrido_metodo_dos(pasable):

  for i in range(len(pasable)):
    print(f"pasable[i][2]") 
  pass
  #for recorre in pasable[::-1]:
  #  print(recorre)

#recorrido_metodo_dos(pasable)

lista1 = [['1','2','3'],['4','5','6'],['7','8','9']]
lista2 = [['1','2','3'],['4','5','6'],['7','8','10']]

def recorrido_metodo_tres(pasable):
  dif =[]
  for i in range(len(lista1)):
    print(lista1[i][2])
    pass
    if lista1[i][2] != lista2[i][2]:
        dif.append(i)
  print("dif")

#recorrido_metodo_tres(pasable)

def recorrido_metodo_cuatro_recursivamente(recibe):
  for element_only_list_father in recibe:
    if type(element_only_list_father) == list:
        recorrido_metodo_cuatro_recursivamente(element_only_list_father)
    else:
        print(element_only_list_father)
  pass

#recorrido_metodo_cuatro_recursivamente(pasable)

#sumando listas
list_numeros1 = [1,2,3,4]
list_numeros2 = [6,7,8,9]
#
lista_final = list_numeros1 + list_numeros2
#print(lista_final)

#print(lista_final * 5) 


def tuples():

  
  my_tuple = (1,2,3,4,5)
  pass
  #print(my_tuple)


def lists():
    lista = []
    for i in range(11):
      lista.append(i)
    return lista

resultado_lista = lists()

#Calculando cuanto demora una lista y una tupla al recorrer en python
#for a in resultado_lista:
#   print(a)

mytuple = tuple(resultado_lista)

for a in resultado_lista:
  pass  
  #print(a)
  
#print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))


