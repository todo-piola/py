''' Crea una función que reciba un argumento string y compruebe si todos los caracteres son mayúsculas'''

def comprobarMayusculas(frase):
    for letra in frase:
        if(letra.islower()):
            return False
    return True

frase = "soY todo MAYUSCulas?"
esMayuscula = comprobarMayusculas(frase)
print(esMayuscula)