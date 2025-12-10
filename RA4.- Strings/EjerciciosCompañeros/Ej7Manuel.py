''' Pedir por teclado una cadena de texto y “analizarla” con distintas funciones.
Deberá contar la longitud total, contar las letras (mirar str.isaplha()), 
contar los números, contar los caracteres especiales y contar los espacios'''
def contarLetras(frase, dic):
    for caracter in frase:
        if(caracter.isalpha()):
            dic["Letras"].append(caracter)
    return dic

def contarNumeros(frase, dic):
    for caracter in frase:
        if(caracter.isnumeric()):
            dic["Numeros"].append(caracter)
    return dic

def contarEspeciales(frase, dic):
    for caracter in frase:
        if(caracter.isalnum() == False and caracter.isspace() == False):
            dic["Especiales"].append(caracter)
    return dic

def contarEspacios(frase, dic):
    for caracter in frase:
        if(caracter.isspace()):
            dic["Espacios"].append(caracter)
    return dic

frase = "de 3  4f d@@## Franco es Cr4ck"

diccionarioCaracteres = {
    "Letras": [],
    "Numeros": [],
    "Especiales": [],
    "Espacios": []
}

diccionarioCaracteres = contarLetras(frase, diccionarioCaracteres)
diccionarioCaracteres = contarNumeros(frase, diccionarioCaracteres)
diccionarioCaracteres = contarEspeciales(frase, diccionarioCaracteres)
diccionarioCaracteres = contarEspacios(frase, diccionarioCaracteres)

for clave, valor in diccionarioCaracteres.items():
    print(f"{clave}: {len(valor)}")