'''EJ2. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>.

diccionario = {
    "nombre": "",
    "edad": 0,
    "direccion": "",
    "telefono": 0,
}

arrayRespuesta = []

for x in diccionario:
    try:
        diccionario[x] = int(input(f"Determina tu {x}: ")) if x in ["edad", "telefono"] else input(f"Determina tu {x}: ")
    except ValueError:
        print("Error de tipos")

print(f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en {diccionario['direccion']} y su número de teléfono es {diccionario['telefono']}")
'''

'''EJ3. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla y
el número de kilos, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Si no hay suficientes kilos, indicarselo al cliente


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

try:
    frutaCliente = input("¿Qué fruta quieres comprar? ")
    kilosFruta = int(input(f"¿Cuantos kilos de {frutaCliente} quieres comprar? "))

    if(frutaCliente in fruteria):
        if(kilosFruta <= fruteria[frutaCliente]["kilosTotales"]):
            fruteria[frutaCliente]["kilosTotales"] -= kilosFruta
            print(f"Has comprado {kilosFruta}kgs de {frutaCliente}. Hay restantes {fruteria[frutaCliente]['kilosTotales']}kgs")
        else: print("Los kilos solicitados superan el total máximo de kilos")
    else: print("La fruta solicitada no está disponible")
except(ValueError):
    print("Error de tipo")
'''

'''EJ4. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre 
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
 el nombre del mes.

fecha = input("Escribe una fecha en formato dd/mm/aaaa: ")

fechaCompleta = {
    "dia": "",
    "mes": "",
    "año": ""
}

arrayFecha = fecha.split("/")

for i, x in enumerate(fechaCompleta):
    fechaCompleta[x] = arrayFecha[i]

print(f"{fechaCompleta["dia"]} de {fechaCompleta["mes"]} de {fechaCompleta["año"]}")
'''

