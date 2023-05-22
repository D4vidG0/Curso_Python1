
class Carta:
   
    def __init__(self, palos, valor):#esta es la clase para definiar la carta
        
        self.palos = palos
        self.valor = valor
        
    def __str__(self):
       return f" {self.valor} {self.palos}" #regresa el valor de la carta y el palo
    
