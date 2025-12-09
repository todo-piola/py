'''Ejercicio 2  (Ana López) 

Vamos a definir una cadena y la vamos a pasar a minúsculas, eliminar los espacios

y las letras pares las vamos a cambiar por asteriscos'''

frase = "  Este Ejercicio Es Muy Divertido  "
frase = frase.lower().strip()
print(frase)

resultado = ""
contador = 2

for letra in frase:
    if(contador%2 == 0):
        resultado += "*"
    else:
        resultado += letra

    contador+=1

print(resultado)