''' Ejercicio 5: Crea una función analizar_numeros(numeros) que reciba una lista de
enteros y devuelva una tupla con:
● El número de elementos pares.
● El número de elementos impares.
● La suma total'''

def analizar_numeros(numeros):
    estadisticasNumeros = []
    sumaTotal = 0
    pares = 0
    impares = 0

    for x in range(len(numeros)):
        sumaTotal+=numeros[x]
        if(numeros[x] == 0 or numeros[x] % 2 == 0):
            pares+=1
        else:
            impares+=1

    estadisticasNumeros.append(sumaTotal)
    estadisticasNumeros.append(pares)
    estadisticasNumeros.append(impares)

    print(estadisticasNumeros)
    return estadisticasNumeros

arrayNums = [5, 9, 25, 7, 3, 5, 2, 4, 24]
analizar_numeros(arrayNums)
