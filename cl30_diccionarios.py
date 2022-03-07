"""
.keys():Retorna la clave de nuestro elemento.

.values(): Retorna una lista de elementos (valores del diccionario).

.items(): Devuelve lista de tuplas (primero la clave y luego el valor).

.clear(): Elimina todos los items del diccionario.

.pop(“n”): Elimina el elemento ingresado.

"""


def dictionaries():
    mi_dict = {
      'Tierra': 1,
      'Marte': 2,
      'Saturno': 3
    }
    poblacion_paises = {
      'Argentina': 44938712,
	    'Brasil': 210147125,
	    'Colombia': 50372424
    }
    #imprimir por llaves
    return poblacion_paises

pobl = dictionaries()
# Imprimiento las llaves
for pais in pobl.keys():
  pass
  #print(pais)

# Imprimiento las llaves
for pais in pobl.values():
  pass
  #print(pais)

#Imprimiendo ambos valores
for pais, poblacion in pobl.items():
  pass
  #print(pais + ' tiene una poblacion de ' + str(poblacion) + ' habitantes')