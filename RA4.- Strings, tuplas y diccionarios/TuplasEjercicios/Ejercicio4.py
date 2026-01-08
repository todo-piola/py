''' Ejercicio 4: Crea una función convertir_temperatura(celsius) que reciba una
temperatura en grados Celsius y devuelva una tupla con:
● La temperatura en Fahrenheit.
● La temperatura en Kelvin.'''

def convertir_temperatura(celsius):
    arrayTemperaturas = [celsius]
    arrayTemperaturas.append((celsius*9/5)+32)
    arrayTemperaturas.append(celsius+273.15)
    return arrayTemperaturas
    
gradosCelsius = 2
convertir_temperatura(gradosCelsius)