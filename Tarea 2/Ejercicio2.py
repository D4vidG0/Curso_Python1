#Ejercicio 2 Triangulo
num=int(input("Ingrese un numero mayor a 0: \n"))

if num > 0:
   for row in range(1,num+1):
    for col in range(1,row+1):
          print(col, end=" ")
    print()


else:
   print("Error, el numero no es mayor que 0")

