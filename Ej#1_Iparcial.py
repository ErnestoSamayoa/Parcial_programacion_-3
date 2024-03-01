#Variante A:
#1. Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los elementos de la lista. 

def sum_lista(lista):
    suma = 0
    for elemento in lista:
        suma+=elemento # suma=suma+elemento

    return suma


