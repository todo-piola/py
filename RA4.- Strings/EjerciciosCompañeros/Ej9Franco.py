'''Volviendo a Messenger

Pide al usuario una oración completa y el programa debe decir cuántas palabras tiene esa oración.
Si ese número es par, convierte las letras pares a mayúsculas y las impares a minúsculas y devuelve esa frase convertida.
Si el número es impar, devuelve la frase con las palabras con el orden invertido.'''

frase = "Estoy estudiando Python no quiero suspender"
word1 = "caracola"
word2 = "Caracola"
if word1 > word2:
    print("k pacha aqui")
elif word2 > word1:
    print("asaaaaa")

def contadorPalabras(frase):
    listaPalabras = frase.split()
    numeroPalabras = len(listaPalabras)
    return numeroPalabras

def conversorMessenger(frase, num):
    fraseConvertida=""
    indice = 0
    if(num%2==0):
        while(indice < len(frase)):
            if(indice%2==0):
                fraseConvertida+=frase[indice].upper()
            else:
                fraseConvertida+=frase[indice].lower()
            indice+=1
    else:
        listaPalabras = frase.split()
        listaPalabras.reverse()
        fraseConvertida = " ".join(listaPalabras)

    return fraseConvertida

numPalabras = contadorPalabras(frase)
print(conversorMessenger(frase, numPalabras))