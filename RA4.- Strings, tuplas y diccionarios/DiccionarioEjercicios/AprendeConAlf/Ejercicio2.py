'''EJ2. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>.'''

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
