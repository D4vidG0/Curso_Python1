def sumar_numeros():
     n = int(input("Cuantos numeros desea sumar: ")) #Pedir la cantidad de numeros
     sum = 0
     i = 0
     while n > 0: #ciclo while para guardar los numeros y sumarlos
         num = int(input("Ingrese el numero: "))
         sum = sum + num
         n = n - 1
     return(sum)

def restar_numeros():
    num1 = int(input("Ingrese primer numero: ")) #Pedir la cantidad de numeros
    num2 = int(input("Ingrese segundo numero: ")) #Pedir la cantidad de numeros   
    return num1 - num2 #retorna la resta

def division_numeros():
    dividendo = int(input("Ingrese dividendo: ")) #Pedir los numeros para dividir
    divisor = int(input("Ingrese divisor: ")) #Pedir los numeros para dividir
    if divisor == 0:
        return"ERROR: No se puede dividir entre 0" #comprabacion de numero porque no se puede dividir entre 0
    else:
        return dividendo / divisor

def multiplicar_numeros():
     n = int(input("Cuantos numeros desea multiplicar: ")) #Pedir la cantidad de numeros que se desean multiplicar
     mult = 1
     i = 0
     while n > 0: #ciclo while para guardar los numeros y multiplicar
         num = int(input("Ingrese el Numero: "))
         mult = mult * num
         n = n - 1
     return(mult)


def factorial_numero():
    num = int(input("Ingrese el numero: ")) #Pedir el numero que se desea el factorial
    if num < 0:
        return "ERROR: El factorial de un negativo no existe" #Comprobacion de datos ya que el factorial de 0 no existe
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial

def potencia_numero():
    base = int(input("Ingrese la base: ")) 
    exp = int(input("Ingrese el exponente: "))
    if base == 0 and exp == 0:      #Comprobacion de datos, ya que 0 a la 0 es una indeterminacion
        return "ERROR: No se puede realizar operacion"
    else:
       return base**exp

