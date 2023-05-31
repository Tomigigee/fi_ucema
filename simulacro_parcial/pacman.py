from ejercicio4v2 import pacman, rosa, fantasma, verde

print(pacman.vidas)
print(pacman.puntos)
pacman.comer_fantasma(fantasma, rosa)

print(pacman.puntos)

pacman.perder_vida()
print(pacman.vidas)
print(pacman.velocidad())

pacman.comer_fantasma(fantasma, verde)
print(pacman.velocidad())