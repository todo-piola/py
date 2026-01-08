''' Pida al usuario una frase.
Elimine los espacios al inicio y al final (strip()).
 Muestre: La frase en minúsculas (lower()).
La frase en mayúsculas (upper()).
La frase con la primera letra en mayúscula (capitalize()).
Reemplace todas las comas por puntos (replace()).
Cuente cuántas veces aparece una palabra que el usuario ingresa (count()).
Verifique si la frase empieza con una vocal (startswith()).
Muestre cuántas palabras tiene la frase (split()).'''

frase = input("Ingrese una frase: ")
frase = frase.strip()
print("Frase en minusculas:", frase.lower())
print("Frase en mayusculas:", frase.upper())
print("Frase con la primera letra en mayuscula:", frase.capitalize())
frase_sin_comas = frase.replace(",", ".")
print("Frase con comas reemplazadas por puntos:", frase_sin_comas)
palabra_buscar = input("Ingrese una palabra para contar su aparicion en la frase: ")
contador_palabra = frase.count(palabra_buscar)
print(f"La palabra '{palabra_buscar}' aparece {contador_palabra} veces en la frase.")
vocales = "aeiouAEIOU"
if frase.startswith(tuple(vocales)):
    print("La frase empieza con una vocal.")