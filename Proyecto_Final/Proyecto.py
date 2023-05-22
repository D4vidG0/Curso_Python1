import random
palos = ["♠","♣","♥","♦"]
valor = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
baraja = []

class Carta:
   
    def __init__(self, palos, numero, valor):
        
        self.palos = palos
        self.numero = numero
        self.valor = valor
        
    def __str__(self):
       return f"Carta {self.palos} {self.numero}"


    
class Mazo(Carta):

    def Mazo(self):
        for v in valor:
            for palos in palos:
                baraja.append(valor + palos)
                return(baraja)


carta1 = Carta("10","♠",10)
print(carta1)
