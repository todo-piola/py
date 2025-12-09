''' Clasificador de palabras

Escribe un programa en Python que pida al usuario un texto y clasifique sus palabras según estas reglas:
- Palabras que empiezan por vocal.
- Palabras que terminan en consonante.
- Palabras que contienen algún número.

El programa debe:

- Separar el texto en palabras.
- Detectar cuáles cumplen cada condición.
- Guardarlas en un diccionario con tres listas.
- Mostrar un informe final indicando las palabras encontradas en cada categoría
  y cuántas hay en cada una.'''

frase = input("Escribe una frase: ")
diccionario = {
  "Empiezan por vocal": [],
  "Terminan en consonante": [],
  "Contienen números": []
}

palabras = frase.split()

for palabra in palabras:
    if palabra[0].lower() in "aeiou":
        diccionario["Empiezan por vocal"].append(palabra)
    if palabra[-1].lower() not in "aeiou":
        diccionario["Terminan en consonante"].append(palabra)
    for caracter in palabra:
        if caracter.isdigit():
            diccionario["Contienen números"].append(palabra)
            break

print("Palabras que empiezan por vocal:", diccionario["Empiezan por vocal"], "Cantidad:", len(diccionario["Empiezan por vocal"]))
print("Palabras que terminan en consonante:", diccionario["Terminan en consonante"], "Cantidad:", len(diccionario["Terminan en consonante"]))
print("Palabras que contienen números:", diccionario["Contienen números"], "Cantidad:", len(diccionario["Contienen números"]))