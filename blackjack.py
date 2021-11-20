from random import choice, sample

#Baraja

picas = {chr(0x1f0a1): 11, chr(0x1f0a2): 2, chr(0x1f0a3): 3, chr(0x1f0a4): 4, chr(0x1f0a5): 5, chr(0x1f0a6): 6, chr(0x1f0a7): 7, chr(0x1f0a8): 8, chr(0x1f0a9): 9, chr(0x1f0aa): 10, chr(0X1f0ab): 10, chr(0x1f0ad): 10, chr(0x1f0ae): 10}
corazones = {chr(0x1f0b1): 11, chr(0x1f0b2): 2, chr(0x1f0b3): 3, chr(0x1f0b4): 4, chr(0x1f0b5): 5, chr(0x1f0b6): 6, chr(0x1f0b7): 7, chr(0x1f0b8): 8, chr(0x1f0b9): 9, chr(0x1f0ba): 10, chr(0X1f0bb): 10, chr(0x1f0bd): 10, chr(0x1f0be): 10}
rombos = {chr(0x1f0c1): 11, chr(0x1f0c2): 2, chr(0x1f0c3): 3, chr(0x1f0c4): 4, chr(0x1f0c5): 5, chr(0x1f0c6): 6, chr(0x1f0c7): 7, chr(0x1f0c8): 8, chr(0x1f0c9): 9, chr(0x1f0ca): 10, chr(0X1f0cb): 10, chr(0x1f0cd): 10, chr(0x1f0ac): 10}
treboles = {chr(0x1f0d1): 11, chr(0x1f0d2): 2, chr(0x1f0d3): 3, chr(0x1f0d4): 4, chr(0x1f0d5): 5, chr(0x1f0d6): 6, chr(0x1f0d7): 7, chr(0x1f0d8): 8, chr(0x1f0d9): 9, chr(0x1f0da): 10, chr(0X1f0db): 10, chr(0x1f0dd): 10, chr(0x1f0de): 10}

baraja = {**picas, **corazones, **rombos, **treboles}

#Valor de cada carta

print("Cartas {}:".format(" ".join(baraja.keys())))
print("Valores de las cartas {}".format(list(baraja.values())))

for carta, valor in baraja.items():
    print("Las cartas {} valen {}".format(carta, valor))

lista_baraja = list(baraja)

#Mano del jugador

print("Sus cartas:", end=" ")
carta_jugador = choice(lista_baraja)
score_jugador = baraja[carta_jugador]
print(carta_jugador, end=" ")
carta_jugador = choice(lista_baraja)
score_jugador += baraja[carta_jugador]
print(carta_jugador, end=" ")
print("Puntuación total: ", score_jugador)

#Mano del casino

print("La mano del casino:", end=" ")
carta_casino = choice(lista_baraja)
score_casino = baraja[carta_casino]
print(carta_casino, end=" ")
carta_casino = choice(lista_baraja)
score_casino += baraja[carta_casino]
print(carta_casino, end=" ")
print("Puntuación total: ", score_casino)

#Ganador

while score_jugador != score_casino:
    if score_jugador > score_casino:
        print("Ganaste la mano")
    if score_jugador < score_casino:
        print("Perdiste la mano")
    if score_jugador == score_casino:
        print("Empate, no hay ganador")
    break









