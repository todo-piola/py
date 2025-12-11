''' Recoger un email por consola introducido por el usuario. En una función se debe comprobar que el correo introducido por el usuario
 contenga “@” y acabe en “.com” o “.es”.
Además, el usuario solo tendrá tres oportunidades para validar el correo.'''

def validarCorreo(email, intentos):
    if(email.find("@") and (email.endswith(".com")) or (email.endswith(".es"))):
        print("Email introducido es correcto")
    else:
        intentos-=1
        print(f"Email inválido. Tiene {intentos} intentos restantes")
        return intentos

intentos = 3

while(intentos > 0):
    email = input("Introduce tu email: ")
    intentos = validarCorreo(email, intentos)


