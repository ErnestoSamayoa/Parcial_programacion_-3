#2. Define una función llamada "inverso_palabra" que reciba una cadena como parámetro y devuelva la cadena invertida. 
#Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp". 

print("\n******Bienvenido Usuario*****")

inverso_palabra = "python"
palabra = list(inverso_palabra)
palabra.reverse()
texto_revertido = ''.join(palabra)
print(texto_revertido)

print("\n******************************")

