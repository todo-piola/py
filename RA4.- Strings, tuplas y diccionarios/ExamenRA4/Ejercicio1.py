

def validaEmail(email):
    if("@" not in email): return verificacion   # Verificaciones iniciales para no entrar en la función
    if("." not in email): return verificacion
    if(email.count("@") > 1): return verificacion

    segmentos = email.split("@")

    if(len(segmentos) > 1): # Si entra por aquí significa que el email tiene carácteres antes y después del @
        dominio = segmentos[1]
        if(dominio.startswith(".") or dominio.endswith(".")): return verificacion
        if(segmentos[0] == ""): return verificacion

    return True

email = "@GMAIL.COM"
verificacion = False
verificacion = validaEmail(email)
print(verificacion)