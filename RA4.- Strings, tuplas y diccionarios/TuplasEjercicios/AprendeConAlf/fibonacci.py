'''Una secuencia fibonacci es una serie numérica donde
 cada número es la suma de los dos anteriores (empezando por 0 y 1)'''

anterior = 0
actual = 1

numero = 0

limite = 15

for x in range(limite):
    print(anterior)
    numero = anterior + actual
    anterior = actual
    actual = numero
    
    