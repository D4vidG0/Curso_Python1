from datetime import datetime

def crear_base(): #crea base de datos
     file = open("base_datos.txt", "a") #Abre el archivo es modo append para agregar lineas
     file.close()

def base_resultado(string): #agrega usuario a la base de datos 
    file = open("base_datos.txt", "a") #Abre el archivo es modo append para agregar lineas
    file.write(string) #Escribe el string que es nuestro caso es el resultado de la operacion
    file.write("\n") #Puse este salto de linea para que los resultados no queden pegados
    file.close()

def obtener_usario(): #obtiene de la base de datos los usuarios y los guarda en una lista
    usuarios = []
    file = open("base_datos.txt")
    for linea in file:
        usuarios.append(linea.rstrip("\n")) #Agrega cada nombre de usuario a una lista y la regresa
    file.close()
    return(usuarios)
    
def estadisticas_usuario(usuario, resultado):
    f = open(f'{usuario}-stats.txt', 'a') #crea archivo unico de estadistica para cada usuario
    now=datetime.today() #Agrega la hora
    fecha = now.strftime("%c")
    f.write(f"FECHA: {fecha} USUARIO: {usuario}  RESULTADO: {resultado}")
    f.write("\n") #Puse este salto de linea para que los resultados no queden pegados
    f.close()

def obtener_stats(usuario): #obtiene cada usuario
    try: #con este imprime en la terminal las estadisticas si el archivo de estadisticas existe
        f = open(f'{usuario}-stats.txt')
        for linea in f:
            print(linea)
        f.close()
    except FileNotFoundError: #Si el usuario existe pero no ha jugado una partida, el archivo no existe y tira este error. 
        print("*****Lo sentimos el jugador todavia no ha jugado una partida****")
        


        


# usuario = "Dave"
# resultado = "Gano"
# ganadas = 10
# perdidas = 7
# porce = str(porcentaje_ganadas(ganadas,perdidas))
# estadisticas_usuario(usuario, resultado, porce)