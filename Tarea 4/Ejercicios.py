def contar_caracteres(string):
    string_clear = string.replace(" ", "") #quitando espacios del string
    contador = 0
    c2 = 0
    c3 = 0
    for chr in string_clear:
        if chr.isalpha(): #encuetra si es una letra
            contador += 1
        elif chr.isdigit(): #encuentra si es un digito
            c2 += 1
        else:  #todo lo demas son caracteres especiales
            c3 += 1  
    return contador, c2, c3 #devuelve los 3 contadores

def aparicion_caracteres(string):
    string_clear = string.replace(" ", "") #quitando espacios del string
    respuesta = dict() #se define un diccionario vacio para almacenar 
    for chr in string_clear:
        if  chr in respuesta.keys():
            respuesta[chr] = respuesta[chr] + 1 #cuenta solo si la letra ya esta guardada
        else:
            respuesta[chr] = 1 #primera aparicion de la letra
    return respuesta

def eliminar_lista(test = []):
    continuar = True
    while continuar:
        elem = input("Ingrese el elemento de la lista o digite Salir para salir\n") #se crea el while para que el usuario ingrese los datos que desee
        if elem == "Salir":
            continuar = False #digita Salir para Salir del programa
        else:
            test.append(elem) #append sirve para ir agregando los datos que ingreso el usuario
    for dato in test:
        if test.count(dato) > 1: #cuenta si el dato ya esta en la lista
            test.remove(dato) #elimina datos repetidos 
    continuar2 = True
    while continuar2:
        rem = input("INGRESE EL ELEMENTO QUE DESEA REMOVER: \n") #aca se le pide que borre el dato que desee
        if rem not in test : #cuenta si el dato ya esta en la lista
            print("ERROR: DATO NO ENCONTRADO")
        else:
            test.remove(rem) #remove borra el dato
            continuar2 = False
    return(test)

def devolver_lista_tupla(string):
    string_clear = string.replace(" ", "") #quitar espacios
    list = string_clear.split(",") #esta funcion los separa en lista cuando detecta la coma
    tupla = tuple(list) #esta funcion lo convierte en tupla
    return list , tupla

