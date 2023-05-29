#Esta es el ejercicio 6 de la Tarea 2

# import random
# numero = random.randint(1, 20) #longitud de la lista
# # print(numero)
# newlist = []
# i=0
# while i <= numero:

#     newlist.append(random.randint(1, 20))
#     i+=1

# print("Esta es la lista de numero aleatorios")
# print(newlist)

# set_ejemplo = set(newlist)
# newlist=list(set_ejemplo)
# print("Esta es la lista de numeros sin repetidos")
# print(newlist)

test1 = [1, 2, 300, 300, 2, 4, 6] #Esta es la lista de prueba
test2 = [3, 3, 3, 3, 3, 3, 3] 

print("Estos son los casos de prueba: ")
print(test1)
print(test2)

x = lambda a : set(a) #Se utilizo la lambda y el set para eliminar repetidos

print("Este es el resultado sin repetidos: ")
print(list(x(test1)))
print(list(x(test2)))





