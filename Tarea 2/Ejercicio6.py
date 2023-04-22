#eliminar repetidos de una lista
#Utilizare la lista del Ejercion4
import random
numero = random.randint(1, 20) #longitud de la lista
# print(numero)
newlist = []
i=0
while i <= numero:

    newlist.append(random.randint(1, 20))
    i+=1

print("Esta es la lista de numero aleatorios")
print(newlist)

set_ejemplo = set(newlist)
newlist=list(set_ejemplo)
print("Esta es la lista de numeros sin repetidos")
print(newlist)
