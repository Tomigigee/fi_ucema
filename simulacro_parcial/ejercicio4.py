class PacMan:
    def __init__(self):
        self.puntos = 0
        self.vidas = 3
        #velocidad opcional
    
    def comer_bolita(self, cantidad):
        self.puntos += (cantidad*2)
    
    def velocidad(self):
        return (2 + self.puntos)/100
    
    def perder_vida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("Game over")
    
    def comer_fantasma(self, fantasma, color):
        self.puntos += fantasma.puntos_color(color)
class Fantasma:
    def __init__(self):
        self.fantasmas = {"rosa": 8, "verde": 6, "naranja": 4, "rojo": 2}
    
    def puntos_color(self, color):
        return self.fantasmas[color]
    


pacman = PacMan()
fantasma = Fantasma()
#fantasma
