import carta as C
import random

palos = ["♠","♣","♥","♦"]
valor = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Baraja:
    
    def __init__(self):
        self.baraja = []
        for v in valor:
            for p in palos:
                self.baraja.append(C.Carta(p,v)) #Aca se crea la baraja tomando los valores y palos de la lista de arriba
    

    def barajar(self):
        random.shuffle(self.baraja)

    def repartir_carta(self):
        cartajugador = self.baraja.pop(0) # con este reparta la primera carta del deck 
        return cartajugador
        

    
    def print_mazo(self): #cree  este metodo para imprimir el mazo, pero al final no lo use mas que para pruebas
        for i in (self.baraja):
            print(i, end=" ")

                