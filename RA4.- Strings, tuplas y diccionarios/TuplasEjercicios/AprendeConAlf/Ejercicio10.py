'''Escribir un programa que almacene en una lista los siguientes precios,
 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.'''

import math

lista = [50, 75, 46, 22, 80, 65, 8]

menor = math.inf
maximo = 0

for x in lista:
    if x <= menor:
        menor = x
    elif x >= maximo:
        maximo = x

print(menor, maximo)
