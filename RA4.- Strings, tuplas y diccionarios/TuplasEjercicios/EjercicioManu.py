'''Ejercicio index by Manu
Adivina en qué posición está el nº n (aleatorio 1-10) en una tupla'''

import random

tupla = [4, 7, 2, 5, 9]

def buscarNumero(tupla):
    numeroAleatorio = random.randint(1,9)

    if(numeroAleatorio in tupla):
        posNum = tupla.index(numeroAleatorio)
        print(f'La tupla contiene el nºaleatorio {numeroAleatorio} en la posición {posNum}')
        return posNum # Devuelve el índice del número aleatorio en la tupla
    else:
        print(f'Número aleatorio {numeroAleatorio} no aparece en la tupla')
        return False

buscarNumero(tupla)