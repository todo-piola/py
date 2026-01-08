'''Ejercicio 6: Crea una función procesar_cadena(cadena) que devuelva una tupla con:
● La cadena en mayúsculas.
● La cadena en minúsculas.
● La longitud de la cadena'''

def procesar_cadena(cadena):
    arrayCadenas = []
    arrayCadenas.append(cadena.upper())
    arrayCadenas.append(cadena.lower())
    arrayCadenas.append(len(cadena))
    print(arrayCadenas)
    return arrayCadenas

cadena = "ESTA es la Cadena Definitiva"
procesar_cadena(cadena)