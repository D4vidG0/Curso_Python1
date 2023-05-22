import baraja as B
import carta as C
import Mano as M
#este modulo es como la mesa donde se reparten las manos del jugador y de la casa

class Juego:
    def __init__(self, jugadores = []):
        self.jugadores = jugadores

        mazo = B.Baraja() #crea el mazo
        mazo.barajar() #baraja el mazo

        mano_jugadores = [] #variable para guardar la mano de jugadores

        for jugador in jugadores:
            mano = M.Mano(jugador) #crea mano de cada jugador
            mano.agregar_carta(mazo.repartir_carta()) #reparte 1 carta
            mano.agregar_carta(mazo.repartir_carta()) #reparte 1 carta
            mano_jugadores.append(mano) #guarda las manos
        casa =[]
        mano_casa = M.Mano(casa) #crea mano de la casa
        mano_casa.agregar_carta(mazo.repartir_carta()) #reparte 1 carta
        mano_casa.agregar_carta(mazo.repartir_carta()) #reparte 1 carta
        
        self.mazo = mazo
        self.mano_jugadores = mano_jugadores
        self.mano_casa = mano_casa

    


