''' Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.'''

def analizar_texto(texto):
    textoAnalizado = []
    palabrasDelTexto = texto.split(" ")
    textoAnalizado.append(len(texto))   # Añado número total de caracteres
    textoAnalizado.append(len(palabrasDelTexto))
    textoAnalizado.append(palabrasDelTexto[0])  # Primera palabra del texto

    print(textoAnalizado)
    return textoAnalizado

texto = "Caracol al sol"
analizar_texto(texto)

