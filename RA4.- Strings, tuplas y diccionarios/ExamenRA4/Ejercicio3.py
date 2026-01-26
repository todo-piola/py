
facturas = {}

def gestionarFacturas(facturas):
    cobrado = []
    try:
        while True:
            pendiente = 0
            opcion = input("¿Que opcion elige? Escriba 'aniadir' o 'eliminar': ")

            match opcion:
                case "aniadir":
                    numeroFactura = int(input("Que número de factura desea añadir?: "))
                    coste = float(input("Y su coste total es: ")) # Acepta decimales
                    facturas[numeroFactura] = coste
                case "eliminar":
                    numeroFactura = int(input("Que número de factura desea eliminar?: "))
                    facturas.pop(numeroFactura)
            for x in facturas:
                pendiente += facturas[x]
            print(f"La cantidad pendiente de cobro es {pendiente} €")

            print(f"Las facturas totales son: {facturas}")
            continua = input("Desea continuar modificando facturas (s/n): ")
            if(continua == "n"): return facturas

    except ValueError:
        print("Error de tipo. Introduzca un número correcto para su factura")


facturas = gestionarFacturas(facturas)