'''Modifica la cadena “               este ejercicio es muy complicado            ” para que el ejercicio sea facilísimo
 y cada una de las palabras comience en mayúsculas
 y sin espacios y luego imprimelo invertido, ademas busca el indice de la palabra complicado.'''

frase = "            este ejercicio es muy complicado            "
frase = frase.strip().title()
print(frase)

frase_invertida = frase.split()
frase_invertida.reverse()
frase_invertida = " ".join(frase_invertida)
print(frase_invertida)

indice = frase.find("Complicado")
print(f"El indice de la palabra complicado es: {indice}")