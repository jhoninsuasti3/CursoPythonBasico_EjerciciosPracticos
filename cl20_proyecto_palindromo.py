def palindromo(palabra):
  palabra = palabra.replace(' ', '').lower() # remplaza espacios y convierte a mins
  resultado = ""
  if palabra[::] == palabra[::-1] :
    resultado = "Es palindromo"
  else:
    resultado = " No es palindromo"
  return resultado