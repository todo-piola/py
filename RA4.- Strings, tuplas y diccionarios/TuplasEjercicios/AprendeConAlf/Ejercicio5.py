'''Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.'''
nums = []
for x in range(1,11):
    nums.append(x)


numsInvertido = reversed(nums)
cadena = ""

for x in numsInvertido:
    cadena += f"{x},"

cadena = cadena[:-1]
print(cadena)
long = len(cadena)
