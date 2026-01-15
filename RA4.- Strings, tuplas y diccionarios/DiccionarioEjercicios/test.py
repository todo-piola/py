# Nested diccionario

daw2 = {
    "estudiante1" : {
        "edad": 25,
        "notaPy": 4
    },
    "estudiante2" : {
        "edad": 22,
        "notaPy": 7
    },
    "estudiante3" : {
        "edad": 19,
        "notaPy": 9
    },
    "estudiante4" : {
        "edad": 30,
        "notaPy": 6
    },
}

print(daw2)

for x, obj in daw2.items():
  for y in obj:
    if(obj[y] < 5):
        obj[y] = 5

print(daw2)

