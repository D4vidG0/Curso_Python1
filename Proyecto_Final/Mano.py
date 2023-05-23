import baraja as B
VALORES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
class Mano:
    def __init__(self, jugador):
        self.jugador = jugador
        self.cartas = []
        self.value = 0
        self.carta = ()
        self.value2 = 0
        self.palos = " "
        
        
    def mostrar_mano(self, esbot = True): #este metodo es el que me muestra la mano de cada jugador
         for i in range(0, len(self.cartas)):
                if esbot == True and i == 0: #esbot se utliza para reprentar a la compu y si es True tira una carta tapada
                     print("CARTA TAPADA")
                else:
                     print(f"Su Carta es: "+str(self.cartas[i]))
    
    def agregar_carta(self, carta): #agrega la carta y la guarda en una lista. Tambien guarda el valor de la carta
         self.cartas.append(carta)
         self.value += VALORES[carta.valor]
   
    def valor_mano(self): #Cree este metodo sacar el valor de la mano y que se vaya sumando
         for carta in self.cartas:
              self.value += VALORES[carta.valor]
         return(self.value)
     
    def valor_cartas(self): #este metodo me guarda al valor de cada carta en una lista y la regresa solo con los valores (sin palo)
         valores =[]
         for i in range(0, len(self.cartas)):
              self.value2 = VALORES[self.cartas[i].valor]
              valores.append(self.value2)
         return valores
    
    def valor_palo(self):
          palos = []
          for i in range(0, len(self.cartas)):
              self.palos = VALORES[self.cartas[i].valor]
              palos.append(self.palos)
          return palos
     
    
      



# mano =[]
# mano = Mano("Dave")
# mazo = B.Baraja() #crea el mazo
# mazo.barajar() #baraja el mazo
# mano.agregar_carta(mazo.repartir_carta())
# mano.agregar_carta(mazo.repartir_carta())
# mano.mostrar_mano(False)
# # # print(f"El valor de su mano es {mano.valor_mano()}")
# # # mano.mostrar_mano(False)
# print(mano.valor_cartas())