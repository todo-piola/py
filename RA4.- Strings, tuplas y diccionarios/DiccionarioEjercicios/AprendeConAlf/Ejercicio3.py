'''EJ3. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla y
el número de kilos, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Si no hay suficientes kilos, indicarselo al cliente'''


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
