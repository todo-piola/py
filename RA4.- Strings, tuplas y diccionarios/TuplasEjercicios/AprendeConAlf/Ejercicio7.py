'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante.'''

import string

# Abecedario en minúsculas
abc_espanol = list(string.ascii_lowercase)
abc_espanol.insert(14, 'ñ')
contador = 1

copia_abc = abc_espanol.copy()

for x in copia_abc:
    if(contador % 3 == 0):
        abc_espanol.remove(x)
    contador += 1

print(abc_espanol)