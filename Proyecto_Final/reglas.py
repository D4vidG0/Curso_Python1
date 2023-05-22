#este modulo sirve para definir la reglas de quien gana y regresa el nombre del ganador. 

def Ganador(jugador,casa,player):
    if casa == 21 and jugador == 21:
        return"CASA"
    elif casa > jugador and casa < 21:
        return"CASA"
    elif casa > jugador and casa == 21:
        return"CASA"
    elif casa > 21 and jugador < 21:
        return player
    elif casa < 21 and jugador == 21:
        return player
    elif jugador < 21 and casa > 21:
        return player
    elif jugador < 21 and casa ==21:
        return player
    elif jugador == 21 and casa > 21:
        return player
    elif casa == 21 and jugador > 21:
        return"CASA"
    elif casa < 21 and jugador < 21 and jugador > casa:
        return player
    elif casa < 21 and jugador < 21 and casa > jugador:
        return"CASA"
    elif casa == jugador and casa < 21:
        return"CASA"
    elif jugador >21:
        return "Casa"
    elif casa > 21:
        return  player










    

    