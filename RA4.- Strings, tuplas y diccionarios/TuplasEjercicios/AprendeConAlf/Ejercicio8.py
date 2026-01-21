'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''

palabra = input("Palabra: ")
invertida = ""

for letra in reversed(palabra):
    invertida += letra

print(invertida)