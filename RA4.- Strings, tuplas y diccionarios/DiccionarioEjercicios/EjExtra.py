'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>.'''

diccionario = {
    "nombre": "",
    "edad": 0,
    "direccion": "",
    "telefono": 0,
}

for x in diccionario:
    try:
        diccionario[x] = int(input(f"Determina tu {x}: ")) if x in ["edad", "telefono"] else input(f"Determina tu {x}: ")
    except ValueError:
        print("Error de tipos")
    
print(diccionario)

'''Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla y
el número de kilos, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Si no hay suficientes kilos, indicarselo al cliente
 '''

fruteria = {
    "manzana": {
        "precio": 1.25,
        "kilosTotales": 12 
    },
    "pera": {
        "precio": 0.75,
        "kilosTotales": 7
    }
}

