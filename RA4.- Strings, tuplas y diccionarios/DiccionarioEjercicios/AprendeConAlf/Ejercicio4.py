'''EJ4. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre 
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
 el nombre del mes.'''

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

