# lista de numeros aleatorios con longitud aleatoria de la lista
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

newlist = [x ** 3 for x in newlist] #elevar cada elemento al cubo

print("Esta es la lista de numero aleatorios al cubo")
print(newlist)


