import Mesa as M 
import os
import logs
import time
import reglas 

def repartir_jugador(mano_jugadores, mazo): #esta funcion sirve para repartir otra carta al jugador y le ingresa la mano del jugador y el mazo
    for hand in mano_jugadores:
        while True:
            print("\n*********PARTIDA EN PROGRESO******\n")
            hand.mostrar_mano(False)
            valor_palos = hand.valor_palo() # todos los palos se guardan en una lista. La cree solo para contar si hay 2 cartas
            print(f"El valor de su mano es: {hand.value}")
            if hand.value == 21 and (len(valor_palos) == 2): #si suma 21 y tiene 2 palos significa que tiene 2 cartas
                hand.value = 212
                return(hand.value)
            goon = input(f'{hand.jugador}, quiere otra carta? (Y/N): ')
            print("\n*********PARTIDA EN PROGRESO******\n")
            if goon == 'Y' or goon == 'y':
                hand.agregar_carta(mazo.repartir_carta()) #aca se agrega a la mano una carta nueva
                valores_mano = hand.valor_cartas()
                if valores_mano.count(7) == 3: #est es la condicion para mano de 3 7s 
                    hand.value = 210 #agrege este valor como indicador para que lo reconozca en la funcion Partida
                    return(hand.value)
                elif (len(valores_mano) == 5) and (hand.value <= 21): #esta es la condicion para ver si hay 5 cartas menores 
                    hand.value = 211
                    return(hand.value)
                elif hand.value > 21: #condicion para determinar si ya se paso de 21
                   hand.mostrar_mano(False)
                   print(f"El valor de su mano es {hand.value}")
                   print()
                   break
            elif goon == 'N' or goon == 'n':
                # os.system('cls')
                print(f"El valor de su mano es {hand.value}")
                break
            else:
                time.sleep(2)
                print('Por favor indique Y o N') #esta condicion se creo por si el usuario ingresa otra letra que no sea Y o N
                time.sleep(2)
    return(hand.value)


def repartir_casa(casamano, mazo): # esta es la funcion para repartir la mano a la Casa
    # os.system('cls')
    while casamano.value <= 14:
        casamano.agregar_carta(mazo.repartir_carta()) #la logica es que si tiene menor que 14 que pida otra carta
    
    if casamano.value >= 14 and casamano.value <= 17: #Si la carta que recibio no suma en total 17, entonces pide otra carta
        casamano.agregar_carta(mazo.repartir_carta())
    casamano.mostrar_mano(True)
    print(f"El valor de la mano de CASA es: {casamano.value}")
    return(casamano.value) #regresa el valor de la mano



def elegir_usuario (): #funcion para que el usuario elija usuario nuevo o existente
        continuar = True
        num = input("Escoga su opcion: \n 1- Usuario nuevo \n 2- Usuario existente \n 3-Salir\n")
        if num == "1":
            usuarios = logs.obtener_usario() #obtiene los usuario existentes para comprobar que ese usuario no exista
            seguir = input("Desea continuar? (Y/N):")
            if seguir == "Y" or seguir == 'y':
                while continuar:
                    usuario = str(input("Digite el nombre del usuario: \n"))
                    usuario = usuario.upper()
                    print(f"Su usuario es: {usuario}")
                    if usuario in usuarios:
                        print("Error: Usuario existente") #Si el usuario ya existe entonces muestra este error
                        time.sleep(2)
                    else:
                        logs.base_resultado(str(usuario)) # sino existe entonces comienza la partida
                        print(f"***Bienvenido: {usuario}***")
                        print("INICIANDO PARTIDA ...")
                        time.sleep(2)
                        os.system('cls')
                        return(usuario)
            elif seguir == "N" or seguir == "n":
                print("REGRESANDO AL MENU PRINCIPAL ... ")
                time.sleep(2)
                exit
            else:
                print("****ERROR:OPCION NO VALIDA****")
                time.sleep(1)
                print("REGRESANDO AL MENU PRINCIPAL ... ")
                time.sleep(2)
                exit 
        elif num =="2":
            usuarios = logs.obtener_usario() #obtiene los usuario de aca
            print("Esta es la lista de usuarios existentes: ")
            for user in usuarios: #con esto se imprimen los usuarios existentes
                print(user)
            seguir = input("Desea continuar? (Y/N):")
            if seguir == "Y" or seguir == 'y':
                usuario = input("Digite el nombre del usuario: \n")
                usuario = usuario.upper() #Con esto hacemos que a la hora de digiar el usuario sea indiferente la primera mayuscula
                if usuario in usuarios: #se comprueba que el usuario exista
                    os.system('cls')
                    print(f"********Bienvenido al BLACKJACK: {usuario}**********")
                    print("********INICIANDO PARTIDA********")
                    time.sleep(1)
                    return(usuario)
                else: #regresa un error si el usuario no existe y lo lleva de vuelta al menu principal
                    print("***********ERROR USUARIO NO EXISTENTE**********")
                    print("************REGRESANDO A MENU PRINCIPAL*********")
                    time.sleep(3)
            elif seguir == "N" or seguir == "n":
                print("REGRESANDO AL MENU PRINCIPAL ... ")
                time.sleep(2)
                exit
            else:
                print("****ERROR:OPCION NO VALIDA****")
                print("REGRESANDO AL MENU PRINCIPAL ... ")
                time.sleep(2)
                exit 

        elif num == "3":
            exit
        else:
            print("ERROR: REGRESANDO A MENU PRINCIPAL") #si ingresa una opcion no valida, regresa al menu principal
            time.sleep(1)
            print("REGRESANDO AL MENU PRINCIPAL ... ")
            time.sleep(2)

def Partida(user): #con esta funcion crea la partida contra la casa 
    if user == None:
        exit
    else:
        mano1 = M.Juego([user]) #crea la mano
        x= repartir_jugador(mano1.mano_jugadores, mano1.mazo) #reparte las cartas 
        if x == 210:
            print ("************HAS GANADO****************") #gana si tiene 3 7s 
            print("\n*********MANO ESPECIAL 7 7 7*********\n") 
            print("\n*********PARTIDA FINALIZADA************\n")
            print("\nREGRESANDO AL MENU PRINCIPAL .....\n")
            time.sleep(2)
            return"GANO 7 7 7"

        elif x ==211: #el usuario gana si tiene 5 menores
            print ("\n************HAS GANADO****************\n")
            print("\n*********MANO ESPECIAL 5 MENORES*********\n")
            print("\n*********PARTIDA FINALIZADA************\n")
            print("\nREGRESANDO AL MENU PRINCIPAL .....\n")
            time.sleep(2)
            return"GANO 5 MENORES"

        elif x == 212: #el usario gana si tiene 21 de  una vez en la mano, conocido como blackjack
            print ("\n************HAS GANADO****************\n")
            print("\n***********BLACKJACK***************\n")
            print("\n*********PARTIDA FINALIZADA************\n")
            print("\nREGRESANDO AL MENU PRINCIPAL .....\n")
            time.sleep(2)
            return"GANO BLACKJACK"

        elif x > 21: #pierde si la mano ya se paso de 21
            print ("************HAS PERDIDO****************")
            print("\n*********PARTIDA FINALIZADA************\n")
            time.sleep(2)
            print("\nREGRESANDO AL MENU PRINCIPAL .....\n")
            time.sleep(2)
            return"PERDIO"

        else: #con esta condicion juega la casa
                print("\nRepartiendo CASA ...")
                time.sleep(2)
                mano2 = M.Juego(["Casa"]) #crea la mano de la casa
                y = repartir_casa(mano2.mano_casa, mano2.mazo) #reparte la mano de la casa
                time.sleep(2)
                print("\n*************WINNER************\n") 
                win = reglas.Ganador(x, y, user) #esta funcion declara el ganador
                print(win)
                print("\n*********PARTIDA FINALIZADA************\n") #Una vez que la partida termina, regresa al menu principal
                print("\nREGRESANDO AL MENU PRINCIPAL .....\n")
                time.sleep(5)
                if win == user:
                    return"GANO"
                else:
                    return"PERDIO" 

