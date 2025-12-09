'''Volviendo a Messenger

Pide al usuario una oración completa y el programa debe decir cuántas palabras tiene esa oración.
Si ese número es par, convierte las letras pares a mayúsculas y las impares a minúsculas y devuelve esa frase convertida.
Si el número es impar, devuelve la frase con las palabras con el orden invertido.'''

frase = "Estoy estudiando Python no quiero suspender"

def contadorPalabras(frase):
    listaPalabras = frase.split()
    numeroPalabras = len(listaPalabras)
    return numeroPalabras

def conversorMessenger(frase, num):
    fraseConvertida=""
    if(num%2==0):
        for i, letra in enumerate(frase): # i es el índice, letra cada caracter
            if(i%2==0):
                fraseConvertida+=letra.upper()
            else:
                fraseConvertida+=letra.lower()
    else:
        listaPalabras = frase.split()
        listaPalabras.reverse()
        fraseConvertida = " ".join(listaPalabras)

    return fraseConvertida

numPalabras = contadorPalabras(frase)
print(conversorMessenger(frase, numPalabras))