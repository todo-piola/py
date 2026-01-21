'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.'''
palabra = "palindromo"
vocales = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

claves = vocales.keys()

for letra in palabra:
    if(letra in claves):
        vocales[letra] += 1

print(vocales)