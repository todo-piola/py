''' Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.'''

def calcular_estadisticas(numeros):
    arrayEstadisticas = []
    arrayEstadisticas.append(min(numeros))
    arrayEstadisticas.append(max(numeros))
    
    media = 0
    for x in numeros:
        media+= x
    media/=len(numeros)
    arrayEstadisticas.append(media)

    print(arrayEstadisticas)
    return arrayEstadisticas

arrayNumeros = [6, 25, 7, 2, 9]
calcular_estadisticas(arrayNumeros)
    