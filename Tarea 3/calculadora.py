# Este es el modulo principal de la calculadora 
import menu
import arit
import log 
continuar = True
while continuar:
    print("\n*****************MENU PRINCIPAL*******************\n")
    print("1. Sumar la cantidad de numeros que desea \n")
    print("2. Restar 2 numeros \n")
    print("3. Multiplicar la cantidad de numeros que desea \n")
    print("4. Dividir 2 numeros \n")
    print("5. Factorial de un numero \n")
    print("6. Potencia de un numero \n")
    print("7. Salir \n")
    num = int(input("Eliga el numero de la operacion artimetica que desea: "))
    if num == 7:
      continuar = False
    elif num == 1: #Apartir de aqui se llama al modulo arit que contiene las funciones de las operaciones
       res = arit.sumar_numeros() #guarda el return de la funcion es la variable res. 
       print(f"El resultado de la operacion es: "+ str(res)) 
       log.log_resultado("El resultado de la suma es: "+ str(res))  # Genera el log
       menu.volver_menu() #funcion para volver al menu
    elif num == 2:
       res = arit.restar_numeros()
       print(f"El resultado de la resta es: "+ str(res))
       log.log_resultado("El resultado de la resta es: "+ str(res))    
       menu.volver_menu()  
    elif num == 3:
       res = arit.multiplicar_numeros()
       print(f"El resultado de la multiplicacion es: "+ str(res))
       log.log_resultado("El resultado de la multiplicacion es: "+ str(res)) 
       menu.volver_menu()  
    elif num == 4:
       res = arit.division_numeros()
       print(f"El resultado de la division es: "+ str(res))
       log.log_resultado("El resultado de la division es: "+ str(res))
       menu.volver_menu()  
    elif num == 5:
       res = arit.factorial_numero()
       print(f"El resultado del factorial es: "+ str(res))
       log.log_resultado("El resultado del factorial es: "+ str(res))
       menu.volver_menu()  
    elif num == 6:
       res = arit.potencia_numero()
       print(f"El resultado de la potencia es: "+ str(res))
       log.log_resultado("El resultado de la potencia es: "+ str(res))
       menu.volver_menu()  