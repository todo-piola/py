''' A través de una función, introduciendo una cadena por parámetro, devolver la longitud, 
devolver la cadena en minúsculas y devolver las ultimas 5 letras de la cadena.'''

def longitudCadena(frase):
    return frase.len()

def minusculasCadena(frase):
    return frase.lower()

def finalCadena(frase):
    extraccion = ""
    for letra in range(len(frase)-5, len(frase)):
        extraccion += frase[letra]
    return extraccion


frase = "Este es el ejercicio de Pacheco"
print(finalCadena(frase))