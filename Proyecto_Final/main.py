import os
import jugador
import logs
import time

#Modulo principal donde se corre el programa y se junta los modulos

def menu_principal():
    logs.crear_base()
    continuar = True
    while continuar:
       os.system('cls')
       print("******MENU PRINCIPAL******") #Menu principal donde se pueden ver las estadisticas o jugar un juego nuevo de 21
       num = input("Ingrese la opcion que desea: \n 1- Juego nuevo BlackJack \n 2- Estadisticas de usuario \n 3- Salir\n")
       if num == "1":
          os.system('cls')
          user = jugador.elegir_usuario() #funcion para elegir el jugador
          resultado = jugador.Partida(user) #en la variable resultado se guarda al ganador de la partida
          logs.estadisticas_usuario(user , resultado) #con esta funcion se genera las estadisticas de cada usuario

       elif num =="2":
         users =logs.obtener_usario() #obtienes los usuarios y los guarda en una lista
         os.system('cls')
         print("****LISTA DE USUARIOS EXISTENTES****")
         for existente in users: #imprime los usuario existentes
            print(existente)
         user = input("Digite el usuario:")
         if user in users:
            logs.obtener_stats(user) #con esta funcion se obtienen las estadisticas
            cont = True
            while cont:
               ret = input("Digite RETURN para regresar al menu principal: \n") #el usuario tiene que escribir return para regresar
               ret = ret.lower()
               if ret == "RETURN" or ret == "return":
                  cont = False
         else:
            print("USUARIO NO EXISTE") #condicion que imprima error si el usuario no existe
            cont = True
            while cont:
               ret = input("Digite RETURN para regresar al menu principal: \n") #tiene que digitar return para regresar al menu principal
               ret = ret.lower() #con esto acepta cualquier variacion de la palabra return
               if ret == "RETURN" or ret == "return":
                  cont = False

       elif num == "3": #sale del programa
          os.system('cls')
          continuar = False

       else:
          print("ERROR: Opcion no valida. Favor de elegir opcion") #Indica error si digita algo que no se una de las opciones
          time.sleep(2)

menu_principal() #aca se llama a la funcion