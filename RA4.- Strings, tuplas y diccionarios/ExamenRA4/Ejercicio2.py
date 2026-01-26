
tareas = ["barrer", "fregar", "estudiar", "cocinar", "Hacer ejercicios Python", "leer", "hablar", "debatir"]

def mostrar_tareas():
    for x, y in enumerate(tareas):
        print(f"Prioridad {x + 1}. {y}")

def insertar_tarea(nombre, posicion):   
    tareas.insert(posicion, nombre)

def eliminar_tarea(nombre):
    tareas.remove(nombre)

def mover_tarea(nombre, nueva_posicion):
    if(nombre in tareas):
        tarea = nombre
        tareas.remove(nombre)
        tareas.insert((nueva_posicion - 1), tarea)
    else:
        print(f"Lista de tareas no contiene {nombre}")

mostrar_tareas()
insertar_tarea("volar", 2) # - Tendría que invertir el orden de los parámetro ya que el método insert
print("-----------------COMPROBACIÓN DESPUES DE INSERTAR------------")
mostrar_tareas()
# recibe primero el índice. Eso o hacer los parámetros no posicionales cosa que no recuerdo y no tengo tiempo de buscar
eliminar_tarea("leer")
print("-----------------COMPROBACIÓN DESPUES DE ELIMINAR------------")
mostrar_tareas()

mover_tarea("Hacer ejercicios Python", 1)
print("-----------------COMPROBACIÓN DESPUES DE MOVER TAREA------------")
mostrar_tareas()