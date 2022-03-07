## Copy @jhoninsuasti3
from tiposdatos import *
from operadoreslogicosycompracion import *
from cl14condicionales  import *
import  cl15_conversormonedas  as cl15
import   cl16_funciones as cl16  
import cl17_conversormonedas_new as cl17
import cl18_caracteres as cl18
import cl19_slices as cl19
import cl20_proyecto_palindromo as cl20
import cl22_ciclos as cl22
import  cl25_break_cont as cl25 
import videojuego_adivinanumero as juego
import cl28_tuplas as cl28
import cl30_diccionarios as cl30
import generador_contrasenas as generador

def main():
    print("This is Main Program")
    # tiposdatos()   ---> Funcion tipos datos
    # operlogicnadcomparation()
    #cl15.conversor_menu()
    # clase 16 funciones y return#  print(cl16.suma(1, 4))
    # classe 17 aplicando funciones a algo real # cl17.conversor_menu()
    #cl18.caracteres()
    #cl19.slices()
    #palabra = input("Digite la palabra para validar \n") # Para entrar parametro a funcion palindromo
    #print(cl20.palindromo(palabra))
    #cl22.ciclo_tres(3)
    #cl22
    #cl25.ejemplo_dos()
    #numero = int(input('Digite un numero'))
    #if cl25.validate_num_prime(numero):
    #  print("Es primo")
    #else:
    #  print('No es primo')
    #juego.play()
    #cl28.recorrido_metodo_dos()
    #cl28.tuples()
    #cl30.dictionaries()
    print(generador.generate_password(15))
  
if __name__ == "__main__":
    main()
    