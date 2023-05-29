#Esta era la funcion origial del ejercicio 4 de la Tarea 4

def devolver_lista_tupla(string):
    string_clear = string.replace(" ", "") #quitar espacios
    list = string_clear.split(",") #esta funcion los separa en lista cuando detecta la coma
    tupla = tuple(list) #esta funcion lo convierte en tupla
    return list , tupla

print("Este es el string de prueba: 1,2,3,4,5,6,7")

test = "1,2,3,4,5,6,7" #Este es el ejemplo de prueba

print((lambda s: s.split(","))(test)) #aca se usa la lambda y el cuerpo es el split para separlo y el caso de prueba es test
print(tuple((lambda s: s.split(","))(test))) # esta es la misma funcion pero se usa tuple para convertirla en tupla