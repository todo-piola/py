''' Recibir dos cadenas de caracteres y contar sus vocales para después sumarlas.
por otra parte combinar las dos cadenas y remplazar cada carácter que este en una posición impar por una “C”.'''

def contarVocales(cadena1, cadena2):
    contador = 0
    for caracter in cadena1:
        if(caracter.lower() in "aeiou"):
            contador += 1
    for caracter in cadena2:
        if(caracter.lower() in "aeiou"):
            contador += 1
    return contador

def combinarCadenas(cadena1, cadena2):
    cadenaCombinada = cadena1 + cadena2
    nuevaCadena = ""
    indice = 0
    
    while indice < len(cadenaCombinada): # recorrer con índice
        if(i % 2 == 0): # posición impar (índices pares)
            nuevaCadena += "C"
        else:
            nuevaCadena += caracter
        indice+=1

    return nuevaCadena

cadena1 = "Hola que tal"
cadena2 = "Estoy bien gracias"
totalVocales = contarVocales(cadena1, cadena2)
print(f"El total de vocales en ambas cadenas es: {totalVocales}")
cadenaModificada = combinarCadenas(cadena1, cadena2)
print(f"La cadena combinada y modificada es: {cadenaModificada}")