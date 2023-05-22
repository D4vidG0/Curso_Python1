palos = ["♠","♣","♥","♦"]
valor = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
baraja = []

for v in valor:
    for p in palos:
        carta = str(f"{v} de {p}")
        baraja.append(carta)


print(baraja)