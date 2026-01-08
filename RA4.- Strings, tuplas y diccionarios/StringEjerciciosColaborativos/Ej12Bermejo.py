''' Crear una funcion que cuente el numero de letras que tiene un string, el numero de numeros y el numero de espacios.
La funcion debe devolver un string con el siguiente formato:
"tienes X letras, Y numeros y Z espacios" '''

from Ej7Manuel import contarLetras, contarNumeros, contarEspacios
import Ej7Manuel as m

frase = "hola que tal tengo 2 perros y 1 gato"

diccionarioCaracteres = {
    "Letras": [],
    "Numeros": [],
    "Espacios": []
}

diccionarioCaracteres = m.contarLetras(frase, diccionarioCaracteres)
diccionarioCaracteres = m.contarNumeros(frase, diccionarioCaracteres)
diccionarioCaracteres = m.contarEspacios(frase, diccionarioCaracteres)

numLetras = len(diccionarioCaracteres["Letras"])
numNumeros = len(diccionarioCaracteres["Numeros"])
numEspacios = len(diccionarioCaracteres["Espacios"])

print(f"Tienes {numLetras} letras, {numNumeros} numeros y {numEspacios} espacios")
