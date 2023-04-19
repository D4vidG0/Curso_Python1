#Ejercicio 1 factorial de un numero ingresado por el usuario
# factorial de 4 es 4*3*2*1
num=int(input("Ingrese un numero mayor a 0: \n"))

if num > 0:
    i = 1
    factorial =1
    while i <= num:
      factorial=i*factorial
      i+=1
    print("El factorial de", num ,"es", factorial)


else:
   print("Error, el numero no es mayor que 0")
